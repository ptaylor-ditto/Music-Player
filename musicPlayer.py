import PySimpleGUI as sg
import pygame, os
pygame.init()
songs = ['baby-shark.mp3', 'rick_astley.mp3', 'NyanCat.mp3', 'CantinaSong.mp3']
os.system('cls')
x = 0
pathSep = os.path.sep
fullPathToMusicFile = pathSep.join([os.getcwd(), songs[x]])
pygame.mixer.music.load(fullPathToMusicFile)
layout = [
    [sg.Text('Volume  '), sg.Slider(range=(0,100), orientation='h', size=(60,10), key=('volume'))],
    [sg.Button(image_filename='back_ten.png', size=(20,20), key='back_ten'),
        sg.Button(image_filename='forward_ten.png', size=(20,20), key='forward_ten')
    ],
        [sg.Button(image_filename='back_button.png', size=(40,40), key='back'),
        sg.Button(image_filename='play_button.png', size=(40,40), key='play/pause', visible=True),
        sg.Button(image_filename='forward_button.png', size=(40,40), key='forward')
        ]
]
window = sg.Window('Music Player', layout)
pygame.mixer.music.play()
pygame.mixer.music.pause()
def play(x):
    music = songs[x]
    pygame.mixer.music.load(music)
    pygame.mixer.music.play()
while True:
    event, values = window.read()
    length = pygame.mixer.music.get_pos()
    pygame.mixer.music.set_volume(values['volume']/100)
    if event == sg.WIN_CLOSED:
        break
    if event == 'back_ten':
        length = pygame.mixer.music.get_pos()
        pygame.mixer.music.set_pos(length-10)
    if event == 'forward_ten':
        length = pygame.mixer.music.get_pos()
        pygame.mixer.music.set_pos(length+10)
    if event == 'play/pause':
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
