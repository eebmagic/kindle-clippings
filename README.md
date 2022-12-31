# Kindle Clippings

This code is meant to be run when a kindle device is mounted.
Should automatically convert your `My Clippings.txt` file to a markdown file for each book.

## Setting up for yourself
There are a few parameters you'll want to change int he `config.yaml` file.
- Change the `exportDir` variable to be where you want the `.md` files dumped to.
- If you're not on MacOS or your kindle device mounts with a different name, then you'll want to change the `clippingsFilePath` variable to match.
- If you don't want notifications on runs, set `systemNotifications` to **False**.
- If you have books that you don't want parsed, then edit the `ignorable` list.

### Automating on device mount
If on MacOS you can use [launchctl](https://ss64.com/osx/launchctl.html) to automate running the `main.py` script on kindle device mount.

The `.plist` file should look something like this:
```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
    <key>Label</key>
    <string>com.kindle.parse-highlights</string>
    <key>ProgramArguments</key>
    <array>
        <string>/usr/local/bin/python</string>
        <string>/Users/username/Documents/kindle-clippings/main.py</string>
    </array>
    <key>WatchPaths</key>
    <array>
        <string>/Volumes/Kindle</string>
    </array>
</dict>
</plist>
```
**NOTES:**
- Make sure the filename is `com.kindle.parse-highlights`.
- Replace `/usr/local/bin/python` with whatever path your preffered python executable is
- Replace `/Users/username/Documents/kindle-clippings/main.py` with the correct path to wherever you've cloned this repo.
