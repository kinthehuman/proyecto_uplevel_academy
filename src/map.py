from ursina import *

class map(Entity):
    def __init__ (self, l):
        bottom = Entity(scale=(l, 1, l), y=-1, texture="grass", collider="box", model="cube")
        top = Entity(scale=(l,1,l), y=l-1, collider="box", model="cube")
        wall_1 = Entity(scale=(l, l, 1), z=-l/2,y=l/2-1, collider="box", model="cube")
        wall_2 = Entity(scale=(l, l, 1), z=+l/2,y=l/2-1, collider="box", model="cube")
        wall_3 = Entity(scale=(1, l, l), x=-l/2,y=l/2-1, collider="box", model="cube")
        wall_4 = Entity(scale=(1, l, l), x=l/2,y=l/2-1, collider="box", model="cube")
