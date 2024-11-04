#map file should be as the following:
# 1. the first line should be the width and height of the map
from collections import deque
def reader():
    snake_Q = deque()

    Direction_dict = {0:"top", 1:"right", 2:"down", 3:"left"}

    f = open("./puzzler/mapfile.txt","r")
    width, height = map(int, f.readline().split())
    World = []

    #read_world
    for i in range(height):
        World.append(list(map(int, f.readline().split())))
    Apple = [[0 for i in range(width)] for j in range(height)]

    #read_apple
    apple_number = int(f.readline())
    for i in range(apple_number):
        y,x, number = map(int, f.readline().split())
        Apple[y][x] = number

    #read_snake
    snake_length = int(f.readline())
    for i in range(snake_length):
        x, y, start,end = map(int, f.readline().split())
        if(start==5 and end == 5):
            snake_Q.append((x,y))
        else:
            snake_Q.append((x,y,(Direction_dict[start],Direction_dict[end])))
    f.close()
    return width, height, World, Apple, snake_Q