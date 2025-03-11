from ursina import *

class map(Entity):
    def shape (length):
        bottom = Entity(scale=length, y=-1, texture="grass", collider="box", model="cube")
        wall_x = Entity(scale=(bottom.scale[1], 1, 15), x=-bottom.scale[1]/2, y=-1, collider="box", model="cube")