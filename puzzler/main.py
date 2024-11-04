import pygame as pg
from collections import deque
from Box import Box, Apple, Snake_Head, Snake_Body
from reader import reader
class Game:
    def __init__(self):
        self.screen = pg.display.set_mode((1260,600))
        self.clock = pg.time.Clock()
        self.all_sprites = pg.sprite.Group()
        #read the map file -> follow reader.py
        width, height, World, world_apple, snake_Q = reader()



        #Filling the map with box
        self.map = []
        for i in range(height):
            for j in range(width):
                if(World[i][j] == 1):
                    self.map.append(Box((60+j*60, 60+i*60), self.all_sprites))
        
        #Filling the map with apple
        self.apple = []
        for i in range(height):
            for j in range(width):
                if(world_apple[i][j] != 0):
                    self.apple.append(Apple((60+j*60, 60+i*60), world_apple[i][j], self.all_sprites))
        #Filling the map with snake
        self.snake = deque()
        for i in range(len(snake_Q)):
            if i == 0:
                self.snake.append(Snake_Head((60+snake_Q[i][1]*60, 60+snake_Q[i][0]*60), self.all_sprites))
            else:
                self.snake.append(Snake_Body((60+snake_Q[i][1]*60, 60+snake_Q[i][0]*60), snake_Q[i][2], self.all_sprites))
        #self.snake_head = Snake_Head((110, 110), self.all_sprites)

    def run(self):
        while True:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    return
            self.all_sprites.update()
            self.screen.fill((30, 30, 30))
            self.all_sprites.draw(self.screen)
            pg.display.flip()
            self.clock.tick(60) 

if __name__ == '__main__':
    pg.init()
    Game().run()
    pg.quit()