import json

def buildText(clips):
    clips = sorted(clips, key=lambda c: c['location'])
    entries = []
    for clip in clips:
        page = clip['page'].replace('Highlight on ', '')

        entry = f"**{page} ({clip['location']})**\n\n"
        entry += f"**Date: {clip['date']}**\n"
        entry += f">{clip['text']}\n"
        entry += '---\n'
        entries.append(entry)

    newcontent = '\n'.join(entries)
    return newcontent


# Load filecontents
filename = 'data.json'
with open(filename) as file:
    bookclips = json.load(file)

with open('ignorable-books.txt') as file:
    ignorable = set(file.read().strip().split('\n'))


counter = 1
indexes = {}
for book, clips in bookclips.items():
    if book not in ignorable:
        indexes[counter] = book
        counter += 1


        # selectedClips = bookclips[title]
        # selectedClips = sorted(selectedClips, key=lambda c: c['location'])

        newcontent = buildText(clips)
        filename = f'exports/{book}.md'
        with open(filename, 'w') as file:
            file.write(newcontent)
            print(f'WROTE TO FILE: {filename}')

