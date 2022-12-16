import os
import pygame
import pygame_menu
import random
import math
from pygame import mixer
import sys
os.chdir(r'C:\Users\Windows 10\Desktop\Microsoft\Prezentacije\Programs for school\Code\Github\MatijaB-classwork\pygame\Snakes And Ladders')
clock = pygame.time.Clock()
size = 10 
playsound = True
WIN = False
MENU = True
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
GRAY = (109, 112, 114)



class Tile(pygame.sprite.Sprite):                #board class
    def __init__(self):
        super().__init__()
        self.color = LIGHTBLUE
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
        self.counter = [100, 1]                      
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
                check = True
                while check == True:
                    randx = random.randint(1, 100)
                    randy = random.randint(1, 100)
                    delta = randx - randy
                    if delta > 10 or delta < -10:
                        if randx not in self.counter and randy not in self.counter:
                            check = False
                            self.counter.append(randx)
                            self.counter.append(randy)
                a = None
                b = None
                for x in self.tilelist:
                    for y in x:
                        if randx == y[2]:
                            a = y
                        if randy == y[2]:
                            b = y
                self.snakes.append([a,b])
    
    def drawing(self):           
        for i in self.tilelist:                  #going through the list to get the values to draw the rectangles
            for j in i:
                randomcolor = random.randint(0, 5)          #random color picker
                if randomcolor == 0:
                    self.color = LIGHTBLUE
                elif randomcolor == 1:
                    self.color = LIGHTYELLOW
                elif randomcolor == 2:
                    self.color = LIGHTGREEN
                elif randomcolor == 3:
                    self.color = LIGHTPURPLE
                elif randomcolor == 4:
                    self.color = LIGHTRED
                
                #rectangle drawing code
                pygame.draw.rect(screen, self.color, (j[0], j[1], 159, 107))
                tinytext = pygame.font.Font("papyrus.TTF",20)
                textSurf = tinytext.render(str(j[2]), True, BLACK)
                screen.blit(textSurf, ((j[0]+30), (j[1]+30)))
        #code for drawing the ladders and snakes
        for x in self.ladder:
            pygame.draw.line(screen, (RED) , (x[0][0]+53,x[0][1]+56),(x[1][0]+53,x[1][1]+56),3)
            pygame.draw.line(screen, (RED) , (x[0][0]+106,x[0][1]+56),(x[1][0]+106,x[1][1]+56),3)
        for x in self.snakes:
            pygame.draw.line(screen, (GREEN) , (x[0][0]+80,x[0][1]+56),(x[1][0]+80,x[1][1]+56),8)

#player class
class Player(pygame.sprite.Sprite):
    def __init__(self, T, color):
        self.val = 1
        self.posx = None
        self.posy = None
        self.tile = T.tilelist
        self.lader = T.ladder
        self.snek = T.snakes
        self.color = color
        self.radius = 50
        self.size = 80
        for x in self.tile:                   #code to spawn the object at the starting position 1
            for y in x:
                if self.val == y[2]:
                    a = y
                    self.posx = y[0]
                    self.posy = y[1]
    
    def move(self, e):          #function for movement
        if (self.val + e) > 0:
            self.val += e
        else:
            print("N o.")   #just a fun little thing to show, as it wont appear in the actual window, just in the run bar
        if self.val >= 100 and self.val <107:          #winning condition
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
            pygame.draw.circle(screen, self.color,(self.posx+60,self.posy+40), self.radius)
        elif playerNum == 2:
            pygame.draw.rect(screen, self.color,[self.posx,self.posy,80,80], 0)

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

def win():
    global playsound
    if player1.val == 100:
        win_text = semitinytext.render("Player 1 wins!", True, BLACK)
        screen.blit(win_text, (1605, 800))
    elif player2.val == 100:
        win_text = semitinytext.render("Player 2 wins!", True, BLACK)
        screen.blit(win_text, (1605, 800))
    if playsound:
        win1.play()
        playsound = False
    player1.val = 1
    player2.val = 1
    for x in player1.tile:            #so we move by checking values of the places that we are at
            for y in x:
                if player1.val == y[2]:
                    a = y
                    player1.posx = y[0]
                    player1.posy = y[1]
    for x in player2.tile:            #so we move by checking values of the places that we are at
            for y in x:
                if player2.val == y[2]:
                    a = y
                    player2.posx = y[0]
                    player2.posy = y[1]
    player1.draw(1)
    player2.draw(2)

