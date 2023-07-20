# This script is to test whether the sound files and playsound library are working fine or not

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



# main loop
while True:
    
    #getting user choice
    #try:
    num = input(prompt)

    num = int(num)
    # except:
    #     print('Your were supposed to enter a number.')
    #     continue
    
    if (num == 1):
        play_sound(bass)
        print('played')

    if num == 2:
        play_sound(drum)

    if num == 3:
        play_sound(floor)    

    if num == 4:
        play_sound(hi_hat)
    
    if num == 5:
        play_sound(snare)


## this is just test code


