import random
import time
import pygame
import numpy
from pygame.locals import *
from pygame.color import *
import pymunk
from pymunk import Vec2d
import pymunk.pygame_util
import pandas as pd
import csv
import matplotlib.pyplot as plt

# Some general variables -- you don't need to change any of these
N_BLOCKS = 6 # How many blocks will fall?
BLOCK_SIZE = 20 # How big are the blocks?
deltaY     = 35 # How far spaced out vertically are they?
xSD        = 30.0 # What is the SD for their x-locations?
FPS = 30. # how many frames per second do we run?
BLOCK_MASS = 1.0
BLOCK_FRICTION = 1.0
FLOOR = 100
RUN_TIME = 10.0 # Time in seconds that we will run a simulation for
STEPS_PER_FRAME = 5.0 # Do not change this
WIDTH = 600 # Screen dimensions -- don't change
HEIGHT = 600

class BlockTower:
    # Implement a class to show/simulate blocks falling via pymunk
    # Note: this code has been modified from the pymunk pyramid demo

    def __init__(self, positions):
        # The intializer takes a list of x-positions for blocks; their height is set
        # by the code here.
        assert(len(positions)==N_BLOCKS) # can't give more than N_BLOCKS since we need to draw them

        self.positions = positions # store the positions of our blocks

        # Set up some pygame stuff
        self.running = True
        self.physics_running = False
        self.start_time = 0
        self.drawing = True
        self.w, self.h = WIDTH,HEIGHT
        self.screen = pygame.display.set_mode((self.w, self.h))
        self.clock = pygame.time.Clock()

        ### Init pymunk and create space
        self.space = pymunk.Space()
        self.space.gravity = (0.0, -900.0)
        self.space.sleep_time_threshold = 0.3

        self.floor = pymunk.Segment(self.space.static_body, (0, FLOOR), (self.w,FLOOR), 1.0)
        self.floor.friction = 1.0
        self.space.add(self.floor)

        # Draw each block and add it to the physics
        for i in range(N_BLOCKS):
            points = [(-BLOCK_SIZE, -BLOCK_SIZE), (-BLOCK_SIZE, BLOCK_SIZE), (BLOCK_SIZE,BLOCK_SIZE), (BLOCK_SIZE, -BLOCK_SIZE)]
            moment = pymunk.moment_for_poly(BLOCK_MASS, points, (0,0))
            body = pymunk.Body(BLOCK_MASS, moment)
            xpos = self.positions[i]
            ypos = FLOOR + (2*i+1) * deltaY
            body.position = Vec2d(xpos,ypos)
            shape = pymunk.Poly(body, points)
            if(i == N_BLOCKS-1):     # color the top
                shape.color = (1,0,0,1)
                self.target_block = shape # store the top one we are tracking
            shape.friction = 1
            self.space.add(body,shape)

        ### draw options for drawing
        self.draw_options = pymunk.pygame_util.DrawOptions(self.screen)

    def is_black_block_on_floor(self):
        # Returns true or false depending on whether the black block is on the bottom
        col = self.target_block.shapes_collide(self.floor) # this resturns a ContactPointSet
        return len(col.points) > 0

    def run_person(self):
        # Show a window where people can predict yes/no (y/n) for whether the black block hits the bottom.
        # After they respond, they can observe the physics.
        # Rteturns their prediction and whether the black block actually hit the floor

        prediction = None # what people predicted?

        # Call this to run a single simulation with the given positions
        while self.running and (time.time() - self.start_time) < RUN_TIME or self.start_time==0:
            for event in pygame.event.get():
                if event.type == QUIT:
                    self.running = False
                elif event.type == KEYDOWN and event.key == K_ESCAPE:
                    self.running = False
                elif event.type == KEYDOWN and (event.key == K_y or event.key==K_n):  ## This detects a space press and starts simulating
                    prediction = (event.key == K_y)
                    self.physics_running = True
                    self.start_time = time.time()  # remember the time that physics started running

            if self.physics_running:
                self.space.step(1.0 / FPS / STEPS_PER_FRAME)  ## conveera frames per second to internal clock tics -- don't change!

            if self.drawing:
                self.draw()

            self.clock.tick(FPS) # don't let this loop run faster than FPS
        return (prediction, self.is_black_block_on_floor())

    def simulate(self):
        # Just run a simulation, returning whether after 10s the black block hits the floor
        for s in range(int(FPS*5*RUN_TIME)): # run for 10s
            self.space.step(1.0 / FPS / STEPS_PER_FRAME) # run this many steps
        return self.is_black_block_on_floor()

    def draw(self):
        ### This gets called to draw the scene

        ### Clear the screen
        self.screen.fill(THECOLORS["white"])

        ### Draw space  with our given options
        self.space.debug_draw(self.draw_options)

        ### All done, lets flip the display, which will cause it to be displayed
        pygame.display.flip()
data=pd.read_csv("predictions.csv")

shape=int((data.shape[0]+2)/4)
print("shape:",shape)

SDD=[1,5,10,15,20,50,100]
fig = plt.figure()
ax=[None]*7
ax[0] = fig.add_subplot(241)
ax[1] = fig.add_subplot(242)
ax[2] = fig.add_subplot(243)
ax[3] = fig.add_subplot(244)
ax[4] = fig.add_subplot(245)
ax[5] = fig.add_subplot(246)
ax[6] = fig.add_subplot(247)
qq=-1
for SD in SDD:
    qq+=1
    acc = []
    pre = []
    for i in range(shape):
        r = 0
        pos = data.iloc[4 * i + 1, 0:6]
        positions = numpy.zeros(6)
        for j in range(100):
            for k in range(6):
                positions[k] = float(pos[k]) + numpy.random.normal(0, SD)
            demo = BlockTower(positions)
            if (demo.simulate() == True):
                r += 1
        acc.append(r / 100)
        pre.append(data.iloc[4 * i + 1, 7])
    pygame.quit()

    cluster = numpy.zeros(10)
    rr = numpy.zeros(10)
    for i in range(shape):
        if acc[i] == 1:
            if pre[i] == 'TRUE':
                cluster[9] += 1
            rr[9] += 1
        else:
            for j in range(10):
                if acc[i] < (j + 1) * 0.1:
                    if pre[i] == 'TRUE':
                        cluster[j] += 1
                    rr[j] += 1
                    break
    for i in range(10):
        if rr[i] == 0:
            cluster[i] = 0
        else:
            cluster[i] = cluster[i] / rr[i]
    sum2=0
    for i in range(10):
        sum2+=(abs(cluster[i]-i*0.1+0.05))*rr[i]
    print("SD:",SD,"sum:",sum2)
    ax[qq].set_title("SD: "+str(SD))
    ax[qq].plot(cluster)
    base=[m*0.1+0.05 for m in range(10)]
    ax[qq].plot(base,'r')
plt.show()