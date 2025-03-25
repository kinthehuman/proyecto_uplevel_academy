from ursina import *
from time import *

class enemy_collider(Entity):
    def __init__(self, parent):
        super().__init__(model = "quad", color = color.white, position = parent.position + [0,parent.scale[2],0] + parent.attack_range/2*parent.forward, rotation = parent.rotation + [0,90,0], scale=[parent.attack_range,parent.scale[2]])
        self.damage = parent.damage

