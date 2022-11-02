"""
 Pygame base template for opening a window
 
 Sample Python/Pygame Programs
 Simpson College Computer Science
 http://programarcadegames.com/
 http://simpson.edu/computer-science/
 
 Explanation video: http://youtu.be/vRB_983kUMc
"""
 
import pygame
 
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
y_speed = 1
x_coord1 = 1
y_coord1 = 200
x_coord2 = 690
y_coord2 = 200
collide = 0
pygame.init()
 
# Set the width and height of the screen [width, height]
size = (700, 500)
screen = pygame.display.set_mode(size)
 
pygame.display.set_caption("My Game")
 
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
            y_coord1 += y_speed  #code to make the rectangle actually move (so y_coord1 will have y_speed added to it and then the value is assigned back to y_coord1)
            if y_coord1 < 1:
                y_coord1 = 1
            elif y_coord1 > 450:
                y_coord1 = 450
        #This is the code for when the key isn't pressed        
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                y_speed = 0
            
    # --- Screen-clearing code goes here
 
    # Here, we clear the screen to white. Don't put other drawing commands
    # above this, or they will be erased with this command.
 
    # If you want a background image, replace this clear with blit'ing the
    # background image.
    screen.fill(WHITE)
    y_coord1 += y_speed  #code to make the rectangle actually move (so y_coord1 will have y_speed added to it and then the value is assigned back to y_coord1)
    if x < 1 or x > 670:
        x = 350
        y = 250
    if ((x == x_coord1 + 20) and ((y < (y_coord1 + 100 + 50)) or (y > (y_coord1 + 100 - 50)))) or ((x == x_coord2 + 20)):
        xoffset = xoffset * (- 1)
    x = x + xoffset
    if y < 1 or y > 470:
        yoffset = yoffset * (-1)
    y = y + yoffset
 
    # --- Drawing code should go here
    pygame.draw.rect(screen, BLACK, [0,0,700,500], 0)
    pygame.draw.ellipse(screen, WHITE, [x,y,30,30], 0)
    pygame.draw.rect(screen,WHITE,[x_coord1,y_coord1,10,100],3)
    pygame.draw.rect(screen,WHITE,[x_coord2,y_coord2,10,100],3)
    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
 
    # --- Limit to 60 frames per second
    clock.tick(60)
 
# Close the window and quit.
pygame.quit()