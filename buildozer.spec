[app]
title = VideoBot Studio
package.name = videobotstudio
package.domain = org.baowpheem
source.dir = .
source.include_exts = py,png,jpg,kv,atlas,json,ttf
requirements = python3,kivy==2.3.1,requests
orientation = portrait
fullscreen = 0

[app:android]
android.permissions = INTERNET,READ_MEDIA_VIDEO,READ_MEDIA_IMAGES,CAMERA,RECORD_AUDIO,WRITE_EXTERNAL_STORAGE
android.api = 33
android.minapi = 21
android.ndk = 25b
android.sdk = 33
android.accept_sdk_licenses = True

[buildozer]
log_level = 2
warn_on_root = 1
