# I made this when making the phoneme dictionary to help keep track of progress, shoutout to KotaruComplex's playlist which helped me lock-in

import json
import pykakasi


with open('phoneme.json', 'r', encoding='utf-8') as phoneme_file:
    phoneme_data = json.load(phoneme_file)

excluded_romaji = {item['romaji'] for item in phoneme_data}


kakasi = pykakasi.kakasi()


def convert_to_romaji_and_count(hiragana):
    result = kakasi.convert(hiragana)
    included_count = 0
    excluded_count = 0
    romaji_string = ''
    
    for item in result:
        hepburn = item['hepburn']
        if hepburn in excluded_romaji:
            excluded_count += 1
        else:
            romaji_string += hepburn
            included_count += 1
    
    return romaji_string, included_count, excluded_count


kana_string = "あ い う え お か き く け こ さ し す せ そ た ち つ て と な に ぬ ね の は ひ ふ へ ほ ま み む め も や ゆ よ ら り る れ ろ わ を ん が ぎ ぐ げ ご ざ じ ず ぜ ぞ だ ぢ づ で ど ば び ぶ べ ぼ ぱ ぴ ぷ ぺ ぽ っ きゃ きゅ きょ しゃ しゅ しょ ちゃ ちゅ ちょ にゃ にゅ にょ ひゃ ひゅ ひょ みゃ みゅ みょ りゃ りゅ りょ ぎゃ ぎゅ ぎょ じゃ じゅ じょ びゃ びゅ びょ ぴゃ ぴゅ ぴょ"
converted_romaji, included_count, excluded_count = convert_to_romaji_and_count(kana_string)
total_count = included_count + excluded_count
remaining_count = included_count - excluded_count

print(converted_romaji)
print("Count of non-excluded romaji:", included_count)
print("Count of excluded romaji:", excluded_count)
print("Count of all romaji:", total_count)
print("Remaining Count of all romaji:", remaining_count)
