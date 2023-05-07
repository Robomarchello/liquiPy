import numpy
from .mouse import Mouse


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

        self.rect = rect
        self.image = image

        self.bounds = bounds

    def draw(self, renderer):
        renderer.draw_color = (255, 0, 0, 255)
        for position in self.mesh:
            renderer.draw_point(position)

    def update_mesh(self):
        pass

    def reset_mesh(self):
        pass

    def handle_event(self):
        pass