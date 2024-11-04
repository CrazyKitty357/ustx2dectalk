# This is the script that replaces the phonemes in vocal.txt with dectalk phonemes

import json
import re

# Load phoneme mappings from phoneme.json
with open('phoneme.json', 'r', encoding='utf-8') as f:
    phoneme_data = json.load(f)

# Load the vocal.txt file contents
with open('vocal.txt', 'r', encoding='utf-8') as f:
    vocal_text = f.read()

# Sort phonemes by length of "romaji" to avoid partial matches
# Longer romaji strings are replaced first to avoid overlapping issues
phoneme_data = sorted(phoneme_data, key=lambda x: len(x['romaji']), reverse=True)

# Replace each Romaji string with the corresponding Dectalk string using regex word boundaries
for phoneme in phoneme_data:
    romaji = phoneme['romaji']
    dectalk = phoneme['dectalk']
    # Use regex to replace only whole words to prevent partial replacements
    vocal_text = re.sub(r'\b' + re.escape(romaji) + r'\b', dectalk, vocal_text)

# Overwrite the vocal.txt file with the updated text
with open('vocal.txt', 'w', encoding='utf-8') as f:
    f.write(vocal_text)

print("Replacements completed and saved to vocal.txt!")
