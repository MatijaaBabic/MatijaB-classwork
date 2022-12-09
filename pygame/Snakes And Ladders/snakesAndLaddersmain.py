import os
import pygame
import pygame_menu
import random
import math
os.chdir(r'C:\Users\Windows 10\Desktop\Microsoft\Prezentacije\Programs for school\Code\Github\MatijaB-classwork\pygame\Snakes And Ladders')
info = pygame.display.Info()
SIZE = W, H = info.current_w, info.current_h
screen = pygame.display.set_mode(SIZE)
clock = pygame.time.Clock()
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (115, 181, 239)
YELLOW = (234, 226, 61)
LIGHTBLUE = (129, 185, 234)
LIGHTYELLOW = (241, 239, 143)
LIGHTRED = (241, 158, 143)
LIGHTGREEN = (143, 241, 143)
LIGHTPURPLE = (211, 121, 199)



class Tile(pygame.sprite.Sprite):                #board class
    def __init__(self):
        super().__init__()
        self.tilelist = []                    #list for the board                    #code to initialize the board, by using a list
        num = 100
        for i in range(0,10):
            temp = []
            for j in range(0,10):
                x = j*160
                y = i*108
                temp.append((x, y, num))                 #it takes the values of x and y with the distances provided to fit the screen, with enough space on side, and uses the num variable to count down from 100 to 1
                num = num - 1
            self.tilelist.append(temp)
        
        #ladder code
        self.ladder = []                #creating ladders, by having a list containing their x and y coordinates
        self.counter = [1, 100]
        numlad = random.randint(4, 6)       #4 to 6 ladders per game, randomly chosen
        for i in range(numlad):
            check = True
            while check == True:
                randx = random.randint(1,100)
                randy = random.randint(1,100)
                delta = randx - randy
                if delta > 10 or delta < -10:
                    if randx not in self.counter and randy not in self.counter:
                        check = False
                        self.counter.append(randx)
                        self.counter.append(randy)
            a = None     #this code serves to get the values of the coordinates for tiles, and if the coordinates align it places the coordinate of the ladder there
            b = None
            for x in self.tilelist:
                for y in x:
                    if randx == y[2]:               #we check if the random x value is equal to any of the values in the original list, and if it does it places the x value there, 
                        a = y
                    if randy == y[2]:              #this does the same thing for the y values
                        b = y
            self.ladder.append((a,b))           #appending those values to the ladder list

            #creating dem snaikies
            self.snakes = []
            numsnek = random.randint(4,6)
            for i in range(numsnek):
                check1 = True
                while check1 == True:
                    randx = random.randint(1, 100)
                    randy = random.randint(1, 100)
                    delta1 = randx - randy
                    if delta1 > 10 or delta1 < -10:
                        if randx not in self.counter and randy not in self.counter:
                            check1 = False
                            self.counter.append(randx)
                            self.counter.append(randy)
            c = None
            d = None
            for x in self.tilelist:
                for y in x:
                    if randx == y[2]:
                        c = y
                    if randy == y[2]:
                        d = y
            self.snakes.append((c,d))
    
    def drawing(self):           
        for i in self.tilelist:                  #going through the list to get the values to draw the rectangles
            for j in i:
                randomcolor = random.randint(0, 5)          #random color picker
                if randomcolor == 0:
                    color = LIGHTBLUE
                elif randomcolor == 1:
                    color = LIGHTYELLOW
                elif randomcolor == 2:
                    color = LIGHTGREEN
                elif randomcolor == 3:
                    color = LIGHTPURPLE
                elif randomcolor == 4:
                    color = LIGHTRED
                
                #rectangle drawing code
                pygame.draw.rect(screen, (color), (j[0], j[1], 159, 107))
                tinytext = pygame.font.Font("papyrus",20)
                textSurf = tinytext.render(str(j[2]), True, BLACK)
                screen.blit(textSurf, ((j[0]+30), (j[1]+30)))
        #code for drawing the ladders and snakes
        for x in self.ladder:
            pygame.draw.line(screen, (RED) , (x[0][0]+53,x[0][1]+56),(x[1][0]+53,x[1][1]+56),3)
            pygame.draw.line(screen, (RED) , (x[0][0]+106,x[0][1]+56),(x[1][0]+106,x[1][1]+56),3)
        for x in self.snakes:
            pygame.draw.line(screen, (GREEN) , (x[0][0]+80,x[0][1]+56),(x[1][0]+80,x[1][1]+56),8)

#player class
class player(pygame.sprite.Sprite):
    def __init__(self, T, color):
        self.val = 1
        self.posx = None
        self.posy = None
        self.tile = T.tilelist
        self.lad = T.ladder
        self.snk = T.snakes
        self.color = color

                


                
                



