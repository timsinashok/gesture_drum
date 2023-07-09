# This script does not wait for user to enter number to play sound. 

from playsound import playsound

def play_sound(file_path):
    playsound(file_path)

# file paths
bass = 'sounds/mod_Bass-Drum-Hit-Level-6c-.mp3'
drum = 'sounds/mod_Drum-Sticks-Hit-A-.mp3'
floor = 'sounds/mod_Floor-Tom-Drum-Hit-Level-6B-.mp3'
hi_hat = 'sounds/mod_Hi-Hat-Closed-Hit-B1-.mp3'
snare = 'sounds/mod_Snare-Drum-Hit-Level-1a-.mp3'

prompt = "Enter a number: "

num = input(prompt)

num = int(num)

# Convert number to a string and split it into individual characters
digit_list = list(str(num))

# Convert each character back to an integer
digit_list = [int(digit) for digit in digit_list]

print(digit_list)

for digit in digit_list:
    if (digit == 1):
        play_sound(bass)
        print('played')

    if digit == 2:
        play_sound(drum)

    if digit == 3:
        play_sound(floor)    

    if digit == 4:
        play_sound(hi_hat)
    
    if digit == 5:
        play_sound(snare)


