from ursina import *
from time import *

class enemy(Entity):
    def __init__(hp, dmg, speed, self, player):
        super().__init__(model="cube",color=color.red)
        self.health = hp
        self.damage = dmg
        self.speed = speed
        self.player = player

    def move(self):
        self.look_at(self.player.position)
        self.forward * self.speed*time.dt
    
    def update(self):
        if(distance(self, self.player)>2):
            self.move()


class zombie(enemy):
    def __init__():
        super().__init__(health = 100, dmg = 20, speed = 3)