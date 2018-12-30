import Vector2
from StateMachine import StateMachine


class GameEntity:
    def __init__(self, name, world, image):
        self.world = world
        self.name = name
        self.image = image
        self.speed = 0
        self.location = Vector2(0, 0)
        self.destination = Vector2(0, 0)
        self.mind = StateMachine()

    def render(self, surface):
        x, y = self.location
        w, h = self.image.get_size()
        surface.blit(self.image, (x - w / 2, y - h / 2))

    def process(self, time_passed):
        self.mind.do_think()
        if self.destination != self.location:
            vec_to_destination = self.destination - self.location
            distance_to_destination = abs(vec_to_destination)
            heading = vec_to_destination.normalization()
            shifting_distance = min(distance_to_destination, self.speed * time_passed)
            self.location += heading * shifting_distance
