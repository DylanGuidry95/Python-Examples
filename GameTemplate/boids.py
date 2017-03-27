from agent import Agent
from gameobject import GameObject
import random
from constants import *
from vector import Vector2

class Flocking(GameObject):
    def __init__(self, numboids):
        self.numboids = numboids
        self.boids = []
        self.createboids()
        self.renderer = None

    def createboids(self):
        count = 0
        while count < self.numboids:
            self.boids.append(Agent(count))
            self.boids[count].transform.globalposition = (
                Vector2(random.randint(-SCREEN_WIDTH, SCREEN_WIDTH),
                        random.randint(-SCREEN_HEIGHT, SCREEN_HEIGHT)))

    def update(self, deltatime):
        for boid in self.boids:
            boid.velocity = Vector2.add(boid.velocity, self.rule1(boid))
            boid.transform.globalposition = Vector2.add(boid.transform.globalposition,
                                                        boid.velocity)


    def rule1(self, boid):
        percivedcenter = Vector2(0, 0)
        for other in self.boids:
            if other.name != boid.name:
                percivedcenter = percivedcenter + other.transform.globalposition
        return percivedcenter / (self.numboids - 1)
        