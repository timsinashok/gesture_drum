from playsound import playsound

def play_sound(file_path):
    playsound(file_path)

# file paths
bass = '/Users/ashoktimsina/Desktop/gesture_durm/sounds/Bass-Drum-Hit-Level-6c-.mp3'
drum = '/sounds/Bass-Drum-Hit-Level-6c-.mp3'
floor = '/sounds/Bass-Drum-Hit-Level-6c-.mp3'
hi_hat = '/sounds/Bass-Drum-Hit-Level-6c-.mp3'
snare = '/sounds/Bass-Drum-Hit-Level-6c-.mp3'

prompt = "Enter a number: "

play_sound(bass)

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