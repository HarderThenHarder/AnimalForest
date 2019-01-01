from GameEntity import GameEntity
from AntState import *


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

    def render(self, surface):
        # Base Class Method Render
        GameEntity.render(self, surface)
        # Extra render method "Draw Carry Image"
        if self.carry_img:
            x, y = self.location
            w, h = self.carry_img.get_size()
            surface.blit(self.carry_img, (x - w / 2, y - h / 2))

    def carry(self, img):
        self.carry_img = img

    def drop(self, surface):
        x, y = self.location
        w, h = self.carry_img.get_size()
        surface.blit(self.carry_img, (x - w / 2, y - h / 2))
        self.carry_img = None




