import pygame
import random
from pygame import mixer
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (115, 181, 239)
YELLOW = (234, 226, 61)
kills = 0
score = 0
highest_score = 0
level = 1
velp = 0
offset = 128
class Invader(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("enemy.png").convert_alpha()
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.health = 2
        
    def update(self):
        self.rect.y = self.rect.y + 1
        if self.rect.y > H - 192:
            self.rect.y = H - 192


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("Player.png").convert_alpha()
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
    

class Background(pygame.sprite.Sprite):
    def __init__(self, image_file, location):
        pygame.sprite.Sprite.__init__(self)  #call Sprite initializer
        self.image = pygame.image.load(image_file)
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = location

def game_over():
    game_over_text = font.render("GAME OVER", True, WHITE)
    screen.blit(game_over_text, (760, 440))

pygame.init() 
font = pygame.font.Font("C:/Users/Windows 10/Documents/Github/bit5x3.ttf", 200)
info = pygame.display.Info()
SIZE = W, H = info.current_w, info.current_h
screen = pygame.display.set_mode(SIZE)
pygame.display.set_caption("Space Invaders")
block_list = pygame.sprite.Group()
all_sprites_list = pygame.sprite.Group()
bg = Background('bg.jpg', [0,0])
for y in range (0,3):
    offset = 128
    for i in range(0,9):         #if we do it this way always write it as one more enemy than you want
        block = Invader()
        block.rect.x = offset
        offset = offset + 128
        block.rect.y = 10 + 64 * y
        block_list.add(block)
        all_sprites_list.add(block)
        block_list.update()
player = Player()
player.rect.x = 928
player.rect.y = 1000
all_sprites_list.add(player)
#pygame.mixer.init()
#pygame.mixer.music.load('05_Earth.mp3')
#pygame.mixer.music.play()
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
                pygame.mixer.music.stop()
                pygame.quit()
            if event.key == pygame.K_LEFT:
                velp = -5
            elif event.key == pygame.K_RIGHT:
                velp = 5
        #code to make the rectangle actually move (so y_coord1 will have y_speed added to it and then the value is assigned back to y_coord1)
        #This is the code for when the key isn't pressed        
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                 velp = 0
    # --- Game logic should go here
 
    # --- Screen-clearing code goes here
 
    # Here, we clear the screen to white. Don't put other drawing commands
    # above this, or they will be erased with this command.
    player.rect.x += velp
    # If you want a background image, replace this clear with blit'ing the
    # background image.
    screen.fill([255, 255, 255])
    screen.blit(bg.image, bg.rect)
    # --- Drawing code should go here
    all_sprites_list.draw(screen)
    blocks_hit_list = pygame.sprite.spritecollide(block, block_list, True)
    block_list.update()
    
    #if len(blocks_hit_list) > 0:

    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
    if player.rect.x < 0:
        player.rect.x = 0
    if player.rect.x > 1856:
        player.rect.x = 1856
    # --- Limit to 60 frames per second
    clock.tick(60)
 
# Close the window and quit.
pygame.mixer.music.stop()
pygame.quit()