#ui elements

import pygame
from pygame.locals import *
from .mouse import Mouse


class Button:
    def __init__(self, image, position, func, sound=None):
        self.image = image
        self.rect = self.image.get_rect(topleft=position)
        self.function = func

        self.sound = sound
        
        self.hovered = False

    def draw(self, renderer):
        #renderer.blit(self.image, self.rect)
        self.image.draw(dstrect=self.rect)

        if self.rect.collidepoint(Mouse.position):
            self.hovered = True
            Mouse.hovered = True
        else:
            self.hovered = False

        #renderer.draw_color = (255, 0, 0, 0)
        #renderer.fill_rect(self.rect)

    def handle_event(self, event):
        if event.type == MOUSEBUTTONDOWN:
            if event.button == 1:
                if self.hovered:
                    if self.sound != None:
                        self.sound.play()
                        
                    self.function()
