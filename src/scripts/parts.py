import pygame
from pygame._sdl2.video import Texture
from pygame.locals import MOUSEWHEEL
from .ui import Button
from .mouse import Mouse
from .mesh import Grid
from .tools import Tool, Smudge, Swirl
from tkinter import Tk, filedialog


class ToolBar:
    def __init__(self, renderer, grid, editor):
        self.rect = pygame.Rect(0, 540, 960, 70)
        self.color = pygame.Color(35, 36, 40)

        self.renderer = renderer

        self.text = Texture.from_surface(
            renderer,
            pygame.image.load('src/assets/tooljam.png')
        )
        self.textRect = self.text.get_rect(bottomright=(955, 605))

        save = grid.save()
        self.editor = editor

        self.buttons = []
        self.buttons.append(
            Button(
            Texture.from_surface(renderer,
                                pygame.image.load('src/assets/SaveBtn.png')),
            (10, 545), save)
        )
        self.buttons.append(
            Button(
            Texture.from_surface(renderer,
                                pygame.image.load('src/assets/UploadBtn.png')),
            (130, 545), self.openFile)
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
        
    def openFile(self):
        """Create a Tk file dialog and cleanup when finished"""
        tk = Tk()
        tk.withdraw() 
        file_name = filedialog.askopenfilename(parent=tk)
        tk.destroy()
        
        self.image = Texture.from_surface(self.renderer, file_name)
        imageRect = self.image.get_rect()
        imageRect = self.imageRect.fit(self.rect)

        return file_name

    def smudge(self):
        print('smudge')

    def swirl(self):
        print('swirl')
    
    def draw(self, renderer):
        renderer.draw_color = (35, 36, 40, 255)
        renderer.fill_rect(self.rect)

        self.text.draw(dstrect=self.textRect)
        
        for button in self.buttons:
            button.draw(renderer)

    def handle_event(self, event):
        for button in self.buttons:
            button.handle_event(event)


class Editor:
    def __init__(self, renderer, image=None):
        self.rect = pygame.Rect(0, 0, 960, 540)
        
        #pixels per cell 
        self.pixelspc = 25
        
        self.image = image

        self.grid = Grid(renderer, self.image, self.pixelspc, self.rect)

        self.minRadius = 16
        self.tools = [
            Smudge(renderer),
            Swirl(renderer)
        ]
        self.toolIndex = 1

    def draw(self, renderer):
        #self.image.draw(dstrect=self.imageRect)
        self.grid.draw(renderer)

        tool = self.tools[self.toolIndex]
        tool.update(self.grid.mesh)
        tool.draw(renderer)
        tool.selected = True

    def handle_event(self, event):
        if event.type == MOUSEWHEEL:
            Tool.radius += event.y
            if Tool.radius <= self.minRadius:
                Tool.radius = self.minRadius

        self.tools[self.toolIndex].handle_event(event)