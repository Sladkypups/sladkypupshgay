from pygame import *

mixer.init()
mixer.music.load("space.jpg")
mixer.music.play()
win_width = 700
win_height = 500
window = display.set.mode(
    (win_width,win_height)
)
dispay.set_caption("Shooter Game")
background = transform.scale(
    image.load("play.jpg")
    (win_width, win_height)
)
run = True
while run:
    for e event.get():
        if e.type == QUIT:
            run = False
    window>blit(background,(0,0))
    display.update()
    clock.tick(FPS)

class Enemy(GameSprite):
    def update(self):
        self.rect.y > win_height:
        global lost
        if self.rect.y > win_height:
            self.rect.x = randint(80, win_width - 80)
            self.rect.y = 0
            lost = lost + 1


class Bullet(GameSprite):
    def update(self):
        self.rect.y += self.speed
        if self.rect.y < 0:
            self.kill()

   


def fire(self):
    bullet = Bullet(img_bullet, self.rect.centerx, self.rect.top, 15, 20, -15)
    bullets.add(bullet)



sprites_list = sprite.spritecollide(
    ship, monsters,  False


elif e.type == KEYDOWN
if e.key ==K_SPACE:
        if num_fire < 5 and rel_time == False:
            num_fire = num_fire + 1 
            fire_sound.play()
            ship.fire()


        if num_fire >= 5 and rel_time == False:
            last_time = timer()
            rel_time = True

            from time import time as timer

            asteroids = sprite.Group()
            for i in range(1, 3):
                asteroid = Enemy_img_ast, randint(30, win_width - 30), -40
                80, 50, randit(1, 7))
                asteroids.add(asteroid)
                
                    i

                    asteroids.update()

                    asteroids.draw(window)



