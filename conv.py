# This is the main script, I got no other comments here. If you go to the other 

import json
import sys
import re
import subprocess
from math import pow
from pykakasi import kakasi

# Set up pykakasi for Hiragana to Romaji conversion
kakasi_instance = kakasi()
kakasi_instance.setMode("H", "a")  # Hiragana to Romaji
converter = kakasi_instance.getConverter()

# Define the pitch table for mapping Hz to custom pitch values
pitch_table = {
    65.41: 1, 69.30: 2, 73.42: 3, 77.78: 4, 82.41: 5, 87.31: 6, 
    92.50: 7, 98.00: 8, 103.83: 9, 110.00: 10, 116.54: 11, 123.47: 12,
    130.81: 13, 138.59: 14, 146.83: 15, 155.56: 16, 164.81: 17, 
    174.61: 18, 185.00: 19, 196.00: 20, 207.65: 21, 220.00: 22,
    233.08: 23, 246.94: 24, 261.63: 25, 277.18: 26, 293.66: 27,
    311.13: 28, 329.63: 29, 349.23: 30, 369.99: 31, 392.00: 32,
    415.30: 33, 440.00: 34, 466.16: 35, 493.88: 36, 523.25: 37
}

# Convert MIDI note to frequency in Hz
def midi_to_hz(midi_note):
    return round(440.0 * pow(2, (midi_note - 69) / 12.0), 2)

# Parse the USTX file and generate both DECtalk formats
def convert_ustx_to_dectalk(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        data = file.read()

    # Extract note data
    note_pattern = r'- position: (\d+)\s+duration: (\d+)\s+tone: (\d+)\s+lyric: (\S+)'
    notes = re.findall(note_pattern, data)

    tones_output = []
    vocal_output = []

    previous_end_position = 0

    for position, duration, tone, hiragana_lyric in notes:
        position = int(position)
        duration = int(duration)
        midi_tone = int(tone)
        
        # Check for a rest between notes
        if position > previous_end_position:
            rest_duration = position - previous_end_position
            tones_output.append(f":t0 {rest_duration}")
            vocal_output.append(f"_<{rest_duration},0>")
        
        # Convert tone (MIDI to Hz) and round it to match pitch table keys
        tone_hz = midi_to_hz(midi_tone)
        
        # Convert Hiragana lyric to Romaji
        romaji_lyric = converter.do(hiragana_lyric)

        # Check if tone_hz exists in pitch_table
        vocal_tone = pitch_table.get(tone_hz)
        if vocal_tone is None:
            print(f"Skipping tone {tone_hz} Hz as it is not in the pitch table.")
            continue
        
        # Append to tones format
        tones_output.append(f":t{int(tone_hz)} {duration}")
        
        # Append to vocal format
        vocal_output.append(f"{romaji_lyric}<{duration},{vocal_tone}>")

        # Update previous_end_position
        previous_end_position = position + duration
    
    # Write to tone.txt
    with open("tone.txt", "w") as tone_file:
        tone_file.write(f"[{' '.join(tones_output)}]\n")

    # Write to vocal.txt
    with open("vocal.txt", "w") as vocal_file:
        vocal_file.write(f"[{' '.join(vocal_output)}]\n")

    print("Conversion complete. Files 'tone.txt' and 'vocal.txt' have been created.")
    subprocess.run(['python', 'vocalfix.py'])

# Main
if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python conv.py <ustx_file_path>")
        sys.exit(1)
    
    file_path = sys.argv[1]
    convert_ustx_to_dectalk(file_path)
