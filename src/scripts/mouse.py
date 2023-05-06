import pygame
from pygame.locals import *


class Mouse:
    position = pygame.Vector2(0, 0)
    hovered = False
    visible = True

    @classmethod
    def update(cls):
        pygame.mouse.set_visible(cls.visible)

        if cls.hovered:
            pygame.mouse.set_cursor(SYSTEM_CURSOR_HAND)     
        else:
            pygame.mouse.set_cursor(SYSTEM_CURSOR_ARROW)

        cls.hovered = False
        cls.visible = True

    @classmethod
    def handle_event(cls, event):
        if event.type == MOUSEMOTION:
            cls.position.update(event.pos)