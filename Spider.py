"""
@author: P_k_y
"""
from GameEntity import  GameEntity
import pygame
from random import randint


class Spider(GameEntity):

    def __init__(self, world, image):
        GameEntity.__init__(self, "spider", world, image)
        self.dead_image = pygame.transform.flip(image, 0, 1)
        self.hp = 25
        self.speed = 50.0 + randint(-20, 20)

    def bitten(self):
        self.hp -= 1
        if self.hp <= 0:
            self.speed = 0.
            self.image = self.dead_image
        self.speed = 140.

    def render(self, surface):
        GameEntity.render(self, surface)
        x, y = self.location
        w, h = self.image.get_size()
        bar_x = x - 12
        bar_y = y + h / 2
        surface.fill((255, 0, 0), (bar_x, bar_y, 25, 4))
        surface.fill((0, 255, 0), (bar_x, bar_y, self.hp, 4))

    def process(self, time_passed):
        x, y = self.location.x, self.location.y
        if not (0 < x < self.world.WIDTH_HEIGHT[0] + 2 and 0 < self.world.WIDTH_HEIGHT[1] + 2):
            self.world.remove_entity(self.id)
            return
        GameEntity.process(self, time_passed)



