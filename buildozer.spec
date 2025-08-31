[app]
# App name (what shows on Android)
title = MyPythonApp

# Name of your main .py file (don’t include .py)
# Example: if your file is main.py → write "main"
source.main = main

# Package name (like com.example.myapp)
package.name = mypythonapp

# Unique package domain (must be reversed)
package.domain = org.example

# App version
version = 1.0

# Requirements: list libraries your app uses
# (keep python3,kivy for basic app)
requirements = python3,kivy

# The file to launch
source.include_exts = py,png,jpg,kv,atlas

# Orientation (portrait or landscape)
orientation = portrait

# Icon (optional, must be a .png in your project folder)
# icon.filename = %(source.dir)s/icon.png

# Permissions (uncomment if needed)
# android.permissions = INTERNET

# Supported architectures (armeabi-v7a = most Android phones)
android.archs = armeabi-v7a

# The format to build: apk or aab
android.api = 33
android.minapi = 21
android.sdk = 33
android.ndk = 25b

[buildozer]
log_level = 2
warn_on_root = 1
