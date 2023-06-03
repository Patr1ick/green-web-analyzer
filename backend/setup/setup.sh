#!/bin/bash

CHROMIUM_URL="https://www.googleapis.com/download/storage/v1/b/chromium-browser-snapshots/o/Linux_x64"

LATEST_VERSION=`wget -q -O - "$CHROMIUM_URL%2FLAST_CHANGE?alt=media" `

echo "Downloading version: $LATEST_VERSION"

# Chromium
wget -q -O chromium.zip $CHROMIUM_URL%2F$LATEST_VERSION%2Fchrome-linux.zip?alt=media
unzip -q chromium.zip
rm chromium.zip

# Chromedriver
wget -q -O chromedriver.zip $CHROMIUM_URL%2F$LATEST_VERSION%2Fchromedriver_linux64.zip?alt=media
unzip -q chromedriver.zip
rm chromedriver.zip

/etc/init.d/dbus start