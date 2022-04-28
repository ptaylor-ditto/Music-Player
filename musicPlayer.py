import PySimpleGUI as sg
import pygame, os, audio_metadata
from random import randint
pygame.init()
songs = ['baby-shark.mp3', 'rick_astley.mp3', 'NyanCat.mp3', 'CantinaSong.mp3']
os.system('cls')
x = 0
pathSep = os.path.sep
fullPathToMusicFile = pathSep.join([os.getcwd(), songs[x]])
pygame.mixer.music.load(fullPathToMusicFile)
layout = [
    [sg.Text('Volume  '), sg.Slider(range=(0,100), orientation='h', size=(60,10), key=('volume'))],
    [sg.Text('Song Progress'), sg.Slider(range=(0,0), orientation='h', key='song')],
        [sg.Button(image_filename='back_button.png', size=(40,40), auto_size_button=True, key='back'),
        sg.Button(image_filename='play_button.png', size=(40,40), auto_size_button=True, key='play/pause', visible=True),
        sg.Button(image_filename='forward_button.png', size=(40,40), auto_size_button=True, key='forward')
        ]
]
window = sg.Window('Music Player', layout)
pygame.mixer.music.play()
pygame.mixer.music.pause()
def play(x):
    music = songs[x]
    pygame.mixer.music.load(music)
    pygame.mixer.music.play()
length = audio_metadata.load(fullPathToMusicFile)
while True:
    event, values = window.read()
    length = pygame.mixer.music.get_pos()
    print(length)
    pygame.mixer.music.set_volume(values['volume']/100)
    pygame.mixer.music.set_pos(values['song'])
    if event == sg.WIN_CLOSED:
        break
    if event == 'play/pause':
        length = audio_metadata.load(songs[x])
        window.Element('song').Update(range=(0,length))
        if pygame.mixer.music.get_busy() == True:
            pygame.mixer.music.pause()
            window.Element('play/pause').Update(image_filename='play_button.png')
        else:
            pygame.mixer.music.unpause()
            window.Element('play/pause').Update(image_filename='pause_button.png')
    if event == 'forward':
        pygame.mixer.music.unload()
        if x == len(songs)-1:
            x = 0
        else:
            x = x+1
        play(x)
    if event == 'back':
        pygame.mixer.music.unload()
        if x == 0:
            x = len(songs)-1
        else:
            x = x-1
        play(x)
window.close()
