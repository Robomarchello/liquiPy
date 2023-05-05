import pygame
from pygame.locals import *


class Mouse:
    position = pygame.Vector2(0, 0)
    hovered = False

    @classmethod
    def update(cls):
        if cls.hovered:
            pygame.mouse.set_cursor(SYSTEM_CURSOR_HAND)     
        else:
            pygame.mouse.set_cursor(SYSTEM_CURSOR_ARROW)

        cls.hovered = False

    @classmethod
    def handle_event(cls, event):
        if event.type == MOUSEMOTION:
            cls.position.update(event.pos)