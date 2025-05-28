from pygame import *
from random import *
from timer import *

SCREEN_WIDTH, SCREEN_HEIGHT = 840, 600

BACKGROUND_IMG = 'galaxy.jpg' #1. Subir la imagen
BACKGROUND_IMG2 = 'gameover.jpg'

CHARACTER1LOAD  = 'rocket.png' #1. OBJETO 1

TRESURELOAD  = 'ufo.png' #1. OBJETO 2
TRESURELOAD1  = 'png-transparent-gasoline-others-miscellaneous-jerrycan-canister-thumbnail-removebg-preview.png' #1. OBJETO 2
TRESURELOAD2 = 'png-transparent-hayabusa2-asteroid-162173-ryugu-space-probe-asteroid-spacecraft-outer-space-nasa-removebg-preview.png'

Xp1,Yp1 = 400,500

font.init()
font_1 = font.SysFont('Arial',20)
misses = 0
life = 3
points = 0

# init()
# mixer.init()
# mixer.music.load('fire.ogg')
# mixer.music.play()

window = display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
display.set_caption('shoter')
background = transform.scale(image.load(BACKGROUND_IMG), (SCREEN_WIDTH, SCREEN_HEIGHT))
background2 = transform.scale(image.load(BACKGROUND_IMG2), (SCREEN_WIDTH, SCREEN_HEIGHT))
rosa = (58,95,168)




class Character(sprite.Sprite):
    def __init__(self, img, cor_x, cor_y, width, height, speed=0):
        super().__init__()
        self.height = height
        self.width = width
        self.image = transform.scale(image.load(img), (self.height,self.width))
        self.speed = speed
        self.rect = self.image.get_rect()
        self.rect.x = cor_x
        self.rect.y = cor_y

    def reset(self):
        screen.blit(self.image, (self.rect.x, self.rect.y))


class Player(Character):
    def update(self):
        keys = key.get_pressed()
        if keys[K_d] and self.rect.x < SCREEN_WIDTH - 81:
            self.rect.x += self.speed
        if keys[K_a] and self.rect.x > 1:
            self.rect.x -= self.speed
    def shut(self):
        for i in range (5):
            
            bullet = Bullet('bullet.png',self.rect.centerx, self.rect.top,20,35,10)
            Bullets.add(bullet)

class Enemy(Character):

    def update(self):
        global misses
        self.rect.y += self.speed
        if self.rect.y >= SCREEN_HEIGHT:
            self.rect.y = -100
            self.rect.x = randint(50,SCREEN_WIDTH-100)
            self.speed = randint(2,5)
            misses += 1

class Bullet(Character):
    def update(self):
        self.rect.y -= self.speed 
        if  self.rect.y <= 0:
            self.kill()



Bullets = sprite.Group()



screen = display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
background = transform.scale(image.load(BACKGROUND_IMG), (SCREEN_WIDTH, SCREEN_HEIGHT))
Player1 = Player(CHARACTER1LOAD,0,SCREEN_HEIGHT-100,100,100,5)

monsters = sprite.Group()
for i in range (1,randint(5,7)):
    enemy = Enemy(TRESURELOAD, randint(0,SCREEN_HEIGHT-100),-100,100,100,randint(3,5))
    monsters.add(enemy)


monsters1 = sprite.Group()
for i in range (1):
    enemy = Enemy(TRESURELOAD1, randint(0,SCREEN_HEIGHT-100),-100,100,100,randint(3,5))
    monsters1.add(enemy)

monsters2 = sprite.Group()
for i in range (1):
    enemy = Enemy(TRESURELOAD2, randint(0,SCREEN_HEIGHT-100),-100,100,100,randint(3,5))
    monsters2.add(enemy)

fin = False
clock = time.Clock()
run = True
FPS = 165
finish = False

while run :

    for e in event.get():

        if e.type == QUIT:

            run = False

        
        if e.type== KEYDOWN:
            
                
            if e.key == K_SPACE:
                
                Player1.shut()
            if e.key == K_SPACE:
                
                Player1.shut()

    if not finish:

        keys = key.get_pressed()
        screen.blit(background,(0,0))
        pointtext = font_1.render(f'points: {points}',True ,(123,231,121))
        screen.blit(pointtext,(20,40))
        missttext = font_1.render(f'strikes: {misses}',True ,(123,231,221))
        screen.blit(missttext,(20,20))
        lifetext = font_1.render(f'life: {life}',True ,(132,94,217))
        screen.blit(lifetext,(SCREEN_WIDTH - 70,30))

        Player1.reset()
        Player1.update()

        monsters.draw(screen)
        monsters.update()

        monsters1.draw(screen)
        monsters1.update()

        monsters2.draw(screen)
        monsters2.update()

        Bullets.draw(screen)
        Bullets.update()

        collide = sprite.groupcollide(monsters ,Bullets,True ,True)
        collide1 = sprite.groupcollide(monsters1 ,Bullets,True ,True)
        
        #////////////////////////////////////masianito/////////////////////////////////
        for colision in collide:
            points += 1
            
            enemy = Enemy(TRESURELOAD, randint(0,SCREEN_HEIGHT-100),-100,100,100,randint(3,5))
            monsters.add(enemy)

        if sprite.spritecollide(Player1,monsters,True):
            enemy = Enemy(TRESURELOAD, randint(0,SCREEN_HEIGHT-100),-100,100,100,randint(3,5))
            monsters.add(enemy)
            life -= 1
        #///////
        for colision in collide1:
            enemy = Enemy(TRESURELOAD1 , randint(0,SCREEN_HEIGHT-100),-100,100,100,randint(3,5))
            monsters1.add(enemy)
        
        if sprite.spritecollide(Player1,monsters1,True):
            enemy = Enemy(TRESURELOAD1 , randint(0,SCREEN_HEIGHT-100),-100,100,100,randint(3,5))
            monsters1.add(enemy)
            life += 2

        
        if sprite.spritecollide(Player1,monsters2,True):
            enemy = Enemy(TRESURELOAD2 , randint(0,SCREEN_HEIGHT-100),-100,100,100,randint(3,5))
            monsters2.add(enemy)
            life -= 1


        if misses == 20 or life <=-0:
            finish = True
            print('aholamundo')
            screen.blit(background2,(0,0))


    display.update()
    clock.tick(FPS)

quit()


