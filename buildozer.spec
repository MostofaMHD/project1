# (app)
[app]

# (str) Title of your application
title = SWG Game

# (str) Package name
package.name = snakewatergun

# (str) Package domain (needed for android/ios packaging)
package.domain = org.something

# (str) Source directory
source.dir = .

# (str) Source code where the main.py lives
source.include_exts = py,png,jpg,kv

# (str) Supported orientation (one of landscape, sensorLandscape, portrait, or all)
orientation = portrait

# (bool) Indicate if the application should be fullscreen or not
fullscreen = 0

# (int) Target Android API, should be as high as possible.
android.api = 27

# (int) Minimum API required
android.minapi = 21

# (int) Android SDK version to use
android.sdk = 27

# (list) Permissions
android.permissions = INTERNET

# (str) Version
version = 0.1

# (app requirements)
[app_requirements]

# (list) Application requirements
# comma separated e.g. requirements = sqlite3,kivy
python3 = python3,kivy,Pillow,random