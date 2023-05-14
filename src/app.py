import asyncio
import pygame
from pygame.locals import *
from pygame._sdl2.video import Window, Renderer, Texture
from src.scripts.parts import ToolBar, Editor
from src.scripts.mouse import Mouse


pygame.init()


class App():
    def __init__(self, ScreenSize, caption, fps):
        self.ScreenSize = ScreenSize

        icon = pygame.image.load('src/assets/icon.png')
        
        self.window = Window(caption, ScreenSize)
        self.window.set_icon(icon)
        self.renderer = Renderer(self.window)

        self.dummy = Texture.from_surface(
            self.renderer,
            pygame.image.load('src/assets/dummy.png'))

        self.Editor = Editor(self.renderer, self.dummy)
        self.ToolBar = ToolBar(self.renderer, self.Editor.grid, self.Editor)

        self.event_handlers = [Mouse, self.ToolBar, self.Editor]

        self.clock = pygame.time.Clock()
        self.fps = fps

    async def loop(self):
        renderer = self.renderer
        while True:
            self.clock.tick(self.fps)
            
            self.handle_events()
            Mouse.update()

            renderer.draw_color = (49, 51, 56, 255) # Set the draw color
            renderer.clear() # Fill the screen with the set draw color
            
            self.Editor.draw(renderer)
            self.ToolBar.draw(renderer)
            
            renderer.present() # Update the screen

            await asyncio.sleep(0)

    def handle_events(self):
        #event handling
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                raise SystemExit
            
            if event.type == KEYDOWN:
                if event.key == K_f:
                    print(self.clock.get_fps())
        
            for event_handler in self.event_handlers:
                event_handler.handle_event(event)
