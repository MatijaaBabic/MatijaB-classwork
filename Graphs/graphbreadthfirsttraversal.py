import pygame
import sys
from queue import Queue
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GRAY = (109, 112, 114)
GREEN = (0, 255, 0)
class Graph(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.color = WHITE
        self.graph = {
            "A": {"colour": "White", "neighbours": ["B", "D", "E"]},
            "B": {"colour": "White", "neighbours": ["A", "D", "C"]},
            "C": {"colour": "White", "neighbours": ["B", "G"]},
            "D": {"colour": "White", "neighbours": ["A", "B", "E", "F"]},
            "E": {"colour": "White", "neighbours": ["A", "D"]},
            "F": {"colour": "White", "neighbours": ["D"]},
            "G": {"colour": "White", "neighbours": ["C"]}
        }
    def drawing():
        pygame.draw.circle(screen, self.color, [900, 60, 50, 50], 0)
        for i in range (0, 5):
            pygame.draw.circle(screen, self.color, [900, 60, 50, 50], 0)

pygame.init()
info = pygame.display.Info()
SIZE = W, H = info.current_w, info.current_h
screen = pygame.display.set_mode(SIZE)
clock = pygame.time.Clock()