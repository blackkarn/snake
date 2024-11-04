import pygame as pg

class Box(pg.sprite.Sprite):
    def __init__(self, pos, *groups):
        super().__init__(*groups)
        self.image = pg.image.load("./puzzler/asset/box/box.png").convert_alpha()
        self.image = pg.transform.scale(self.image, (60, 60))
        self.rect = self.image.get_rect(topleft=pos)

class Apple(Box):
    def __init__(self, pos, number,*groups):
        super().__init__(pos, *groups)
        self.image = pg.image.load("./puzzler/asset/apple/apple_"+str(number)+".png").convert_alpha()
        self.image = pg.transform.scale(self.image, (60, 60))
    def used(self):
        self.kill()

class Snake_Head(Box):
    def __init__(self, pos, *groups):
        super().__init__(pos, *groups)
        self.image = pg.image.load("./puzzler/asset/head/head.png").convert_alpha()
        self.image = pg.transform.scale(self.image, (60, 60))

class Snake_Body(Box):
    def __init__(self, pos, direction, *groups):
        super().__init__(pos, *groups)
        start,end = direction 
        self.image = pg.image.load(f"./puzzler/asset/body/{start}_{end}.png").convert_alpha()
        self.image = pg.transform.scale(self.image, (60, 60))
