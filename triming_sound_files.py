from pydub import AudioSegment
from pydub.silence import split_on_silence

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

# Example usage:
input_file = "/Users/ashoktimsina/Desktop/gesture_durm/sounds/Bass-Drum-Hit-Level-6c-.mp3"
output_file = "/Users/ashoktimsina/Desktop/gesture_durm/sounds/Bass-Drum-Hit-Level-6c-mod.mp3"
min_silence_len = 100  # Minimum silence duration in milliseconds
silence_threshold = -30  # Silence threshold in dB

## this needs to be modeified to cover all sound files
# Call the remove_silence() function with the specified parameterss
remove_silence(input_file, output_file, min_silence_len, silence_threshold)
