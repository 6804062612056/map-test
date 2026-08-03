[app]

# Application name
title = map

# Package name (ต้องเป็นตัวเล็ก ไม่มีขีด)
package.name = map

# ต้องเป็น domain จริงรูปแบบ reverse domain
package.domain = com.guy


# Source
source.dir = .


# Include files
source.include_exts = py,kv,png,jpg,atlas,txt


# Version
version = 1.0.0
android.numeric_version = 10000


# Python + libraries
requirements = python3==3.11,kivy==2.3.1,kivy_garden.mapview,plyer


# Python version
p4a.python_version = 3.11


# Android permissions
android.permissions = INTERNET,ACCESS_FINE_LOCATION,ACCESS_COARSE_LOCATION


# Orientation
orientation = portrait


# Fullscreen
fullscreen = 0


[buildozer]

log_level = 2
