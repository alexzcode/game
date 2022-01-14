from ursina import *
from perlin_noise import *
from random import *
from ursina.prefabs.first_person_controller import FirstPersonController
noise = PerlinNoise(octaves=2,seed=2123)

app = Ursina()

player = FirstPersonController()

def update():
	if player.x > 35:
		player.x = 0
	if player.x < 0:
		player.x = 34.9
	if player.z > 35:
		player.z = 0
	if player.z < 0:
		player.z = 34.9
	if player.y < -0.5:
		player.y = 10
		player.x = 17.5
		player.z = 17.5
	if held_keys['left mouse']:
		NewBlock = Entity(position = (player.x+1,player.y,player.z+1),model='cube',texture='assets/grass.png',parent=scene,collider='box')

for z in range(35):
	for x in range(35):
		y = noise([x/8,z/8])
		block = Entity(position=(x,y,z),model='cube',collider='cube',texture='assets/grass.png')
		player.position = (x/2,10,z/2)

app.run()