import pygame

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
YELLOWISH = (234, 226, 61)
BEIGE = (220, 213, 185)
BROWN = (196, 164, 132)
DARKBROWN = (92, 64, 51)
CYAN = (0, 255, 255)
x = 600
xoffset = 50
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
 
    # --- Screen-clearing code goes here
 
    # Here, we clear the screen to white. Don't put other drawing commands
    # above this, or they will be erased with this command.
 
    # If you want a background image, replace this clear with blit'ing the
    # background image.
    screen.fill(WHITE)
 
    # --- Drawing code should go here
    pygame.draw.rect(screen,GREEN,[0,300,1000,200],0)
    pygame.draw.rect(screen,BLUE,[0,0,1000,300],0)
    if x < 1 or x > 699:
        xoffset = xoffset * - 1
    x = x + xoffset
    
    pygame.draw.ellipse(screen, YELLOWISH, [x,20,60,60], 0)
    pygame.draw.rect(screen,BEIGE,[275,350,75,200],0)
    pygame.draw.rect(screen,BROWN,[230,175,200,200],0)
    pygame.draw.rect(screen,DARKBROWN,[275,275,75,100],0)
    pygame.draw.ellipse(screen, BLACK, [330,325,10,10], 0)
    #pygame.draw.rect(screen,DARKBROWN,[275,275,75,100],0)
    pygame.draw.rect(screen,CYAN,[370,200,50,50],0)
    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
 
    # --- Limit to 60 frames per second
    clock.tick(60)
 
# Close the window and quit.
pygame.quit()