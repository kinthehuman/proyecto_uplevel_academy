from ursina import *
import time
import Coliders

class enemy(Entity):
    def __init__(self, hp, dmg, speed, player, attack_range):
        super().__init__(model="cube",color=color.red)
        self.health = hp
        self.damage = dmg
        self.speed = speed
        self.player = player
        self.attack_range = attack_range

    #mirar al jugador y dirigirse a el
    def move(self,dt):
        self.look_at(self.player.position) 
        self.position += self.forward*self.speed*dt

    def attack(self):
        self.look_at(self.player.position)

    
    # si la distancia es mas grande del rango de ataque el enemigo se mueve al jugador y si no le ataca
    def update(self):
        if(distance(self, self.player) > self.attack_range):
            dt=time.dt
            self.move(dt)
        #else:
            #self.attack()


class zombie(enemy):
    def __init__(self, player):
        super().__init__(100, 20, 1, player,1)

    def attack(self):
        self.look_at(self.player.position)
        colider_zombie = Coliders.Colider(self.damage, "enemy", self.position, self.rotation, (self.scale[2], self.attack_range))
    
    def update(self):
        super().update()