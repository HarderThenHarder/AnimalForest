from State import State
from random import randint
from Vector2 import Vector2


class AntStateExploring(State):
    def __init__(self, ant):
        State.__init__(self, "exploring")
        self.ant = ant
        self.WIDTH_HEIGHT = self.ant.world.WIDTH_HEIGHT

    def random_destination(self):
        w, h = self.WIDTH_HEIGHT
        self.ant.destination = Vector2(randint(0, w), randint(0, h))

    def do_action(self):
        # 5% probability to change NEW DESTINATION
        if randint(1, 20) == 1:
            self.random_destination()

    def check_condition(self):
        # seeking condition
        leaf = self.ant.world.get_near_entity(self.ant.location, "leaf")
        if leaf:
            self.ant.leaf_id = leaf.id
            return "seeking"
        # hunting condition
        spider = self.ant.world.get_near_entity(self.ant.world.NEST_location, "spider", self.ant.world.NEST_R)
        if spider:
            self.ant.spider_id = spider.id
            return "hunting"
        # No state transfer
        return None

    def entry_action(self):
        self.ant.speed = 120 + randint(-30, 30)
        self.random_destination()


class AntStateSeeking(State):

    def __init__(self, ant):
        State.__init__(self, "seeking")
        self.ant = ant

    def check_condition(self):
        leaf = self.ant.world.get_entity(self.ant.leaf_id)
        if leaf is None:
            return "exploring"
        elif self.ant.location.get_distance_to(leaf.location) < 5.0:
            self.ant.carry(leaf.img)
            self.ant.world.remove_entity(leaf.id)
            return "delivering"
        return None

    def entry_action(self):
        leaf = self.ant.world.get_entity(self.ant.leaf_id)
        if leaf:
            self.ant.destination = leaf.location
            self.ant.speed = 160 + randint(-20, 20)


class AntStateHunting:
    pass


class AntStateDelivering:
    pass
