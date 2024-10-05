import pygame,sys
pygame.init()
screen= pygame.display.set_mode((600,600))
pygame.display.set_caption("TEST GAME")
screen.fill("white")
pygame.display.update()
class Dino(pygame.sprite.Sprite):
    def __init__(self,x,y):
        super().__init__()
        self.image=pygame.image.load("dino.png")
        self.rect=self.image.get_rect()
        self.rect.center=[x,y]
    def update(self,key_pressed):
        if key_pressed[pygame.K_UP]: 
            print("hi")
            self.rect.move_ip(0,-5)   

        if key_pressed[pygame.K_DOWN]: 
            self.rect.move_ip(0,5)   
        
        if key_pressed[pygame.K_RIGHT]: 
            self.rect.move_ip(5,0)

        if key_pressed[pygame.K_LEFT]: 
            self.rect.move_ip(-5,0)      

d1=Dino(200,200)
d2=Dino(250,250)
dino_group=pygame.sprite.Group()
dino_group.add(d1)
dino_group.add(d2)

pygame.display.update()
while True:
    screen.fill("white")
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            sys.exit()
    dino_group.draw(screen)
    key_pressed=pygame.key.get_pressed()
    d1.update(key_pressed)
    pygame.display.update()