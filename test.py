from random import *
import pygame

figures = [
    [[1, 5, 9, 13], [4, 5, 6, 7]],
    [[4, 5, 9, 10], [2, 6, 5, 9]],
    [[6, 7, 9, 10], [1, 5, 6, 10]],
    [[1, 2, 5, 9], [0, 4, 5, 6], [1, 5, 9, 8], [4, 5, 6, 10]],
    [[1, 2, 6, 10], [5, 6, 7, 9], [2, 6, 10, 11], [3, 5, 6, 7]],
    [[1, 4, 5, 6], [1, 4, 5, 9], [4, 5, 6, 9], [1, 5, 6, 9]],
    [[1, 2, 5, 6]],
]

# print(1 % len(figures[6]))
type = randint(0, len(figures) - 1)
print(type)
image = figures[type]
print(image)
rotation = 0
block = figures[type][rotation]

for i in range(4):
    rotation = (rotation + i) % len(image)
    print(rotation)
    block = figures[type][rotation]
    print(block)



