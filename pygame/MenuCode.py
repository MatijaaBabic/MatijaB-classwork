import pygame
import sys
import pygame_menu
import random
info = pygame.display.Info()
W, H = info.current_w, info.current_h
def set_difficulty(value, difficulty):
    if difficulty == "easy":
        
    pass

def start_the_game():
    # Do the job here !
    pass
menu = pygame_menu.Menu(
    height=H,
    theme=pygame_menu.themes.THEME_BLACK,
    title='Pong: The Game',
    width=W
)
menu.add.selector('Difficulty: ', [("Quitting speedrun any% world record", 1), ("Nightmare", 2), ('Hurt me plenty', 3), ("I ain't no baby", 4), ('Please dont hurt me :(', 5), ("Baby mode", 6)], onchange=set_difficulty)
menu.add.button('Play', start_the_game)
menu.add.button('Quit', pygame_menu.events.EXIT)