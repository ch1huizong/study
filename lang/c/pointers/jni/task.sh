#!/usr/bin/bash

cd ..
ndk-build

adb push ./libs/armeabi-v7a/m /data/local/tmp

adb shell "chmod +x /data/local/tmp/m"

adb shell "/data/local/tmp/m"
