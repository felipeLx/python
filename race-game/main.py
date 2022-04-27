from cars import *
from pilots import *
from roads import *

import pygame 
import time
import math
from utils import scale_img, blit_rotate_center

# variable of the track
GRASS = scale_img(pygame.image.load('img/grass.jpg'), 2.5)
TRACK = scale_img(pygame.image.load('img/track.png'), 0.8)
HEDGE = scale_img(pygame.image.load('img/track-border.png'), 0.8)
FINISH = pygame.image.load('img/finish.png')

# variable of the car
BARR = scale_img(pygame.image.load('pilots/barr.png'), 0.5)
FITT = scale_img(pygame.image.load('pilots/fitt.png'), 0.5)
MASS = scale_img(pygame.image.load('pilots/mass.png'), 0.5)
PIQ = scale_img(pygame.image.load('pilots/piq.png'), 0.5)
SEN = scale_img(pygame.image.load('pilots/sen.png'), 0.5)

# variable of the window
WIDTH, HEIGTH = TRACK.get_width(), TRACK.get_height()
WIN = pygame.display.set_mode((WIDTH+40, HEIGTH+40))
pygame.display.set_caption('Brasil Racing')
FPS = 60

# draw the pilots
class AbstractCar: # not to be initiate directly
    def __init__(self, max_vel, rotation_vel):
        self.img = self.IMG
        self.max_vel = max_vel
        self.rotation_vel = rotation_vel
        self.vel = 0
        self.angle = 0
        self.x, self.y = self.START_POS
        self.acc = 0.1
    
    def rotate(self, left=False, right=False):
        if left:
            self.angle += self.rotation_vel
        elif right:
            self.angle -= self.rotation_vel
        else:
            pass
    
    def draw(self, win):
        blit_rotate_center(win, self.img, (self.x, self.y), self.angle)

    def move_forward(self):
        self.vel = min(self.vel + self.acc, self.max_vel)
        self.move()

    def move_backward(self):
        self.vel = max(self.vel - self.acc, -self.max_vel/2)
        self.move()

    def move(self):
        self.y -= self.vel * math.cos(math.radians(self.angle))
        self.x -= self.vel * math.sin(math.radians(self.angle))
    
    
# player class
class Player(AbstractCar):
    IMG = SEN
    START_POS = (150, 200)

    def reduce_speed(self):
        # self.acc = 0
        self.vel = max(self.vel - self.acc/2, 0)
        self.move()

# draw the objects
def draw(win, images, player):
    for img, pos in images:
        win.blit(img, pos)
    player.draw(win)
    pygame.display.update() # code will run every single time to display the content

# move player
def move_player(player):
    keys = pygame.key.get_pressed()
    moved = False

    if keys[pygame.K_a]:
        player.rotate(left=True)
    if keys[pygame.K_d]:
        player.rotate(right=True)
    if keys[pygame.K_w]:
        moved = True
        player.move_forward()
    if keys[pygame.K_s]:
        moved = True
        player.move_backward()
    if not moved:
        player.reduce_speed()

# define race loop
race = True
clock = pygame.time.Clock()
images = [(GRASS, (0,0)), (TRACK, (0,0)), (HEDGE, (0,0)), (FINISH, (110,180))]
player = Player(5, 4)

while race:
    clock.tick(FPS) # the loop can't run faster than 60 frame per second

    # blit to show the objects on screen / putting on order of later appear
    draw(WIN, images, player)
    # blit the pilots/cars
    WIN.blit(BARR, (10,0))
    WIN.blit(FITT, (30,0))
    WIN.blit(MASS, (60,0))
    WIN.blit(PIQ, (90,0))
    WIN.blit(SEN, (120,0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            race = False
            break
    
    move_player(player)
pygame.quit()