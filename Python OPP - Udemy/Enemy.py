class Sprite:

    def __init__(self, x, y, img_file, speed, life_counter):
        self.x = x
        self.y = y
        self.img_file = img_file
        self.speed = speed
        self.life_counter = life_counter


class Enemy(Sprite):

    def __init__(self, x, y, img_file, speed, life_counter=5):
        Sprite.__init__(x, y, img_file, speed, 5)
        self.message = "I'm here to protect my master"


class Player(Enemy):

    def __init__(self, x, y, img_file, speed, life_counter=6):
        Enemy.__init__(self, x, y, img_file, speed, 6)
        self.speed = 56


class DifficultEnemy(Enemy):

    def __init__(self, x, y, img_file):
        Enemy.__init__(self, x, y, img_file, 80)


class EasyEnemy(Player):

    def __init__(self, x, y, img_file, speed, life_counter):
        Player.__init__(x, y, img_file, speed, life_counter)
        self.life_counter = 1
