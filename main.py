from utils import parseClipsToJson, buildText
import yaml
import os

# Load file
with open('/Volumes/Kindle/documents/My Clippings.txt', 'r') as file:
    content = file.read()

# Load config
with open('config.yaml') as file:
    config = yaml.safe_load(file)

    ignorable = set(config['ignorable'])
    exportDir = config['exportDir']

    if not os.path.exists(exportDir):
        os.mkdir(exportDir)

bookclips = parseClipsToJson(content)

for book, clips in bookclips.items():
    if book not in ignorable:
        newcontent = buildText(clips)
        filename = f'{exportDir}/{book}.md'
        with open(filename, 'w') as file:
            file.write(newcontent)
            print(f'WROTE TO FILE: {filename}')