pygame.init()
info = pygame.display.Info()
SIZE = W, H = info.current_w, info.current_h
screen = pygame.display.set_mode(SIZE)
semitinytext = pygame.font.Font("papyrus.TTF",25)
board = Tile()
player1 = Player(board, BLUE)
player2 = Player(board, RED)
win1 = pygame.mixer.Sound("win.wav")
screen.fill(GRAY)
whoseturnitis = semitinytext.render("TURN:", True, BLACK)
screen.blit(whoseturnitis, (1650, 250))
howtoplay = semitinytext.render("Press SPACE to", True, BLACK)
screen.blit(howtoplay, (1610, 950))
howtoplay1 = semitinytext.render("throw the dice", True, BLACK)
screen.blit(howtoplay1, (1610, 1000))
mixer.music.load("stillalive.wav")
mixer.music.play(-1)
turn = 1
done = False
roll = False
board.drawing()
while not done:
    #if MENU == True:
        #code for the menu
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                if roll == True:
                    roll = False
                else:
                    roll = True
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()
            if event.key == pygame.K_TAB:
                MENU = False

    if not WIN:         #later add the condition for menu as well
        player1.draw(1)
        player2.draw(2)
        if turn == 1:
            pygame.draw.circle(screen, player1.color, (1700, 400),50)
        elif turn == 2:
            pygame.draw.circle(screen, player2.color, (1700, 400),50)
        if roll == True:
            timeinterval = random.randint(5, 20)
            for i in range(timeinterval):
                no = random.randint(1, 6)
                yes = random.randint(1, 6)
                if no == 1 and yes == 1:
                    dice1one()
                    dice2one()
                elif no == 1 and yes == 2:
                    dice1one()
                    dice2two()
                elif no == 1 and yes == 3:
                    dice1one()
                    dice2three()
                elif no == 1 and yes == 4:
                    dice1one()
                    dice2four()
                elif no == 1 and yes == 5:
                    dice1one()
                    dice2five()
                elif no == 1 and yes == 6:
                    dice1one()
                    dice2six()
                elif no == 2 and yes == 1:
                    dice1two()
                    dice2one()
                elif no == 2 and yes == 2:
                    dice1two()
                    dice2two()
                elif no == 2 and yes == 3:
                    dice1two()
                    dice2three()
                elif no == 2 and yes == 4:
                    dice1two()
                    dice2four()
                elif no == 2 and yes == 5:
                    dice1two()
                    dice2five()
                elif no == 2 and yes == 6:
                    dice1two()
                    dice2six()
                elif no == 3 and yes == 1:
                    dice1three()
                    dice2one()
                elif no == 3 and yes == 2:
                    dice1three()
                    dice2two()
                elif no == 3 and yes == 3:
                    dice1three()
                    dice2three()
                elif no == 3 and yes == 4:
                    dice1three()
                    dice2four()
                elif no == 3 and yes == 5:
                    dice1three()
                    dice2five()
                elif no == 3 and yes == 6:
                    dice1three()
                    dice2six()
                elif no == 4 and yes == 1:
                    dice1four()
                    dice2one()
                elif no == 4 and yes == 2:
                    dice1four()
                    dice2two()
                elif no == 4 and yes == 3:
                    dice1four()
                    dice2three()
                elif no == 4 and yes == 4:
                    dice1four()
                    dice2four()
                elif no == 4 and yes == 5:
                    dice1four()
                    dice2five()
                elif no == 4 and yes == 6:
                    dice1four()
                    dice2six()
                elif no == 5 and yes == 1:
                    dice1five()
                    dice2one()
                elif no == 5 and yes == 2:
                    dice1five()
                    dice2two()
                elif no == 5 and yes == 3:
                    dice1five()
                    dice2three()
                elif no == 5 and yes == 4:
                    dice1five()
                    dice2four()
                elif no == 5 and yes == 5:
                    dice1five()
                    dice2five()
                elif no == 5 and yes == 6:
                    dice1five()
                    dice2six()
                elif no == 6 and yes == 1:
                    dice1six()
                    dice2one()
                elif no == 6 and yes == 2:
                    dice1six()
                    dice2two()
                elif no == 6 and yes == 3:
                    dice1six()
                    dice2three()
                elif no == 6 and yes == 4:
                    dice1six()
                    dice2four()
                elif no == 6 and yes == 5:
                    dice1six()
                    dice2five()
                elif no == 6 and yes == 6:
                    dice1six()
                    dice2six()
                pygame.time.wait(150)
                pygame.display.update()
            sum = no + yes
            roll = False
            if turn == 1:
                
                player1.move(sum)
                turn = 2
                pygame.draw.circle(screen, player2.color, (1700, 400),50)
            elif turn == 2:
                
                player2.move(sum)
                turn = 1
                pygame.draw.circle(screen, player1.color, (1700, 400),50)
    else:
        win()
    pygame.display.update()
    clock.tick(60)
pygame.quit()
quit()