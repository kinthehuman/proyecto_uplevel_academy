from ursina import *
import time

class enemy(Entity):
    def __init__(self, hp, dmg, speed, player, attack_range):
        super().__init__(model="cube",color=color.red, collider="box")
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
        else:
            self.attack()


class zombie(enemy):
    def __init__(self, player):
        super().__init__(100, 20, 1, player,1)

    def attack(self):
        self.look_at(self.player.position)
        # colider_zombie = enemy_collider.enemy_collider(self, "enemy")
        hit_info = boxcast(origin= self.position, direction=self.forward, distance=self.attack_range, thickness=(self.scale[2],0.1), traverse_target=self.player)
        if(hit_info):
            self.player.takeDamage(self.damage)
    
    def update(self):
        super().update()
