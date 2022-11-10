import pygame
import random
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (115, 181, 239)
YELLOW = (234, 226, 61)

class Invader(pygame.sprite.Sprite):
    def _init_(self):
        pygame.sprite.Sprite._init_(self)
        self.image = pygame.image.load("enemy.png").convert_alpha()
        self.image.set_colorkey(WHITE)
        self.rect = self.image.get_rect()
    def update(self):
        self.rect.y += 2
        if self.rect.y > H:
            self.rect.y = random.randrange(20, 100)
            self.rect.x = random.randrange(0, W)
pygame.init() 
info = pygame.display.Info()
SIZE = W, H = info.current_w, info.current_h
screen = pygame.display.set_mode(SIZE)
pygame.display.set_caption("Space Invaders")
block_list = pygame.sprite.Group()
for i in range(25):
    block = Invader()
    block.rect.x = random.randrange(W)
    block.rect.y = random.randrange(H)
    block_list.add(block)
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
        elif event.type == pygame.KEYDOWN:     #we can use while if we want it to move for as long as the key is presed
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
        #code to make the rectangle actually move (so y_coord1 will have y_speed added to it and then the value is assigned back to y_coord1)
        #This is the code for when the key isn't pressed        

    # --- Game logic should go here
    
    
    # --- Screen-clearing code goes here
 
    # Here, we clear the screen to white. Don't put other drawing commands
    # above this, or they will be erased with this command.
 
    # If you want a background image, replace this clear with blit'ing the
    # background image.
    screen.fill(WHITE)
 
    # --- Drawing code should go here
    block_list.update()
    block_list.draw(screen)
    blocks_hit_list = pygame.sprite.spritecollide(block, block_list, True)
    #if len(blocks_hit_list) > 0:

    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
 
    # --- Limit to 60 frames per second
    clock.tick(60)
 
# Close the window and quit.
pygame.quit()