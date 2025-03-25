from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController
import player_collider
"""
self.health es la vida del player
self.damage es el daño que hace el player
self.speed es la velocidad del player
self.jump_height es la altura del salto del player
self.gravity es la gravedad del player
self.jump_up_duration es la duración del salto hacia arriba del player, porque la gravedad solo afecta a la bajada
self.healthbar es el texto que muestra la vida del player en pantalla

la función takeDamage recibe un valor damage(el que tenga la hitbox del enemigo),
le resta ese valor a la vida del player y actualiza el texto de la vida en pantalla

los valores de hp, dmg, spd, jmp y g son los valores iniciales de la clase Player y los valores de berserker son sus correspondientes clases

"""

class Player(FirstPersonController):
    def __init__(self, hp, dmg, spd, jmp, g, r):
       super().__init__()
       self.health = hp
       self.damage = dmg
       self.speed = spd
       self.jump_height = jmp
       self.gravity = g
       self.jump_up_duration = 1
       self.attack_range = r
       self.healthbar = Text(text=self.health, position=(-0.85, -0.4), scale=2, color=color.red)
    def takeDamage(self, damage):
        self.health -= damage
        self.healthbar.text = self.health
    def input(self,key):
        if key== "left mouse down":
            attack=player_collider.player_collider(self)


class berserker(Player):
    def __init__(self):
        super().__init__(150,30, 5, 3, 1, 10)
        
        

