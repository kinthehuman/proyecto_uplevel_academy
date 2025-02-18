from ursina import *

class player(Entity):
    def __init__(hp, dmg):
        super().__init__(model="cube",color="green")
        self.health = hp
        self.damage = dmg
