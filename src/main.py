from ursina import *
import player
import enemy
import map

app = Ursina()
#ground = Entity(scale=(15, 1, 15), y=-1, texture="grass", collider="box", model="cube")
mapa = map.map(50)
yo = player.berserker()
enoemigo1 = enemy.zombie(yo)





def input(key):
    if key == 'q':
        app.quit()
app.run()