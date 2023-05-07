from .mouse import Mouse
import pygame
from pygame._sdl2.video import Texture


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

        self.active = False

    def update_cursor(self):
        self.rect = pygame.Rect(0, 0, self.radius * 2, self.radius * 2)
        self.rect.center = self.position
    
    def draw(self, renderer):
        self.image.draw(dstrect=self.rect)


class Smudge(Tool):
    def __init__(self, renderer):
        super().__init__(renderer)

    def update(self, mesh):
        movement = self.PrevPos - self.position
        self.PrevPos = self.position.copy()

        print(movement)
        self.update_cursor()
        if self.active:
            self.get_colliding(mesh)

    def get_colliding(self, mesh):
        positions = []
        for position in mesh:
            if self.rect.collidepoint(position):
                positions.append(position)