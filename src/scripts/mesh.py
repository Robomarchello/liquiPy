import numpy
from .mouse import Mouse
from pygame import Vector2


class Grid:
    def __init__(self, rect, image, cells, pixelspc, bounds):
        #pixels per cell
        self.pixelspc = pixelspc
        xPoses = numpy.linspace(0, rect.width, cells[0])
        yPoses = numpy.linspace(0, rect.height, cells[1])

        allX = numpy.tile(xPoses, cells[1])
        allY = numpy.repeat(yPoses, cells[0])
        self.mesh = numpy.vstack((allX, allY)).T
        self.mesh += rect.topleft

        self.cells = cells

        self.mesh2d = self.mesh.reshape(
            (self.cells[0], self.cells[1], 2)
        )

        self.TriangleUV = numpy.subtract(self.mesh2d, rect.topleft)
        self.TriangleUV = numpy.divide(self.TriangleUV, rect.size)

        self.rect = rect
        self.image = image

        self.bounds = bounds

    def draw(self, renderer):
        renderer.draw_color = (255, 0, 0, 255)

        for y, row in enumerate(self.mesh2d):
            for x, point in enumerate(row):
                renderer.draw_point(point)

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

                        self.image.draw_quad(triangle[0], triangle[1], triangle[2], triangle[3],
                                        triangleUV[0], triangleUV[1], triangleUV[2], triangleUV[3])



    def update_mesh(self):
        pass

    def reset_mesh(self):
        pass

    def handle_event(self):
        pass