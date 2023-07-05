# The sound used are downloaded from fesliyan studios and the audio files had few seconds of silence that was to be removed.
# This scirpts removes that silence and stores the sound present in the audio file.

from pydub import AudioSegment
from pydub.silence import split_on_silence

import os

def remove_silence(input_file, output_file, min_silence_len, silence_threshold):
    # Load the audio file
    audio = AudioSegment.from_file(input_file)

    # Split the audio based on silence
    chunks = split_on_silence(audio, min_silence_len=min_silence_len, silence_thresh=silence_threshold)

    # Combine the non-silent chunks
    combined_audio = AudioSegment.empty()
    for chunk in chunks:
        combined_audio += chunk

    # Export the combined audio to a new file
    combined_audio.export(output_file, format="mp3")

sound_folder = "sounds"

min_silence_len = 100  # Minimum silence duration in milliseconds
silence_threshold = -30  # Silence threshold in dB

for filename in os.listdir(sound_folder): 
    # checking if the filename is a file or subfolder
    if os.path.isfile(os.path.join(sound_folder, filename)) and filename != '.DS_Store':
        old_filename = 'sounds/' + filename
        new_filename = 'sounds/mod_' + filename
        

        print(filename)
        print(old_filename)
        print(new_filename)
        remove_silence(old_filename, new_filename, min_silence_len, silence_threshold)


# # Example usage:
# input_file = "/Users/ashoktimsina/Desktop/gesture_durm/sounds/Bass-Drum-Hit-Level-6c-.mp3"
# output_file = "/Users/ashoktimsina/Desktop/gesture_durm/sounds/Bass-Drum-Hit-Level-6c-mod.mp3"


# ## this needs to be modeified to cover all sound files
# # Call the remove_silence() function with the specified parameterss
# remove_silence(input_file, output_file, min_silence_len, silence_threshold)
