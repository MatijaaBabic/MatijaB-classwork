"""
 Pygame base template for opening a window
 
 Sample Python/Pygame Programs
 Simpson College Computer Science
 http://programarcadegames.com/
 http://simpson.edu/computer-science/
 
 Explanation video: http://youtu.be/vRB_983kUMc
"""
 
import pygame
import sys

 
# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (115, 181, 239)
YELLOW = (234, 226, 61)
x = 960
y = 590
xoffset = 7
yoffset = 7
y_speed = 0
y_speed2 = 0
x_coord1 = 0
y_coord1 = 500
x_coord2 = 1905
y_coord2 = 500
collide = 0
score1 = 0
score2 = 0

pygame.init()
info = pygame.display.Info()
SIZE = W, H = info.current_w, info.current_h
screen = pygame.display.set_mode(SIZE)
click_sound1 = pygame.mixer.Sound("pongwall.wav")
click_sound2 = pygame.mixer.Sound("pongleftpaddle.ogg")
click_sound3 = pygame.mixer.Sound("pongrightpaddle.ogg")
click_sound4 = pygame.mixer.Sound("pointwin.wav")
# Set the width and height of the screen [width, height]
#size = (700, 500)
#screen = pygame.display.set_mode(size)
pygame.display.set_caption('Ping Pong') 
# Loop until the user clicks the close button.
done = False
 
# Used to manage how fast the screen updates
clock = pygame.time.Clock()
 
