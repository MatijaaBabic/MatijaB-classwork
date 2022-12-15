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
size = 10
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
DBLUE = (5, 66, 119)
PINKISH = (233, 112, 193)



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
        self.lader = T.ladder
        self.snek = T.snakes
        self.color = color
        self.size = random.randint(50, 70)
        for x in self.tile:                   #code to spawn the object at the starting position 1
            for y in x:
                if self.val == y[2]:
                    a = y
                    self.posx = y[0]
                    self.posy = y[1]
    
    def move(self, e):          #function for movement
        if (self.val - e) > 0:
            self.val = self.val + e
        else:
            print("N o.")   #just a fun little thing to show, as it wont appear in the actual window, just in the run bar
        if self.val == 100:          #winning condition
            print("You win :D")
            global WIN	 #variable which will tell the program when to present the winning screen
            WIN = True
        for x in self.tile:            #so we move by checking values of the places that we are at
            for y in x:
                if self.val == y[2]:
                    a = y
                    self.posx = y[0]
                    self.posy = y[1]
        
        for i in self.lader:             #code to actually use the ladders and snakes
            if (self.posx == i[0][0] and self.posy == i[0][1]) or (self.posx == i[1][0] and self.posy == i[1][1]):            #check to see if the coordinates of the player corelate with the beginning coordinates of the ladders by using the coordinates in the ladders list
                if self.val == min(i[0][2], i[1][2]):                      #we make the value of the player the value of the top of the ladder if the player is at the bottom
                    self.val = max(i[0][2], i[1][2])
                    for x in self.tile:
                        for y in x:                                                             #we change the value of the player to the value of the top, and then move the player to that value
                            if self.val == y[2]:
                                a = y
                                self.posx = y[0]
                                self.posy = y[1]
                else:
                    pass
        
        #you can do the same thing with the snakes, which is what I did, just inverted the max and min functions for the self.value
        for j in self.snek:             #code to actually use the ladders and snakes
            if (self.posx == j[0][0] and self.posy == j[0][1]) or (self.posx == j[1][0] and self.posy == j[1][1]):            #check to see if the coordinates of the player corelate with the end coordinate of the snake through the list (same process as the ladder function)
                if self.val == max(j[0][2], j[1][2]):                      #we make the value of the player the value of the tail of the snake if the player is at it's head
                    self.val = min(j[0][2], j[1][2])
                    for x in self.tile:
                        for y in x:                                                             #we change the value of the player to the value of the bottom, and then move the player to that value
                            if self.val == y[2]:
                                a = y
                                self.posx = y[0]
                                self.posy = y[1]
                else:
                    pass
    def draw(self, playerNum):
        if playerNum == 1:
            pygame.draw.circle(screen,(self.color),(self.posx+60,self.posy+40),self.size)
        elif playerNum == 2:
            pygame.draw.rect(screen,(self.color),(self.posx+60,self.posy+40),self.size)

