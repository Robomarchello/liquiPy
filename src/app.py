import pygame
from pygame.locals import *
from pygame._sdl2.video import Window, Renderer
import asyncio

pygame.init()


class App():
    def __init__(self, ScreenSize, caption, fps):
        self.ScreenSize = ScreenSize
        
        #self.screen = pygame.display.set_mode(ScreenSize)
        #pygame.display.set_caption(caption)
        self.window = Window(caption, ScreenSize)
        self.renderer = Renderer(self.window)

        self.event_handlers = []

        self.clock = pygame.time.Clock()
        self.fps = fps

    async def loop(self):
        renderer = self.renderer
        while True:
            self.clock.tick(self.fps)

            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    raise SystemExit

                            
            renderer.draw_color = (49, 51, 56, 255) # Set the draw color
            renderer.clear() # Fill the screen with the set draw color
            
            #texture.draw_triangle((0, 500), mp, (500, 500), (0.0, 1.0), (0.5, 0.0), (1.0, 1.0))
            
            renderer.present() # Update the screen

            await asyncio.sleep(0)