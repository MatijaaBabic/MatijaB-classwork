import os
import pygame
import pygame_menu
import random
os.chdir(r'C:\Users\Windows 10\Desktop\Microsoft\Prezentacije\Programs for school\Code\Github\MatijaB-classwork\pygame\Snakes And Ladders')
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (115, 181, 239)
YELLOW = (234, 226, 61)
class Tile(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.tilelist = []
        num = 100
    def create(self):
        for i in range(0,10):
            temp = []
            for j in range(0,10):
                x = j*160
                y = i*108
                temp.append((x, y, num))
                num = num - 1
            self.tilelist.append(temp)
        
        #ladder code
        self.ladder = []
        self.counter = [1, 100]
        numlad = random.randint(2, 8)
        for i in range(numlad):
            check = True
            while check == True:
                randx = random.randint(0,100)
                randy = random.randint(0,100)
                delta = randx - randy
                if delta > 10 or delta < -10:
                    if randx not in self.counter and randy not in self.counter:
                        check = False
                        self.counter.append(randx)
                        self.counter.append(randy)
            


                
                



