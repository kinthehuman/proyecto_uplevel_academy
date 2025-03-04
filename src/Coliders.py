from ursina import *
from time import *

class Colider(Entity):
    def __init__(self, damage, source, pposition, porientation, dimensions):
        super().__init__(model = "square", color = color.white, position = pposition, rotation = porientation, scale=dimensions)
        self.damage = damage
        self.source = source

