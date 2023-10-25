import pygame, random, math
from pygame.locals import *

'''The engine was inspired by DaFluffyPotate, go subscribe to him: https://www.youtube.com/@DaFluffyPotato'''

def collision_test(object, object_list):
    collisions = []
    for obj in object_list:
        if obj.rect.colliderect(object):
            collisions.append(obj.rect)
    return collisions


class PhysicsEntity:
    'Physics'

    def __init__(self, e_type, pos, size):
        self.x, self.y = pos
        self.width, self.height = size
        self.type = e_type
        self.movement_step = 2
    
    def rect(self):
        return pygame.Rect(self.x, self.y, self.width, self.height)
    
    def update(self, movement):
        
        #entity_rect = self.rect()
        self.x += (movement['right'] - movement['left']) * self.movement_step

        #entity_rect = self.rect()
        self.y += (movement['down'] - movement['up']) * self.movement_step

    def render(self, surf, color):
        pygame.draw.rect(surf, color, self.rect())
    
    def getObjData(self):
        return {'x': self.x, 'y': self.y, 'width': self.width, 'height': self.height, 'type': self.type}