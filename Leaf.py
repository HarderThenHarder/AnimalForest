"""
@author: P_k_y
"""
from GameEntity import GameEntity


class Leaf(GameEntity):

    def __init__(self, world, image):
        GameEntity.__init__(self, world, "leaf", image)

