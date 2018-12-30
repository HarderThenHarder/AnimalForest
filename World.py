
class World:
    def __init__(self, bg_img):
        self.entity_group = {}
        self.entity_id = 0
        self.bg_img = bg_img

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

    def render(self, surface):
        surface.blit(self.bg_img, (0, 0))
        for entity in self.entity_group:
            entity.render(surface)


