#!/usr/bin/env python3

import sys
from pydub import AudioSegment

def extract_one_second(audio_file, output_file):
    """
    Extracts the first second from an audio file.

    Args:
    audio_file (str): Path to the input audio file.
    output_file (str): Path to save the extracted audio.
    """
    audio = AudioSegment.from_file(audio_file)
    audio_after_one_second = audio[1000:]
    audio_after_one_second.export(output_file, format='mp3')

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python extract_one_second.py [input_file] [output_file]")
        sys.exit(1)

    input_file = sys.argv[1]
    output_file = input_file + "_cutted"
    extract_one_second(input_file, output_file)
