from ursina import *
import player
import enemy

app = Ursina()
ground = Entity(scale=(15, 1, 15), y=-1, texture="grass", collider="box", model="cube")

yo = player.berserker()





def input(key):
    if key == 'q':
        app.quit
app.run()