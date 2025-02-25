from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController

#app = Ursina()
#ground = Entity(scale=(15, 1, 40), y=-1, texture="white_cube", collider="box", model="cube")

class Player(FirstPersonController):
    def __init__(self, hp, dmg):
       super().__init__()
       self.health = hp
       self.damage = dmg

class berserker(Player):
    def __init__(self):
        super().__init__(150,30)
        
yo=Player(100,20)
#def input(key):
#    if key == 'q':
#        app.quit
#app.run()