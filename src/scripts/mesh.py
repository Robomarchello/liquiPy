import numpy
from .mouse import Mouse
from time import perf_counter
import pygame


class Grid:
    def __init__(self, renderer, image, pixelspc, bounds):
        self.renderer = renderer
        self.image = image
        self.pixelspc = pixelspc
        self.bounds = bounds

        #pixels per cell
        
        self.rect = image.get_rect().fit(self.bounds)

        self.cells = [
            self.rect.width // self.pixelspc,
            self.rect.height // self.pixelspc
        ]

        xPoses = numpy.linspace(0, self.rect.width, self.cells[0])
        yPoses = numpy.linspace(0, self.rect.height, self.cells[1])

        allX = numpy.tile(xPoses, self.cells[1])
        allY = numpy.repeat(yPoses, self.cells[0])
        self.mesh = numpy.vstack((allX, allY)).T
        self.mesh += self.rect.topleft

        self.mesh2d = self.mesh.reshape(
            (self.cells[0], self.cells[1], 2)
        )

        self.TriangleUV = numpy.subtract(self.mesh2d, self.rect.topleft)
        self.TriangleUV = numpy.divide(self.TriangleUV, self.rect.size)        

    def draw(self, renderer):
        renderer.draw_color = (255, 0, 0, 255)

        for y, row in enumerate(self.mesh2d):
            for x, point in enumerate(row):
                if x < self.cells[0] - 1:
                    if y < self.cells[1] - 1:
                       
                        triangle = [
                            point,
                            self.mesh2d[y][x + 1],
                            self.mesh2d[y + 1][x + 1], 
                            self.mesh2d[y + 1][x]
                        ]
                        triangleUV = [
                            self.TriangleUV[y][x],
                            self.TriangleUV[y][x + 1],
                            self.TriangleUV[y + 1][x + 1],
                            self.TriangleUV[y + 1][x]
                        ]
                        
                        self.image.draw_quad(
                            triangle[0], triangle[1], triangle[2], triangle[3],
                            triangleUV[0], triangleUV[1], triangleUV[2], triangleUV[3]
                            )
                        
                renderer.draw_point(point)
                        

    def save(self):
        self.renderer.draw_color = (0, 0, 0, 255)
        self.renderer.clear()

        for y, row in enumerate(self.mesh2d):
            for x, point in enumerate(row):
                #renderer.draw_point(point)

                if x < self.cells[0] - 1:
                    if y < self.cells[1] - 1:
                       
                        triangle = [
                            point,
                            self.mesh2d[y][x + 1],
                            self.mesh2d[y + 1][x + 1], 
                            self.mesh2d[y + 1][x]
                        ]
                        triangleUV = [
                            self.TriangleUV[y][x],
                            self.TriangleUV[y][x + 1],
                            self.TriangleUV[y + 1][x + 1],
                            self.TriangleUV[y + 1][x]
                        ]
                        
                        self.image.draw_quad(
                            triangle[0], triangle[1], triangle[2], triangle[3],
                            triangleUV[0], triangleUV[1], triangleUV[2], triangleUV[3]
                            )
                        
        surf = self.renderer.to_surface()
        pygame.image.save(surf, 'saved.png')

    def update_image(self, image):
        self.rect = image.get_rect().fit(self.bounds)

        self.cells = [
            self.rect.width // self.pixelspc,
            self.rect.height // self.pixelspc
        ]

        xPoses = numpy.linspace(0, self.rect.width, self.cells[0])
        yPoses = numpy.linspace(0, self.rect.height, self.cells[1])

        allX = numpy.tile(xPoses, self.cells[1])
        allY = numpy.repeat(yPoses, self.cells[0])
        self.mesh = numpy.vstack((allX, allY)).T
        self.mesh += self.rect.topleft

        self.mesh2d = self.mesh.reshape(
            (self.cells[0], self.cells[1], 2)
        )

        self.TriangleUV = numpy.subtract(self.mesh2d, self.rect.topleft)
        self.TriangleUV = numpy.divide(self.TriangleUV, self.rect.size)

    def reset_mesh(self):
        pass

    def handle_event(self):
        pass