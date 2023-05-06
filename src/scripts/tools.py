from .mouse import Mouse


class Tool:
    def __init__(self, radius):
        self.position = Mouse.position
        self.PrevPos = self.position.copy()

        self.radius = radius
        self.active = False
        
    def draw(self, renderer):
        pass


class Smudge(Tool):
    def __init__(self, radius):
        super(radius).__init__()

    def update(self, mesh):
        if self.active:
            pass