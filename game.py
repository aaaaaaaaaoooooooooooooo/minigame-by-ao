import pyxel
import random

WIDTH = 160
HEIGHT = 120

PLAYER_COLOR = 10

class Player:
    def __init__(self):
        self.x = WIDTH // 2
        self.y = HEIGHT - 10

    def update(self):
        if pyxel.btn(pyxel.KEY_LEFT):
            self.x -= 1
        if pyxel.btn(pyxel.KEY_RIGHT):
            self.x += 1

        if self.x < 0:
            self.x = 0
        if self.x > WIDTH - 8:
            self.x = WIDTH - 8

    def draw(self):
        pyxel.tri(self.x, self.y + 8, self.x + 4, self.y, self.x + 8, self.y + 8, PLAYER_COLOR)

class Enemy:
    def __init__(self):
        self.x = random.randint(0, WIDTH - 8)
        self.y = random.randint(-200, -10)
        self.speed = random.randint(1, 5)
        self.color = random.randint(1, 15)

    def update(self):
        self.y += self.speed

        if self.y > HEIGHT:
            self.x = random.randint(0, WIDTH - 8)
            self.y = random.randint(-200, -10)
            self.speed = random.randint(1, 5)

    def draw(self):
        pyxel.rect(self.x, self.y, 4, 4, self.color)

class Game:
    def __init__(self):
        pyxel.init(WIDTH, HEIGHT)

        self.is_game_over = False
        self.player = Player()
        self.enemies = [Enemy() for _ in range(16)]
        self.score = 0
        self.is_game_over = False
        pyxel.run(self.update, self.draw)

    def update(self):
        if not self.is_game_over:
            self.player.update()
            for enemy in self.enemies:
                enemy.update()

            for enemy in self.enemies:
                if self.check_collision(self.player, enemy):
                    self.is_game_over = True

            self.score += 1

        if self.is_game_over and pyxel.btnp(pyxel.KEY_SPACE):
            self.is_game_over = False
            self.score = 0
            self.player = Player()
            self.enemies = [Enemy() for _ in range(16)]


    def draw(self):
        pyxel.cls(12)
        self.player.draw()
        for enemy in self.enemies:
            enemy.draw()

        pyxel.text(10, 10, "Score: {}".format(self.score), 7)

        if self.is_game_over:
            pyxel.text(WIDTH // 2 - 30, HEIGHT // 2, "GAME OVER", 8)
            pyxel.text(45, 70, "Press SPACE to restart", pyxel.COLOR_RED)

        pyxel.text(10, 20, "run away from it", 7)

    def check_collision(self, obj1, obj2):
        return (
            obj1.x + 8 > obj2.x
            and obj1.x < obj2.x + 8
            and obj1.y + 8 > obj2.y
            and obj1.y < obj2.y + 8
        )

Game()