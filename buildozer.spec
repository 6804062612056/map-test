[app]

title = map

package.name = map
package.domain = com.guy

source.dir = .

source.include_exts = py,kv,png,jpg,atlas,txt


version = 1.0.0
android.numeric_version = 10000


requirements = python3,kivy==2.3.1,kivy_garden.mapview,plyer


android.api = 33
android.minapi = 24

android.build_tools_version = 35.0.0

android.accept_sdk_license = True


android.permissions = INTERNET,ACCESS_FINE_LOCATION,ACCESS_COARSE_LOCATION


orientation = portrait

fullscreen = 0



[buildozer]

log_level = 2
