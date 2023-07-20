## This scirpt attempts to implement assyncronous sound play.

import asyncio
from pydub import AudioSegment
from pydub.playback import play

base_dir = '/Users/ashoktimsina/Desktop/gesture_durm/'

bass = base_dir + 'sounds/mod_Bass-Drum-Hit-Level-6c-.mp3'
drum = base_dir + 'sounds/mod_Drum-Sticks-Hit-A-.mp3'
floor = base_dir + 'sounds/mod_Floor-Tom-Drum-Hit-Level-6B-.mp3'
hi_hat = base_dir + 'sounds/mod_Hi-Hat-Closed-Hit-B1-.mp3'
snare = base_dir + 'sounds/mod_Snare-Drum-Hit-Level-1a-.mp3'

async def play_music(file_path):
    audio = AudioSegment.from_file(file_path)
    play(audio)

async def main():
    # List of audio files to play asynchronously
    audio_files = [bass, drum, floor, hi_hat, snare]

    # Create a list of coroutines for each audio file
    coroutines = [play_music(file_path) for file_path in audio_files]

    # Run the coroutines concurrently
    await asyncio.gather(*coroutines)

if __name__ == "__main__":
    asyncio.run(main())