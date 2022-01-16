from re import S
from turtle import position
from ursina import *
from perlin_noise import *
from random import *
from ursina.prefabs.first_person_controller import FirstPersonController
noise = PerlinNoise(octaves=2, seed=2123)
i = 0
playerWood = 0
flat = input('Is world flat? (y/n)\n\n\n\n')


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


class Block(Button):
    def __init__(self, position=(0, 0, 0), texture='assets/grass.png'):
        super().__init__(
            parent=scene,
            position=position,
            model='cube',
            texture=texture,
            color=color.white,
            highlight_color=color.gray)

    def input(self, key):
        if self.hovered:
            if key == 'right mouse down':
                block = Block(position=self.position+mouse.normal,
                              texture='assets/wood.png')

            if key == 'left mouse down':
                destroy(self)


for z in range(35):
    for x in range(35):
        if flat == 'y':
            block = Block(position=(x, 0, z), texture='assets/grass.png')
        elif flat == 'n':
            y = noise([x/8, z/8])
            block = Block(position=(x, y, z), texture='assets/grass.png')


class makeTree():
    treeBark = Entity(parent=scene,
                      model='cube',
                      position=(randint(0, 35),
                                0,
                                randint(0, 35)),
                      texture='assets/wood.png',
                      scale_y=10,
                      collider='box')
    treeLeaves = Entity(parent=scene,
                        model='assets/tree.obj',
                        position=(treeBark.x,
                                  treeBark.scale_y-4.5,
                                  treeBark.z),
                        texture='assets/grass.png',
                        collider='mesh',
                        scale=1)


makeTree()

Sky()
app.run()
