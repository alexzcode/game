from pickle import TRUE
from ursina import *
from perlin_noise import *
from random import uniform
from random import randint
from ursina.prefabs.first_person_controller import FirstPersonController
noise = PerlinNoise(octaves=2, seed=2123)
flat = input('Is world flat? (y/n)\n\n')
day = input('Is Day time? (y/n)\n\n')

app = Ursina()
currentItem = 1
player = FirstPersonController()


def update():
    global currentItem
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
    if held_keys['1']:
        currentItem = 1
    if held_keys['2']:
        currentItem = 2
    if held_keys['3']:
        currentItem = 3
    if held_keys['4']:
        currentItem = 4
    if held_keys['5']:
        currentItem = 5


class Block(Button):
    def __init__(self, position=(0, 0, 0), texture='assets/grass.png'):
        super().__init__(
            parent=scene,
            position=position,
            model='cube',
            texture=texture,
            color=color.color(0, 0, random.uniform(0.9, 1)),
            highlight_color=color.gray)

    def input(self, key):
        if self.hovered:
            if key == 'right mouse down':
                if currentItem == 1:
                    block = Block(position=self.position+mouse.normal,
                                  texture='assets/grass.png')
                if currentItem == 2:
                    block = Block(position=self.position+mouse.normal,
                                  texture='assets/wood.png')
                if currentItem == 3:
                    block = Block(position=self.position+mouse.normal,
                                  texture='assets/stone.png')
                if currentItem == 4:
                    block = Block(position=self.position+mouse.normal,
                                  texture='assets/custom.png')
                if currentItem == 5:
                    block = Block(position=self.position+mouse.normal,
                                  texture='assets/fire1.png')

                    def update():
                        block.texture = 'assets/fire1.png'
                        block.texture = 'assets/fire2.png'

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


if day == 'y':
    sky = Entity(parent=scene, model='sphere',
                 texture='assets/day.jpeg',
                 scale=150,
                 double_sided=True)
elif day == 'n':
    sky = Entity(parent=scene, model='sphere',
                 texture='assets/night.jpeg',
                 scale=150,
                 double_sided=True)
sky.visible = TRUE
app.run()
