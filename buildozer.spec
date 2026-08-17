[app]

title = Basketball Tracker
package.name = basketballtracker
package.domain = org.basketballtracker
source.dir = .
version = 1.0
requirements = python3,kivy
orientation = portrait
fullscreen = 0

[buildozer]

log_level = 2
warn_on_root = 1

[android]

android.api = 35
android.minapi = 21
android.arch = arm64-v8a
android.entrypoint = org.kivy.android.PythonActivity
