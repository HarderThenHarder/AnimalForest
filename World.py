from Vector2 import Vector2
import pygame


class World:
    def __init__(self, world_img, WIDTH_HEIGHT):
        self.entity_group = {}
        self.entity_id = 0
        self.WIDTH_HEIGHT = WIDTH_HEIGHT
        self.world_img = world_img
        self.NEST_R = 100
        self.NEST_location = Vector2(WIDTH_HEIGHT[0] / 2, WIDTH_HEIGHT[1] / 2)

    def add_entity(self, entity):
        self.entity_group[self.entity_id] = entity
        entity.id = self.entity_id
        self.entity_id += 1

    def remove_entity(self, entity_id):
        del self.entity_group[entity_id]

    def get_entity(self, entity_id):
        if entity_id in self.entity_group:
            return self.entity_group[entity_id]
        return None

    def process(self, time_passed):
        for entity in list(self.entity_group.values()):
            entity.process(time_passed)

    def render(self, surface):
        surface.blit(self.world_img, (0, 0))
        pygame.draw.circle(surface, (100, 100, 100), [int(self.NEST_location.x), int(self.NEST_location.y)], self.NEST_R, 2)
        for entity in self.entity_group.values():
            entity.render(surface)

    def get_near_entity(self, location, name, r=100):
        location = location.copy()
        for entity in self.entity_group.values():
            if entity.name == name:
                distance = abs(entity.location.copy() - location)
                if distance < r:
                    return entity
        return None

