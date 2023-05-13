import pygame
from pygame._sdl2.video import Texture
from pygame.locals import MOUSEWHEEL
from tkinter import filedialog
from os import path
import json
from .ui import Button
from .mouse import Mouse
from .mesh import Grid
from .tools import Tool, Smudge, Swirl, Shrink


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

        #for file dialogs       
        self.filetypes = [
            ('PNG', '*.png'), ('JPEG', '*.jpg *.jpeg'),
            ('BMP', '*.bmp'), ('TGA', '.tga')
            ]
        self.imageFiles = [('Image Files', '*.png *.jpg *.jpeg *.bmp *.webp')]
        
        self.grid = grid
        self.editor = editor

        btnSound = pygame.mixer.Sound('src/assets/click.ogg')
        self.buttons = []
        self.buttons.append(
            Button(
            Texture.from_surface(renderer,
                                pygame.image.load('src/assets/SaveBtn.png')),
            (10, 545), self.SaveImage, btnSound)
        )        
        self.buttons.append(
            Button(
            Texture.from_surface(renderer,
                                pygame.image.load('src/assets/UploadBtn.png')),
            (130, 545), self.openFile, btnSound)
        )
        self.buttons.append(
            Button(
            Texture.from_surface(renderer,
                                pygame.image.load('src/assets/RestartBtn.png')),
            (250, 545), self.restart, btnSound)
        )
        self.buttons.append(
            Button(
            Texture.from_surface(renderer,
                                pygame.image.load('src/assets/SmudgeBtn.png')),
            (370, 545), self.smudge, btnSound)
        )
        self.buttons.append(
            Button(
            Texture.from_surface(renderer,
                                pygame.image.load('src/assets/SwirlBtn.png')),
            (490, 545), self.swirl, btnSound)
        )
        self.buttons.append(
            Button(
            Texture.from_surface(renderer,
                                pygame.image.load('src/assets/ShrinkBtn.png')),
            (610, 545), self.shrink, btnSound)
        )

    def openFile(self):
        """Create a Tk file dialog and cleanup when finished"""
        filePath = filedialog.askopenfilename(
            filetypes=self.imageFiles
        )
        
        if filePath == '':
            return

        self.image = Texture.from_surface(self.renderer, 
                            pygame.image.load(filePath))
        imageRect = self.image.get_rect()
        imageRect = imageRect.fit(self.rect)

        self.grid.update_image(self.image)

    def SaveImage(self):
        filePath = filedialog.asksaveasfilename(
            defaultextension='.png', initialfile='result.png', 
            filetypes=self.filetypes
        )

        if filePath == '': 
            return
        
        self.grid.save(filePath)


    def smudge(self):
        self.editor.toolIndex = 0

    def swirl(self):
        self.editor.toolIndex = 1
    
    def shrink(self):
        self.editor.toolIndex = 2

    def restart(self):
        self.editor.grid.reset_mesh()
    
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
        self.pixelspc = 20 #default
        self.pixelspc = self.get_settings()
        
        self.image = image

        self.grid = Grid(renderer, self.image, self.pixelspc, self.rect)

        self.minRadius = 16
        self.tools = [
            Smudge(renderer),
            Swirl(renderer),
            Shrink(renderer)
        ]
        self.toolIndex = 0

    def draw(self, renderer):
        #self.image.draw(dstrect=self.imageRect)
        self.grid.draw(renderer)

        tool = self.tools[self.toolIndex]
        if self.rect.collidepoint(Mouse.position):
            Mouse.visible = False
        else:
            tool.selected = False
        tool.update(self.grid.mesh)
        tool.draw(renderer)
        tool.selected = True

    def handle_event(self, event):
        if event.type == MOUSEWHEEL:
            Tool.radius += event.y
            if Tool.radius <= self.minRadius:
                Tool.radius = self.minRadius

        self.tools[self.toolIndex].handle_event(event)

        self.grid.handle_event(event)

    def get_settings(self):
        settings = {'PixelsPerPoint': self.pixelspc}

        if path.isfile('settings.json'):
            with open('settings.json', 'r') as config:
                settings = json.load(config)
                self.pixelspc = settings['PixelsPerPoint']
        else:
            with open('settings.json', 'w') as config:
                json.dump(settings, config)

        return self.pixelspc
        
        