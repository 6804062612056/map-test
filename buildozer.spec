[app]

title = map
package.name = map
package.domain = com.guy

source.dir = .
source.include_exts = py,kv,png,jpg,atlas,txt

version = 1.0.0
android.numeric_version = 10000

# 🔥 แก้ตรงนี้สำคัญ
requirements = python3,kivy==2.3.1,mapview,plyer,requests,certifi

android.api = 33
android.minapi = 24

android.accept_sdk_license = True

android.permissions = INTERNET,ACCESS_FINE_LOCATION,ACCESS_COARSE_LOCATION

orientation = portrait
fullscreen = 0

# กันพัง + รองรับมือถือ
android.archs = arm64-v8a, armeabi-v7a

# กันจอดำ
android.presplash_color = #FFFFFF


[buildozer]
log_level = 2
