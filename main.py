from utils import parseClipsToJson, buildText, notify
import yaml
import os
import time


# Load config
try:
    containingDir = os.path.abspath(os.path.dirname(__file__))
    with open(os.path.join(containingDir, 'config.yaml')) as file:
        config = yaml.safe_load(file)

        ignorable = set(config['ignorable'])
        exportDir = config['exportDir']
        clippingsFilePath = config['clippingsFilePath']
        systemNotifications = config['systemNotifications']

        assert os.path.exists(clippingsFilePath), f'Clippings filepath does not exist: {clippingsFilePath}'

        if not os.path.exists(exportDir):
            os.mkdir(exportDir)

    # Load clippings file
    with open(clippingsFilePath, 'r') as file:
        content = file.read()
except Exception as e:
    # Give notification
    if systemNotifications:
        notify('KINDLE CLIPS ERROR', str(e))
    raise e

bookclips = parseClipsToJson(content)

for book, clips in bookclips.items():
    if book not in ignorable:
        newcontent = buildText(clips)
        filename = os.path.join(exportDir, f"{book}.md")
        with open(filename, 'w') as file:
            file.write(newcontent)
            print(f'WROTE TO FILE: {filename}')

# Notify of success
if systemNotifications:
    notify('Kindle Clips Updated', 'Your kindle highlights have been updated.')