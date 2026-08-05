[app]

title = map
package.name = map
package.domain = com.guy

source.dir = .
source.include_exts = py,kv,png,jpg,jpeg,atlas,txt,json

version = 1.0.0
android.numeric_version = 10000

requirements = python3,kivy==2.3.1,mapview,plyer,requests,certifi

android.api = 33
android.minapi = 24

android.accept_sdk_license = True

android.permissions = INTERNET,ACCESS_FINE_LOCATION,ACCESS_COARSE_LOCATION,ACCESS_NETWORK_STATE

orientation = portrait
fullscreen = 0

android.archs = arm64-v8a, armeabi-v7a

android.presplash_color = #FFFFFF

android.logcat_filters = *:S python:D


[buildozer]
log_level = 2
