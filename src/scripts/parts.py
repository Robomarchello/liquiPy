import pygame
from pygame._sdl2.video import Texture
from .ui import Button


class ToolBar:
    def __init__(self, renderer):
        self.rect = pygame.Rect(0, 540, 960, 70)
        self.color = pygame.Color(35, 36, 40)

        self.buttons = []
        self.buttons.append(
            Button(
            Texture.from_surface(renderer,
                                pygame.image.load('src/assets/SaveBtn.png')),
            (10, 545), self.save)
        )
        self.buttons.append(
            Button(
            Texture.from_surface(renderer,
                                pygame.image.load('src/assets/UploadBtn.png')),
            (130, 545), self.load)
        )
        self.buttons.append(
            Button(
            Texture.from_surface(renderer,
                                pygame.image.load('src/assets/SmudgeBtn.png')),
            (250, 545), self.smudge)
        )
        self.buttons.append(
            Button(
            Texture.from_surface(renderer,
                                pygame.image.load('src/assets/SwirlBtn.png')),
            (370, 545), self.swirl)
        )
    
    def save(self):
        print('save')
        
    def load(self):
        print('load')

    def smudge(self):
        print('smudge')

    def swirl(self):
        print('swirl')
    
    def draw(self, renderer):
        renderer.draw_color = (35, 36, 40, 255)
        renderer.fill_rect(self.rect)
        
        for button in self.buttons:
            button.draw(renderer)

    def handle_event(self, event):
        for button in self.buttons:
            button.handle_event(event)


class Editor:
    def __init__(self):
        self.rect = pygame.Rect(0, 0, 960, 540)

    def draw(self, renderer):
        pass