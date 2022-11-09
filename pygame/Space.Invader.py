import pygame
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (115, 181, 239)
YELLOW = (234, 226, 61)
class Invader():
    def _init_(self):
        self.max_health = 2
        self.health = 2
        self.max_speed = 3
        self.armor = 0
        self.colour = BLUE
        self.width = 50
        self.height = 50
        self.x = 0
        self.y = 0
    def speak(self):
        print("Hi :D")

invader1 = Invader()  
invader1.x = 100
invader1.x = 100
print(invader1.speak())

invader2 = Invader()  
invader2.x = 200
invader2.x = 100
