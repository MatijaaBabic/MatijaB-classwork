import pygame
import random
from pygame import mixer
import pygame_menu
import os
import sys
os.chdir(r'C:\Users\Windows 10\Desktop\Microsoft\Prezentacije\Programs for school\Code\Github\MatijaB-classwork\pygame\Space Invaders')
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (115, 181, 239)
YELLOW = (234, 226, 61)
kills = 0
score = 0
highest_score = 0
velp = 0
offset = 48
speed = 2
playsound = True
m = 20
n = 3
c_level = 1
z = 0
class Invader(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("enemy.png").convert_alpha()
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.health = 2
        self.counter = 0
        
    def update(self):
        if self.counter % m == 0:
            self.rect.y += speed
        if self.counter == 0:
            self.rect.x += 50
        if self.counter == 50:
            self.rect.x += 70
        if self.counter == 100:
            self.rect.x += 100
        if self.counter == 150:
            self.rect.x -= 50
        if self.counter == 200:
            self.rect.x -= 70
        if self.counter == 250:
            self.rect.x -= 100
        self.counter += 1
        if self.counter == 300:
            self.counter = 0
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("Player.png").convert_alpha()
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.score = 0
        self.highscore = 0
class Bullet(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("laser.png")
        self.rect = self.image.get_rect()
        self.speeeeed = -7
        self.health = 1
    def update(self):
        self.rect.y += self.speeeeed
        if self.rect.y < 0:
            self.kill()
    def death(self):
        if self.health == 0:
            self.kill()
class Background(pygame.sprite.Sprite):
    def __init__(self, image_file, location):
        pygame.sprite.Sprite.__init__(self)  #call Sprite initializer
        self.image = pygame.image.load(image_file)
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = location

class Boom(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.images = []
        for i in range (0, 7):
            img = pygame.image.load(f"boom{i}.png")
            img = pygame.transform.scale(img, (32, 32))
            self.images.append(img)
        self.index = 0
        self.image = self.images[self.index]
        self.rect = self.image.get_rect()
        self.counter = 0
    def update(self):
        boom_speed = 4
        self.counter += 1
        if self.counter >= boom_speed and self.index < len(self.images) - 1:
            self.counter = 0
            self.index += 1
            self.image = self.images[self.index]
        if self.index >= len(self.images) - 1 and self.counter >= boom_speed:
            self.kill()


def game_over():
    global playsound
    global speed
    mixer.music.stop()
    player.kill()
    speed = 0
    game_over_text = font.render("GAME OVER", True, WHITE)
    screen.blit(game_over_text, (600, 440))
    if playsound:
        lose_s.play()
        playsound = False
def win():
    global playsound
    mixer.music.stop()
    player.kill()
    win_text = font.render("YOU WIN!", True, WHITE)
    screen.blit(win_text, (600, 440))
    if playsound:
        win_s.play()
        playsound = False

pygame.init() 
shooting_sound = pygame.mixer.Sound("shooting.wav")
win_s = pygame.mixer.Sound("win.wav")
lose_s = pygame.mixer.Sound("lose.wav")
boom_s = pygame.mixer.Sound("explosion.wav")
font = pygame.font.Font("C:/Users/Windows 10/Documents/Github/bit5x3.ttf", 200)
font1 = pygame.font.Font("C:/Users/Windows 10/Documents/Github/bit5x3.ttf", 20)
info = pygame.display.Info()
SIZE = W, H = info.current_w, info.current_h
screen = pygame.display.set_mode(SIZE)
pygame.display.set_caption("Space Invaders")
block_list = pygame.sprite.Group()
all_sprites_list = pygame.sprite.Group()
bg = Background('bg.jpg', [0,0])
def change_level():
    global m
    global n
    global c_level
    c_level = c_level + 1
    if c_level == 2:
        m = 10
        n = 3
        block_generator()
    elif c_level == 3:
        m = 15
        n = 5
        block_generator()
    elif c_level == 4:
        m = 10
        n = 3
        block_generator()
    elif c_level == 5: 
        m = 5
        n = 7
        block_generator()
for y in range (0,n):
    offset = 160
    for i in range(0,15):         #if we do it this way always write it as one more enemy than you want
        block = Invader()
        block.rect.x = offset
        offset = offset + 96
        block.rect.y = 10 + 48 * y
        health = block.health
        block_list.add(block)
        all_sprites_list.add(block)
        #block_list.update()
def block_generator():
    for y in range (0,n):
        offset = 160
        for i in range(0,15):         #if we do it this way always write it as one more enemy than you want
            block = Invader()
            block.rect.x = offset
            offset = offset + 96
            block.rect.y = 10 + 48 * y
            health = block.health
            block_list.add(block)
            all_sprites_list.add(block)
            #block_list.update()
player = Player()
player.rect.x = 928
player.rect.y = 1040
all_sprites_list.add(player)
bullet_list = pygame.sprite.Group()
boom_list = pygame.sprite.Group()
#background music
mixer.music.load("background.wav")
mixer.music.play(-1)
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
                sys.exit()
            if event.key == pygame.K_LEFT:
                velp = -3
            elif event.key == pygame.K_RIGHT:
                velp = 3
            if event.key == pygame.K_SPACE:
                bullet = Bullet()
                bullet.rect.x = player.rect.x + 31 
                bullet.rect.y = player.rect.y - 31
                all_sprites_list.add(bullet)
                bullet_list.add(bullet)
                shooting_sound.play()
        #code to make the rectangle actually move (so y_coord1 will have y_speed added to it and then the value is assigned back to y_coord1)
        #This is the code for when the key isn't pressed        
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                 velp = 0
    # --- Game logic should go here
    boom_list.update()
    all_sprites_list.update()
    for bullet in bullet_list:
        block_hit_list = pygame.sprite.spritecollide(bullet, block_list, True)
        for block in block_hit_list:
            bullet_list.remove(bullet)
            all_sprites_list.remove(bullet)
            all_sprites_list.remove(block)
            block_list.remove(block)
            boom = Boom()
            boom_list.add(boom)
            boom.rect.x = block.rect.x + 16
            boom.rect.y = block.rect.y + 16
            boom_s.play()
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
    boom_list.draw(screen)
    num_of_enemies = font1.render("Number of enemies left:", True, WHITE)
    num = font1.render(str(len(block_list)), True, WHITE)
    screen.blit(num_of_enemies, [10, 30])
    screen.blit(num, [250, 30])
    level = font1.render("Current level:",True, WHITE)
    level_number = font1.render(str(c_level), True, WHITE)
    screen.blit(level, [10, 60])
    screen.blit(level_number, [150 , 60])
    ##blocks_hit_list = pygame.sprite.spritecollide(block, block_list, True)
    #if len(blocks_hit_list) > 0:


    if len(block_list) == 0 and c_level != 5:
        change_level()
        block.kill()
        block_list.add(block)
        all_sprites_list.add(block)
        all_sprites_list.draw(screen)
        all_sprites_list.update()
        block_list.update()    
    o = player.rect.y
    p = block.rect.y
    z = 48 * n - 33 * n
    if abs(o - p) < z and len(block_list) != 0: 
        game_over()
    elif len(block_list) == 0 and c_level == 5:
        win()
    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
    if player.rect.x < 0:
        player.rect.x = 0
    if player.rect.x > 1856:
        player.rect.x = 1856
    # --- Limit to 60 frames per second
    clock.tick(60)
 
# Close the window and quit.
pygame.quit()