import PySimpleGUI as sg
import pygame
pygame.init()
songs = ['rick_astley.mp3', 'baby-shark.mp3']
music = 'rick_astley.mp3'
pygame.mixer.music.load(music)
x = 0
layout = [
    [sg.Button(image_filename='back_button.png', size=(50,50), auto_size_button=True, key='back'),
        sg.Button(image_filename='play_button.png', size=(50,50), auto_size_button=True, key='play/pause', visible=True),
        sg.Button(image_filename='forward_button.png', size=(50,50), auto_size_button=True, key='forward')]
]
window = sg.Window('title', layout)
pygame.mixer.music.play()
pygame.mixer.music.pause()
def play(x):
    music = songs[x]
    pygame.mixer.music.load(music)
    pygame.mixer.music.play()
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break
    elif event == 'play/pause':
        if pygame.mixer.music.get_busy() == True:
            pygame.mixer.music.pause()
            window.Element('play/pause').Update(image_filename='play_button.png')
        else:
            pygame.mixer.music.unpause()
            window.Element('play/pause').Update(image_filename='pause_button.png')
    elif event == 'forward':
        pygame.mixer.music.unload()
        if x == len(songs)-1:
            x = 0
        else:
            x = x+1
        play(x)
    elif event == 'back':
        pygame.mixer.music.unload()
        if x == 1:
            x = len(songs)-1
        else:
            x = x-1
        play(x)
window.close()