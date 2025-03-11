from Vector2 import Vector2
from constants import *
from math import pi
from random import uniform
import pygame


class Boid:

    def __init__(self, position):
        self.pos = position
        self.vel = Vector2(1, 0).rotate(uniform(0, 2*pi))
        self.accel = Vector2(0, 0)
        # Defined pointing to 0 radians
        self.tPoints = [Vector2(1.5, 0) * BOID_SIZE_MULT, Vector2(-1, -1) * BOID_SIZE_MULT, Vector2(-1, 1) * BOID_SIZE_MULT]

    def guide(self, flock, mousePos, mouseAvoid):
        self.accel = Vector2(0, 0)
        sepSum = Vector2(0, 0)
        alignSum = Vector2(0, 0)
        cohSum = Vector2(0, 0)
        nInSepRange = 0
        nInAlignRange = 0
        nInCohRange = 0

        for boid in flock:
            dist = (self.pos - boid.pos).length()
            if dist > 0 and dist < SEPERATION_RANGE:
                sepSum = sepSum + ((self.pos - boid.pos).normalize() / dist)
                nInSepRange += 1
            if dist > 0 and dist < ALIGNMENT_RANGE:
                alignSum = alignSum + boid.vel
                nInAlignRange += 1
            if dist > 0 and dist < COHESION_RANGE:
                cohSum = cohSum + boid.pos
                nInCohRange += 1
        if nInSepRange > 0:
            self.target(sepSum, SEPERATION_CONSTANT)
        if nInAlignRange > 0:
            self.target(alignSum, ALIGNMENT_CONSTANT)
        if nInCohRange > 0:
            cohSum = cohSum / nInCohRange - self.pos
            self.target(cohSum, COHESION_CONSTANT)
        if mouseAvoid:
            mouseDiff = (mousePos - self.pos)
            if mouseDiff.length() < MOUSE_AVOID_RANGE:
                self.target(mouseDiff, MOUSE_AVOID_CONSTANT)

    def target(self, vector, constant):
        self.accel = self.accel + (vector.normalize() * VELOCITY_LIMIT - self.vel).limit(FORCE_LIMIT) * constant

    def update(self):
        projectedVel = (self.vel + self.accel.rotate(uniform(-RANDOM_TURN_LIMIT, RANDOM_TURN_LIMIT))).limit(VELOCITY_LIMIT)
        projectedPos = self.pos + projectedVel
        if projectedPos.x < SCREEN_OFFSET_X and self.accel.x < 0 or projectedPos.x > WIDTH - SCREEN_OFFSET_X and self.accel.x > 0:
            self.accel.x = -self.accel.x
        if projectedPos.y < SCREEN_OFFSET_Y and self.accel.y < 0 or projectedPos.y > HEIGHT - SCREEN_OFFSET_Y and self.accel.y > 0:
            self.accel.y = -self.accel.y
        self.vel = (self.vel + self.accel.rotate(uniform(-RANDOM_TURN_LIMIT, RANDOM_TURN_LIMIT))).limit(VELOCITY_LIMIT)
        self.pos.x = (self.pos.x + self.vel.x) % WIDTH
        self.pos.y = (self.pos.y + self.vel.y) % HEIGHT

    def display(self, screen, color):
        heading = self.vel.angle()
        tPoints = []
        for i in range(len(self.tPoints)):
            tPoints.append(self.tPoints[i].rotate(heading) + self.pos)
        pygame.draw.polygon(screen, color, [(tPoints[0].x, tPoints[0].y), (tPoints[1].x, tPoints[1].y), (tPoints[2].x, tPoints[2].y)])