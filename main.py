from kivy.app import App
from kivy.clock import Clock
from kivy.uix.floatlayout import FloatLayout

from kivy_garden.mapview import MapView, MapMarker
from plyer import gps, compass

from kivy.graphics import PushMatrix, PopMatrix, Rotate


# 🔥 Marker ลูกศร (หมุนได้)
class ArrowMarker(MapMarker):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.angle = 0

    def set_angle(self, angle):
        self.angle = angle
        self.canvas.before.clear()
        with self.canvas.before:
            PushMatrix()
            Rotate(angle=self.angle, origin=self.center)
        self.canvas.after.clear()
        with self.canvas.after:
            PopMatrix()


class MapScreen(FloatLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        # 🗺️ Map เริ่มต้น (Bangkok)
        self.map = MapView(zoom=15, lat=13.736717, lon=100.523186)
        self.add_widget(self.map)

        self.marker = None  # ❗ ยังไม่สร้างจนกว่า GPS จะมา

        # 📍 GPS
        try:
            gps.configure(on_location=self.on_location)
            gps.start(minTime=1000, minDistance=1)
        except:
            print("GPS not supported")

        # 🧭 Compass
        try:
            compass.enable()
        except:
            print("Compass not supported")

        # 🔄 update ทุก 0.5 วิ
        Clock.schedule_interval(self.update, 0.5)


    # 📍 เมื่อ GPS ได้ตำแหน่ง
    def on_location(self, **kwargs):
        lat = kwargs['lat']
        lon = kwargs['lon']

        print("GPS:", lat, lon)

        # สร้าง marker ครั้งแรก
        if not self.marker:
            self.marker = ArrowMarker(
                lat=lat,
                lon=lon,
                source="arrow.png"  # 👈 ต้องมีไฟล์นี้
            )
            self.map.add_marker(self.marker)
        else:
            self.marker.lat = lat
            self.marker.lon = lon

        # เลื่อน map ตาม
        self.map.center_on(lat, lon)


    # 🧭 หมุนลูกศรตามทิศ
    def update(self, dt):
        try:
            heading = compass.orientation
            if heading is not None and self.marker:
                self.marker.set_angle(heading)
        except:
            pass


class MainApp(App):
    def build(self):
        return MapScreen()

    def on_start(self):
        # 🔐 ขอ permission (Android เท่านั้น)
        try:
            from android.permissions import request_permissions, Permission
            request_permissions([
                Permission.ACCESS_FINE_LOCATION,
                Permission.ACCESS_COARSE_LOCATION
            ])
        except:
            pass


if __name__ == "__main__":
    MainApp().run()
