from kivy.config import Config

Config.set('graphics', 'width', '360')
Config.set('graphics', 'height', '800')

from kivy.app import App
from kivy.clock import Clock
from kivy_garden.mapview import MapView, MapMarker, MapSource
from plyer import gps


class GPSMarker(MapMarker):
    pass


class MapApp(App):

    def build(self):

        self.map = MapView(
            zoom=16,
            lat=13.7563,
            lon=100.5018
        )

        self.marker = GPSMarker(
            lat=13.7563,
            lon=100.5018
        )

        self.map.add_marker(self.marker)

        # เริ่ม GPS
        try:
            gps.configure(
                on_location=self.update_location,
                on_status=self.gps_status
            )

            gps.start(
                minTime=1000,
                minDistance=1
            )

        except Exception as e:
            print(e)

        return self.map


    def update_location(self, **kwargs):

        lat = kwargs['lat']
        lon = kwargs['lon']

        print("GPS:", lat, lon)

        # ย้าย marker
        self.marker.lat = lat
        self.marker.lon = lon

        # เลื่อนแผนที่ตามตำแหน่ง
        self.map.center_on(lat, lon)


    def gps_status(self, stype, status):
        print(stype, status)



if __name__ == "__main__":
    MapApp().run()