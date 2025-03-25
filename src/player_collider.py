from ursina import *
from time import *

class player_collider(Entity):
    def __init__(self, parent):
        super().__init__(model = "quad", color = color.white, position = parent.position + [0,parent.scale[2],0] + parent.attack_range*parent.forward, rotation = parent.rotation + [-parent.camera_pivot.rotation_z, -parent.camera_pivot.rotation_y, -parent.camera_pivot.rotation_x] + [0,90,0], scale=[parent.attack_range,parent.scale[2]])
        self.damage = parent.damage

