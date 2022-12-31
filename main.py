from utils import parseClipsToJson, buildText

# Load file
with open('/Volumes/Kindle/documents/My Clippings.txt', 'r') as file:
    content = file.read()

# Load ignorable
with open('ignorable-books.txt', 'r') as file:
    ignorable = set(file.read().strip().split('\n'))

bookclips = parseClipsToJson(content)

for book, clips in bookclips.items():
    if book not in ignorable:
        newcontent = buildText(clips)
        filename = f'exports/{book}.md'
        with open(filename, 'w') as file:
            file.write(newcontent)
            print(f'WROTE TO FILE: {filename}')
