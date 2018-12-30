from GameEntity import GameEntity
from State import *


class Ant(GameEntity):

    def __init__(self, world, image):
        GameEntity.__init__(self, "ant", world, image)
        state_exploring = AntStateExploring(self)
        state_seeking = AntStateSeeking(self)
        state_hunting = AntStateHunting(self)
        state_delivering = AntStateDelivering(self)
        self.brain.add_state(state_exploring)
        self.brain.add_state(state_seeking)
        self.brain.add_state(state_hunting)
        self.brain.add_state(state_delivering)
        self.carry_img = None

