[app]

# (str) Title of your application
title = map

# (str) Package name
package.name = map

# (str) Package domain
package.domain = com.guy


# (str) Source code directory
source.dir = .

# (list) Source files to include
source.include_exts = py,kv,png,jpg,atlas,txt

# (str) Application version
version = 1.0.0
android.numeric_version = 10000

# (list) Requirements
requirements = python3,kivy,kivy_garden.mapview,plyer
android.permissions = ACCESS_FINE_LOCATION,ACCESS_COARSE_LOCATION

# (str) Supported orientation
orientation = portrait

# (bool) Fullscreen
fullscreen = 0


[buildozer]

# (int) Log level
log_level = 2