from .mouse import Mouse
import pygame
from pygame.locals import MOUSEBUTTONDOWN, MOUSEBUTTONUP
from pygame._sdl2.video import Texture
from math import sqrt


class Tool:
    radius = 32
    def __init__(self, renderer):
        self.position = Mouse.position
        self.PrevPos = self.position.copy()

        self.image = Texture.from_surface(
            renderer,
            pygame.image.load('src/assets/tool.png')
        )

        self.rect = pygame.Rect(0, 0, self.radius * 2, self.radius * 2)
        self.rect.center = self.position

        self.selected = False
        self.holding = False
        
    def update_cursor(self):
        self.rect = pygame.Rect(0, 0, self.radius * 2, self.radius * 2)
        self.rect.center = self.position
    
    def draw(self, renderer):
        self.image.draw(dstrect=self.rect)

    def handle_event(self, event):
        if event.type == MOUSEBUTTONDOWN:
            if event.button == 1:
                self.holding = True
                    

        if event.type == MOUSEBUTTONUP:
            if event.button == 1:
                self.holding = False


class Smudge(Tool):
    def __init__(self, renderer):
        super().__init__(renderer)

    def update(self, mesh):
        movement = self.position - self.PrevPos
        self.PrevPos = self.position.copy()

        self.update_cursor()
        if self.selected:
            collisions = self.get_colliding(mesh)

            if self.holding:
                for index, position in enumerate(collisions[0]):
                    position += movement * (1 - (collisions[1][index] / self.radius))
                    

    def get_colliding(self, mesh):
        positions = []
        distances = []
        for position in mesh:
            if self.rect.collidepoint(position):
                diff = [self.position[0] - position[0],
                        self.position[1] - position[1]]
                
                distance = sqrt(diff[0] ** 2 + diff[1] ** 2)
                if distance < self.radius:
                    positions.append(position)
                    distances.append(distance)

        return [positions, distances]