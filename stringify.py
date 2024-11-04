# This was to convert the hiragana.json to a string, don't worry about this :)

import json

with open('hiragana.json', 'r', encoding='utf-8') as file:
    data = json.load(file)
kana_string = ' '.join(item['kana'] for item in data)
print(kana_string)