#the pain of writing 2 dice codes :(((((
def dice1one():
	x,y,w,h = 1605,100,80,80
	pygame.draw.rect(screen, DBLUE ,(x,y,w,h))
	pygame.draw.circle(screen, PINKISH ,((x+(w//2)), (y+(h//2))), size)

def dice2one():
	x,y,w,h = 1705,100,80,80
	pygame.draw.rect(screen, DBLUE ,(x,y,w,h))
	pygame.draw.circle(screen, PINKISH ,((x+(w//2)), (y+(h//2))), size)

def dice1two():
	x,y,w,h = 1605,100,80,80
	pygame.draw.rect(screen, DBLUE ,(x,y,w,h))
	pygame.draw.circle(screen, PINKISH ,((x+(w//4)), (y+(h//2))),size)
	pygame.draw.circle(screen, PINKISH ,((x+(3*w//4)), (y+(h//2))),size)

def dice2two():
	x,y,w,h = 1705,100,80,80
	pygame.draw.rect(screen, DBLUE ,(x,y,w,h))
	pygame.draw.circle(screen, PINKISH ,((x+(w//4)), (y+(h//2))),size)
	pygame.draw.circle(screen, PINKISH ,((x+(3*w//4)), (y+(h//2))),size)

def dice1three():
	x,y,w,h = 1605,100,80,80
	pygame.draw.rect(screen, DBLUE ,(x,y,w,h))
	pygame.draw.circle(screen, PINKISH ,((x+(w//4)), (y+(3*h//4))),size)
	pygame.draw.circle(screen, PINKISH ,((x+(w//2)), (y+(h//2))),size)
	pygame.draw.circle(screen, PINKISH ,((x+(3*w//4)), (y+(h//4))),size)

def dice2three():
	x,y,w,h = 1705,100,80,80
	pygame.draw.rect(screen, DBLUE ,(x,y,w,h))
	pygame.draw.circle(screen, PINKISH ,((x+(w//4)), (y+(3*h//4))),size)
	pygame.draw.circle(screen, PINKISH ,((x+(w//2)), (y+(h//2))),size)
	pygame.draw.circle(screen, PINKISH ,((x+(3*w//4)), (y+(h//4))),size)

def dice1four():
    x,y,w,h = 1605,100,80,80
    pygame.draw.rect(screen, DBLUE ,(x,y,w,h))
    pygame.draw.circle(screen, PINKISH ,((x+(w//4)), (y+(h//4))),size)
    pygame.draw.circle(screen, PINKISH ,((x+(w//4)), (y+(3*h//4))),size)
    pygame.draw.circle(screen, PINKISH,((x+(3*w//4)), (y+(h//4))),size)
    pygame.draw.circle(screen, PINKISH ,((x+(3*w//4)), (y+(3*h//4))),size)

def dice2four():
    x,y,w,h = 1705,100,80,80
    pygame.draw.rect(screen, DBLUE ,(x,y,w,h))
    pygame.draw.circle(screen, PINKISH ,((x+(w//4)), (y+(h//4))),size)
    pygame.draw.circle(screen, PINKISH ,((x+(w//4)), (y+(3*h//4))),size)
    pygame.draw.circle(screen, PINKISH,((x+(3*w//4)), (y+(h//4))),size)
    pygame.draw.circle(screen, PINKISH ,((x+(3*w//4)), (y+(3*h//4))),size)

def dice1five():
    x,y,w,h = 1605,100,80,80
    pygame.draw.rect(screen, DBLUE ,(x,y,w,h))
    pygame.draw.circle(screen, PINKISH ,((x+(w//2)), (y+(h//2))),size)
    pygame.draw.circle(screen, PINKISH ,((x+(w//4)), (y+(h//4))),size)
    pygame.draw.circle(screen, PINKISH ,((x+(w//4)), (y+(3*h//4))),size)
    pygame.draw.circle(screen, PINKISH ,((x+(3*w//4)), (y+(h//4))),size)
    pygame.draw.circle(screen, PINKISH ,((x+(3*w//4)), (y+(3*h//4))),size)

def dice2five():
    x,y,w,h = 1705,100,80,80
    pygame.draw.rect(screen, DBLUE ,(x,y,w,h))
    pygame.draw.circle(screen, PINKISH ,((x+(w//2)), (y+(h//2))),size)
    pygame.draw.circle(screen, PINKISH ,((x+(w//4)), (y+(h//4))),size)
    pygame.draw.circle(screen, PINKISH ,((x+(w//4)), (y+(3*h//4))),size)
    pygame.draw.circle(screen, PINKISH ,((x+(3*w//4)), (y+(h//4))),size)
    pygame.draw.circle(screen, PINKISH ,((x+(3*w//4)), (y+(3*h//4))),size)

def dice1six():
    x,y,w,h = 1605,100,80,80
    pygame.draw.rect(screen, DBLUE ,(x,y,w,h))
    pygame.draw.circle(screen, PINKISH ,((x+(w//4)), (y+(h//2))),size)
    pygame.draw.circle(screen, PINKISH ,((x+(3*w//4)), (y+(h//2))),size)
    pygame.draw.circle(screen, PINKISH ,((x+(w//4)), (y+(h//4))-10),size)
    pygame.draw.circle(screen, PINKISH ,((x+(w//4)), (y+(3*h//4))+10),size)
    pygame.draw.circle(screen, PINKISH ,((x+(3*w//4)), (y+(h//4))-10),size)
    pygame.draw.circle(screen, PINKISH ,((x+(3*w//4)), (y+(3*h//4))+10),size)

def dice2six():
    x,y,w,h = 1705,100,80,80
    pygame.draw.rect(screen, DBLUE ,(x,y,w,h))
    pygame.draw.circle(screen, PINKISH ,((x+(w//4)), (y+(h//2))),size)
    pygame.draw.circle(screen, PINKISH ,((x+(3*w//4)), (y+(h//2))),size)
    pygame.draw.circle(screen, PINKISH ,((x+(w//4)), (y+(h//4))-10),size)
    pygame.draw.circle(screen, PINKISH ,((x+(w//4)), (y+(3*h//4))+10),size)
    pygame.draw.circle(screen, PINKISH ,((x+(3*w//4)), (y+(h//4))-10),size)
    pygame.draw.circle(screen, PINKISH ,((x+(3*w//4)), (y+(3*h//4))+10),size)

#need to make the win function, probably just a line saying which player won and resseting the players, and the actual code to run the game