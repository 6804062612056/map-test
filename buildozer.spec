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
requirements = python3==3.11,kivy==2.3.1,kivy_garden.mapview,plyer

# Python version สำหรับ python-for-android
p4a.python_version = 3.11

# GPS Permission
android.permissions = ACCESS_FINE_LOCATION,ACCESS_COARSE_LOCATION

# (str) Supported orientation
orientation = portrait

# (bool) Fullscreen
fullscreen = 0


[buildozer]

# (int) Log level
log_level = 2
