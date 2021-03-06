import pygame
from pygame.locals import *
from Ant import Ant
from Leaf import Leaf
from Spider import Spider
from Vector2 import Vector2
from World import World
from pygame.time import Clock
from sys import exit
from random import randint


def main():
    # init
    pygame.init()
    WIDTH_HEIGHT = [1920, 1080]
    screen = pygame.display.set_mode(WIDTH_HEIGHT, RESIZABLE, 32)
    clock = Clock()
    pygame.display.set_caption("AnimalForest v1.0")

    # Constant Value
    ANT_NUMBER = 10

    # Create world
    world_img = pygame.image.load(r"img\world2.png")
    world = World(world_img, WIDTH_HEIGHT)

    # Create animal img
    ant_img = pygame.image.load(r"img\ant.png")
    leaf_img = pygame.image.load(r"img\leaf.png")
    spider_img = pygame.image.load(r"img\spider.png")
    pygame.display.set_icon(ant_img)

    # Create ant Object
    for i in range(ANT_NUMBER):
        ant = Ant(world, ant_img)
        ant.location = world.NEST_location
        ant.brain.set_state("exploring")
        world.add_entity(ant)

    while True:
        time_passed = clock.tick(30)

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                exit()

            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    pygame.quit()
                    exit()

        if randint(1, 20) == 1:
            leaf = Leaf(world, leaf_img)
            leaf.location = Vector2(randint(0, WIDTH_HEIGHT[0]), randint(0, WIDTH_HEIGHT[1]))
            world.add_entity(leaf)

        if randint(1, 300) == 1:
            spider = Spider(world, spider_img)
            spider.location = Vector2(randint(0, WIDTH_HEIGHT[0]), 0)
            spider.destination = Vector2(randint(0, WIDTH_HEIGHT[0]), randint(0, WIDTH_HEIGHT[1]))
            world.add_entity(spider)

        world.process(time_passed)
        world.render(screen)

        pygame.display.update()


if __name__ == '__main__':
    main()
