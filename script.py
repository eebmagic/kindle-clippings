import json

# Load file
with open('/Volumes/Kindle/documents/My Clippings.txt', 'r') as file:
    content = file.read()

clips = {}
curr = []
lines = content.split('\n')
for i, line in enumerate(lines):
    curr.append(line)
    if line.startswith('===') and line.endswith('==='):

        # Parse data
        book = curr[0].strip()
        if not book.isascii():
            book = book[1:]
        data = curr[1][2:]
        text = curr[3]
        values = [val.strip() for val in data.split(' | ')]
        if len(values) == 3:
            page, location, date = values
        elif len(values) == 2:
            page, date = values
            location = None

        # Build entry
        clipping = {
            "page": page,
            "location": location,
            "date": date,
            "text": text
        }

        # Add to dict
        if book not in clips:
            clips[book] = [clipping]
        else:
            clips[book].append(clipping)

        # Reset for next book
        curr = []


# Dump to file
filename = 'data.json'
with open(filename, 'w') as file:
    json.dump(clips, file, indent=2)
    print(f'DUMPED TO FILE: {filename}')
