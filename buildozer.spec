[app]
title = Frostnerjo Miner
package.name = frostminer
package.domain = org.frostprotocol
source.include_exts = py,png,jpg,kv,atlas
version = 1.1.0

# ⚠️ THE INTERLINK: Permissions
# This allows the app to see your local WiFi node and use the internet
android.permissions = INTERNET, ACCESS_NETWORK_STATE, WAKE_LOCK

# Icon & Splash (Use your generated Amiah Doodles here)
icon.filename = assets/icon_frost.png
presplash.filename = assets/splash_amiah.png
[app]

# (str) Title of your application
title = Frost Crush

# (str) Package name
package.name = frostcrush

# (str) Package domain (needed for android/ios packaging)
package.domain = org.jacobfrost

# (str) Source code where the main.py live
source.dir = .

# (list) Source files to include (let empty to include all the files)
source.include_exts = py,png,jpg,kv,atlas

# (str) Application versioning (method 1)
version = 0.1

# (list) Application requirements
# comma separated e.g. requirements = sqlite3,kivy
requirements = python3,kivy

# (str) Custom source folders for requirements
# Sets custom source for some requirements with recipe
# requirements.source.kivy = ../../kivy

# (str) Presplash of the application
# presplash.filename = %(source.dir)s/data/presplash.png

# (str) Icon of the application
# icon.filename = %(source.dir)s/data/icon.png

# (list) Supported orientations
# Valid options are: landscape, portrait, portrait-reverse or landscape-reverse
orientation = portrait

# (bool) Indicate if the application should be fullscreen or not
fullscreen = 1

# (string) Presplash background color (for new android toolchain)
# Supported formats are: #RRGGBB #AARRGGBB or one of the following names:
# red, blue, green, black, white, gray, cyan, magenta, yellow, lightgray,
# darkgray, gray, lightgrey, darkgrey, grey, pearl, onyx
android.presplash_color = #000000

# (list) Permissions
android.permissions = INTERNET

# (int) Target Android API, should be as high as possible.
android.api = 31

# (int) Minimum API your APK will support.
android.minapi = 21

# (bool) If True, then skip trying to update the Android sdk
# This can be useful to avoid excess downloads
android.skip_update = False

# (bool) If True, process data content using the new AssetLoader
# This is usually required for Kivy apps
android.accept_sdk_license = True

# (str) The Android arch to build for, choices: armeabi-v7a, arm64-v8a, x86, x86_64
android.archs = arm64-v8a

[buildozer]

# (int) Log level (0 = error only, 1 = info, 2 = debug (with command output))
log_level = 2

# (int) Display warning if buildozer is run as root (0 = False, 1 = True)
warn_on_root = 0
