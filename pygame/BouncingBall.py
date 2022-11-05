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
x = 350
y = 250
xoffset = 2
yoffset = 3
y_speed = 0
y_speed2 = 0
x_coord1 = 0
y_coord1 = 200
x_coord2 = 690
y_coord2 = 200
collide = 0
score1 = 0
score2 = 0

pygame.init()
#info = pygame.display.Info()
#SIZE = W, H = info.current_w, info.current_h
#screen = pygame.display.set_mode(SIZE)
# Set the width and height of the screen [width, height]
size = (700, 500)
screen = pygame.display.set_mode(size)
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
                y_speed = -3
            elif event.key == pygame.K_DOWN:
                y_speed = 3
            elif event.key == pygame.K_w:
                y_speed2 = -3
            elif event.key == pygame.K_s:
                y_speed2 = 3
        #code to make the rectangle actually move (so y_coord1 will have y_speed added to it and then the value is assigned back to y_coord1)
        #This is the code for when the key isn't pressed        
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                y_speed = 0
            elif event.key == pygame.K_w or event.key == pygame.K_s:    
                y_speed2 = 0      
        font = pygame.font.Font(None, 25)
        text1 = font.render(str(score1),True,WHITE)
        screen.blit(text1,[330,10])          
    # --- Screen-clearing code goes here
 
    # Here, we clear the screen to white. Don't put other drawing commands
    # above this, or they will be erased with this command.
 
    # If you want a background image, replace this clear with blit'ing the
    # background image.
    screen.fill(BLACK)
    y_coord1 += y_speed  #code to make the rectangle actually move (so y_coord1 will have y_speed added to it and then the value is assigned back to y_coord1)
    y_coord2 += y_speed2
    if x < 1 or x > 685:
        x = 350
        y = 250
        y_coord1 = 200
        y_coord2 = 200
    if ((x == x_coord1 + 10) and ((y < (y_coord1 + 100 + 15)) and (y > (y_coord1 - 15)))) or ((x == x_coord2 - 18) and ((y < (y_coord2 + 100 + 15)) and (y > (y_coord2 - 15)))):
        xoffset = xoffset * (- 1)
    x = x + xoffset
    if y < 1 or y > 485:
        yoffset = yoffset * (-1)
    y = y + yoffset
    if x < 1:
        score1 += 1
    elif x > 685:
        score2 += 1
    font = pygame.font.Font("C:/Users/Windows 10/Documents/Github/bit5x3.ttf", 40)
    text1 = font.render(str(score1),True,WHITE)
    screen.blit(text1,[330,10])  
    text2 = font.render(str(score2),True,WHITE)  
    screen.blit(text2,[360,10]) 
    # --- Drawing code should go here
    pygame.draw.ellipse(screen, WHITE, [x,y,15,15], 0)
    pygame.draw.rect(screen,WHITE,[x_coord1,y_coord1,10,100],3)
    pygame.draw.rect(screen,WHITE,[x_coord2,y_coord2,10,100],3)
    pygame.draw.rect(screen,WHITE,[350,0,1,5],0)
    pygame.draw.rect(screen,WHITE,[350,10,1,5],0)
    pygame.draw.rect(screen,WHITE,[350,20,1,5],0)
    pygame.draw.rect(screen,WHITE,[350,30,1,5],0)
    pygame.draw.rect(screen,WHITE,[350,40,1,5],0)
    pygame.draw.rect(screen,WHITE,[350,50,1,5],0)
    pygame.draw.rect(screen,WHITE,[350,60,1,5],0)
    pygame.draw.rect(screen,WHITE,[350,70,1,5],0)
    pygame.draw.rect(screen,WHITE,[350,80,1,5],0)
    pygame.draw.rect(screen,WHITE,[350,90,1,5],0)
    pygame.draw.rect(screen,WHITE,[350,100,1,5],0)
    pygame.draw.rect(screen,WHITE,[350,110,1,5],0)
    pygame.draw.rect(screen,WHITE,[350,120,1,5],0)
    pygame.draw.rect(screen,WHITE,[350,130,1,5],0)
    pygame.draw.rect(screen,WHITE,[350,140,1,5],0)
    pygame.draw.rect(screen,WHITE,[350,150,1,5],0)
    pygame.draw.rect(screen,WHITE,[350,160,1,5],0)
    pygame.draw.rect(screen,WHITE,[350,170,1,5],0)
    pygame.draw.rect(screen,WHITE,[350,180,1,5],0)
    pygame.draw.rect(screen,WHITE,[350,190,1,5],0)
    pygame.draw.rect(screen,WHITE,[350,200,1,5],0)
    pygame.draw.rect(screen,WHITE,[350,210,1,5],0)
    pygame.draw.rect(screen,WHITE,[350,220,1,5],0)
    pygame.draw.rect(screen,WHITE,[350,230,1,5],0)
    pygame.draw.rect(screen,WHITE,[350,240,1,5],0)
    pygame.draw.rect(screen,WHITE,[350,250,1,5],0)
    pygame.draw.rect(screen,WHITE,[350,260,1,5],0)
    pygame.draw.rect(screen,WHITE,[350,270,1,5],0)
    pygame.draw.rect(screen,WHITE,[350,280,1,5],0)
    pygame.draw.rect(screen,WHITE,[350,290,1,5],0)
    pygame.draw.rect(screen,WHITE,[350,300,1,5],0)
    pygame.draw.rect(screen,WHITE,[350,310,1,5],0)
    pygame.draw.rect(screen,WHITE,[350,320,1,5],0)
    pygame.draw.rect(screen,WHITE,[350,330,1,5],0)
    pygame.draw.rect(screen,WHITE,[350,340,1,5],0)
    pygame.draw.rect(screen,WHITE,[350,350,1,5],0)
    pygame.draw.rect(screen,WHITE,[350,360,1,5],0)
    pygame.draw.rect(screen,WHITE,[350,370,1,5],0)
    pygame.draw.rect(screen,WHITE,[350,380,1,5],0)
    pygame.draw.rect(screen,WHITE,[350,390,1,5],0)
    pygame.draw.rect(screen,WHITE,[350,400,1,5],0)
    pygame.draw.rect(screen,WHITE,[350,410,1,5],0)
    pygame.draw.rect(screen,WHITE,[350,420,1,5],0)
    pygame.draw.rect(screen,WHITE,[350,430,1,5],0)
    pygame.draw.rect(screen,WHITE,[350,440,1,5],0)
    pygame.draw.rect(screen,WHITE,[350,450,1,5],0)
    pygame.draw.rect(screen,WHITE,[350,460,1,5],0)
    pygame.draw.rect(screen,WHITE,[350,470,1,5],0)
    pygame.draw.rect(screen,WHITE,[350,480,1,5],0)
    pygame.draw.rect(screen,WHITE,[350,490,1,5],0)
    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
 
    # --- Limit to 60 frames per second
    clock.tick(60)
    if y_coord1 < 0:
        y_coord1 = 0
    if y_coord1 > 400:
        y_coord1 = 400
    if y_coord2 < 0:
        y_coord2 = 0
    if y_coord2 > 400:
        y_coord2 = 400
# Close the window and quit.
pygame.quit()