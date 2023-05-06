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

        self.window = Window(caption, ScreenSize)
        self.renderer = Renderer(self.window)

        self.dummy = Texture.from_surface(
            self.renderer,
            pygame.image.load('src/assets/dummy.png'))

        self.ToolBar = ToolBar(self.renderer)
        self.Editor = Editor(self.dummy)

        self.event_handlers = [Mouse, self.ToolBar]

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
            
            self.ToolBar.draw(renderer)
            self.Editor.draw(renderer)
            
            renderer.present() # Update the screen

            await asyncio.sleep(0)

    def handle_events(self):
        #event handling
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                raise SystemExit
        
            for event_handler in self.event_handlers:
                event_handler.handle_event(event)
