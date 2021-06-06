from pygame import *

class GameSprite(sprite.Sprite):
    def init(self, player_image, player_x, player_y, player_speed, width, height):
        super().init()
        self.image = transform.scale(image.load(player_image), (width,height))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y

    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def update(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y <win_height - 80:
            self.rect.y += self.speed
    def update_1(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y <win_height - 80:
            self.rect.y += self.speed




back = (200, 255, 255)
win_height = 500
win_width = 600
window = display.set_mode((win_width, win_height))
window.fill(back)


game = True
finish = False
clock = time.Clock()
FPS = 60

racket1 = Player('racket.png', 30, 200, 4, 50, 150)
racket2 = Player('racket.png', 520, 200, 4, 50, 150)
ball = GameSprite('tenis_ball.png', 200, 200, 4, 50, 50)


while game:
    window.fill(back)
    racket1.reset()
    racket2.reset()
    ball.reset()
    racket1.update()
    racket2.update_1()
    for e in event.get():
        if e.type == QUIT:
            game = False
    display.update()
    clock.tick(FPS)