# -------- Main Program Loop -----------
while not done:
    # --- Main event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True    
    # --- Game logic should go here
        #This is code for the rectangle to move up or down depending on the key pressed
        elif event.type == pygame.KEYDOWN:     #we can use while if we want it to move for as long as the key is presed
            if event.key == pygame.K_UP:
                y_speed = -7
            elif event.key == pygame.K_DOWN:
                y_speed = 7
            elif event.key == pygame.K_w:
                y_speed2 = -7
            elif event.key == pygame.K_s:
                y_speed2 = 7
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
        #code to make the rectangle actually move (so y_coord1 will have y_speed added to it and then the value is assigned back to y_coord1)
        #This is the code for when the key isn't pressed        
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                y_speed = 0
            elif event.key == pygame.K_w or event.key == pygame.K_s:    
                y_speed2 = 0             
    # --- Screen-clearing code goes here
 
    # Here, we clear the screen to white. Don't put other drawing commands
    # above this, or they will be erased with this command.
 
    # If you want a background image, replace this clear with blit'ing the
    # background image.
    screen.fill(BLACK)
    y_coord1 += y_speed  #code to make the rectangle actually move (so y_coord1 will have y_speed added to it and then the value is assigned back to y_coord1)
    y_coord2 += y_speed2
    if x < 1 or x > 1900:
        x = 960
        y = 590
        y_coord1 = 500
        y_coord2 = 500
        click_sound4.play()
    if ((x == x_coord1 + 15) and ((y < (y_coord1 + 150 + 15)) and (y > (y_coord1 - 15)))) or ((x == x_coord2 - 35) and ((y < (y_coord2 + 150 + 15)) and (y > (y_coord2 - 15)))):
        xoffset = xoffset * (- 1)
        if ((x == x_coord1 + 15) and ((y < (y_coord1 + 150 + 15)) and (y > (y_coord1 - 15)))):
            click_sound2.play()
        elif ((x == x_coord2 - 35) and ((y < (y_coord2 + 150 + 15)) and (y > (y_coord2 - 15)))):
            click_sound3.play()
    x = x + xoffset
    if y < 1 or y > 1060:
        yoffset = yoffset * (-1)
        click_sound1.play()
    y = y + yoffset
    if x < 1:
        score1 += 1
    elif x > 1900:
        score2 += 1
    font = pygame.font.Font("C:/Users/Windows 10/Documents/Github/bit5x3.ttf", 40)
    text1 = font.render(str(score1),True,WHITE)
    screen.blit(text1,[935,10])  
    text2 = font.render(str(score2),True,WHITE)  
    screen.blit(text2,[970,10]) 
    # --- Drawing code should go here
    pygame.draw.ellipse(screen, WHITE, [x,y,20,20], 0)
    pygame.draw.rect(screen,WHITE,[x_coord1,y_coord1,15,150],4)
    pygame.draw.rect(screen,WHITE,[x_coord2,y_coord2,15,150],4)
    pygame.draw.rect(screen,WHITE,[960,0,1,5],0)
    pygame.draw.rect(screen,WHITE,[960,10,1,5],0)
    pygame.draw.rect(screen,WHITE,[960,20,1,5],0)
    pygame.draw.rect(screen,WHITE,[960,30,1,5],0)
    pygame.draw.rect(screen,WHITE,[960,40,1,5],0)
    pygame.draw.rect(screen,WHITE,[960,50,1,5],0)
    pygame.draw.rect(screen,WHITE,[960,60,1,5],0)
    pygame.draw.rect(screen,WHITE,[960,70,1,5],0)
    pygame.draw.rect(screen,WHITE,[960,80,1,5],0)
    pygame.draw.rect(screen,WHITE,[960,90,1,5],0)
    pygame.draw.rect(screen,WHITE,[960,100,1,5],0)
    pygame.draw.rect(screen,WHITE,[960,110,1,5],0)
    pygame.draw.rect(screen,WHITE,[960,120,1,5],0)
    pygame.draw.rect(screen,WHITE,[960,130,1,5],0)
    pygame.draw.rect(screen,WHITE,[960,140,1,5],0)
    pygame.draw.rect(screen,WHITE,[960,150,1,5],0)
    pygame.draw.rect(screen,WHITE,[960,160,1,5],0)
    pygame.draw.rect(screen,WHITE,[960,170,1,5],0)
    pygame.draw.rect(screen,WHITE,[960,180,1,5],0)
    pygame.draw.rect(screen,WHITE,[960,190,1,5],0)
    pygame.draw.rect(screen,WHITE,[960,200,1,5],0)
    pygame.draw.rect(screen,WHITE,[960,210,1,5],0)
    pygame.draw.rect(screen,WHITE,[960,220,1,5],0)
    pygame.draw.rect(screen,WHITE,[960,230,1,5],0)
    pygame.draw.rect(screen,WHITE,[960,240,1,5],0)
    pygame.draw.rect(screen,WHITE,[960,250,1,5],0)
    pygame.draw.rect(screen,WHITE,[960,260,1,5],0)
    pygame.draw.rect(screen,WHITE,[960,270,1,5],0)
    pygame.draw.rect(screen,WHITE,[960,280,1,5],0)
    pygame.draw.rect(screen,WHITE,[960,290,1,5],0)
    pygame.draw.rect(screen,WHITE,[960,300,1,5],0)
    pygame.draw.rect(screen,WHITE,[960,310,1,5],0)
    pygame.draw.rect(screen,WHITE,[960,320,1,5],0)
    pygame.draw.rect(screen,WHITE,[960,330,1,5],0)
    pygame.draw.rect(screen,WHITE,[960,340,1,5],0)
    pygame.draw.rect(screen,WHITE,[960,350,1,5],0)
    pygame.draw.rect(screen,WHITE,[960,360,1,5],0)
    pygame.draw.rect(screen,WHITE,[960,370,1,5],0)
    pygame.draw.rect(screen,WHITE,[960,380,1,5],0)
    pygame.draw.rect(screen,WHITE,[960,390,1,5],0)
    pygame.draw.rect(screen,WHITE,[960,400,1,5],0)
    pygame.draw.rect(screen,WHITE,[960,410,1,5],0)
    pygame.draw.rect(screen,WHITE,[960,420,1,5],0)
    pygame.draw.rect(screen,WHITE,[960,430,1,5],0)
    pygame.draw.rect(screen,WHITE,[960,440,1,5],0)
    pygame.draw.rect(screen,WHITE,[960,450,1,5],0)
    pygame.draw.rect(screen,WHITE,[960,460,1,5],0)
    pygame.draw.rect(screen,WHITE,[960,470,1,5],0)
    pygame.draw.rect(screen,WHITE,[960,480,1,5],0)
    pygame.draw.rect(screen,WHITE,[960,490,1,5],0)
    pygame.draw.rect(screen,WHITE,[960,500,1,5],0)
    pygame.draw.rect(screen,WHITE,[960,510,1,5],0)
    pygame.draw.rect(screen,WHITE,[960,520,1,5],0)
    pygame.draw.rect(screen,WHITE,[960,530,1,5],0)
    pygame.draw.rect(screen,WHITE,[960,540,1,5],0)
    pygame.draw.rect(screen,WHITE,[960,550,1,5],0)
    pygame.draw.rect(screen,WHITE,[960,560,1,5],0)
    pygame.draw.rect(screen,WHITE,[960,570,1,5],0)
    pygame.draw.rect(screen,WHITE,[960,580,1,5],0)
    pygame.draw.rect(screen,WHITE,[960,590,1,5],0)
    pygame.draw.rect(screen,WHITE,[960,600,1,5],0)
    pygame.draw.rect(screen,WHITE,[960,610,1,5],0)
    pygame.draw.rect(screen,WHITE,[960,620,1,5],0)
    pygame.draw.rect(screen,WHITE,[960,630,1,5],0)
    pygame.draw.rect(screen,WHITE,[960,640,1,5],0)
    pygame.draw.rect(screen,WHITE,[960,650,1,5],0)
    pygame.draw.rect(screen,WHITE,[960,660,1,5],0)
    pygame.draw.rect(screen,WHITE,[960,670,1,5],0)
    pygame.draw.rect(screen,WHITE,[960,680,1,5],0)
    pygame.draw.rect(screen,WHITE,[960,690,1,5],0)
    pygame.draw.rect(screen,WHITE,[960,700,1,5],0)
    pygame.draw.rect(screen,WHITE,[960,710,1,5],0)
    pygame.draw.rect(screen,WHITE,[960,720,1,5],0)
    pygame.draw.rect(screen,WHITE,[960,730,1,5],0)
    pygame.draw.rect(screen,WHITE,[960,740,1,5],0)
    pygame.draw.rect(screen,WHITE,[960,750,1,5],0)
    pygame.draw.rect(screen,WHITE,[960,760,1,5],0)
    pygame.draw.rect(screen,WHITE,[960,770,1,5],0)
    pygame.draw.rect(screen,WHITE,[960,780,1,5],0)
    pygame.draw.rect(screen,WHITE,[960,790,1,5],0)
    pygame.draw.rect(screen,WHITE,[960,800,1,5],0)
    pygame.draw.rect(screen,WHITE,[960,810,1,5],0)
    pygame.draw.rect(screen,WHITE,[960,820,1,5],0)
    pygame.draw.rect(screen,WHITE,[960,830,1,5],0)
    pygame.draw.rect(screen,WHITE,[960,840,1,5],0)
    pygame.draw.rect(screen,WHITE,[960,850,1,5],0)
    pygame.draw.rect(screen,WHITE,[960,860,1,5],0)
    pygame.draw.rect(screen,WHITE,[960,870,1,5],0)
    pygame.draw.rect(screen,WHITE,[960,880,1,5],0)
    pygame.draw.rect(screen,WHITE,[960,890,1,5],0)
    pygame.draw.rect(screen,WHITE,[960,900,1,5],0)
    pygame.draw.rect(screen,WHITE,[960,910,1,5],0)
    pygame.draw.rect(screen,WHITE,[960,920,1,5],0)
    pygame.draw.rect(screen,WHITE,[960,930,1,5],0)
    pygame.draw.rect(screen,WHITE,[960,940,1,5],0)
    pygame.draw.rect(screen,WHITE,[960,950,1,5],0)
    pygame.draw.rect(screen,WHITE,[960,960,1,5],0)
    pygame.draw.rect(screen,WHITE,[960,970,1,5],0)
    pygame.draw.rect(screen,WHITE,[960,980,1,5],0)
    pygame.draw.rect(screen,WHITE,[960,990,1,5],0)
    pygame.draw.rect(screen,WHITE,[960,1000,1,5],0)
    pygame.draw.rect(screen,WHITE,[960,1010,1,5],0)
    pygame.draw.rect(screen,WHITE,[960,1020,1,5],0)
    pygame.draw.rect(screen,WHITE,[960,1030,1,5],0)
    pygame.draw.rect(screen,WHITE,[960,1040,1,5],0)
    pygame.draw.rect(screen,WHITE,[960,1050,1,5],0)
    pygame.draw.rect(screen,WHITE,[960,1060,1,5],0)
    pygame.draw.rect(screen,WHITE,[960,1070,1,5],0)
    pygame.draw.rect(screen,WHITE,[960,1080,1,5],0)
    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
 
    # --- Limit to 60 frames per second
    clock.tick(60)
    if y_coord1 < 0:
        y_coord1 = 0
    if y_coord1 > 980:
        y_coord1 = 980
    if y_coord2 < 0:
        y_coord2 = 0
    if y_coord2 > 980:
        y_coord2 = 980
# Close the window and quit.
