import pygame
from math import cos , sin
from Utils import *
    
class Ray:
    def __init__(self, x, y, angle, screen, color):
        self.position = [x, y]
        self.angle = angle
        self.screen = screen

    def march(self, objects, collisions):
        counter = 0
        current_position = self.position
        pygame.draw.circle(self.screen, RED, self.position, 5)
        while counter < MAX_STEPS:
            record = 10000
            for object in objects:
                distance = object.SignedDistance(current_position)
                if distance < record:
                    record = distance

            if record < COLLISION_THESHOLD:
                collisions.insert(0, (current_position[0], current_position[1]))
                break

            x_step = current_position[0] + cos(self.angle) * record
            y_step = current_position[1] + sin(self.angle) * record

            pygame.draw.circle(self.screen, GREEN, (current_position[0], current_position[1]), abs(record), 1)
            pygame.draw.line(self.screen, WHITE, (current_position[0], current_position[1]), (x_step, y_step), 1)

            current_position[0] = x_step
            current_position[1] = y_step

            if (x_step < 0 or x_step > WIDTH or y_step < 0 or y_step > HEIGHT) or (current_position[0] < 0 or current_position[0] > WIDTH or current_position[1] < 0 or current_position[1] > HEIGHT): 
                break
            counter += 1

        pygame.display.update()
