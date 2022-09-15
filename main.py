import pygame as pg
from pygame.locals import *

HEIGHT=550
WIDTH =1150

vec = pg.math.Vector2

FPS = 60


class Ball(pg.sprite.Sprite):
    def __init__(self,coords):
        super().__init__()
        self.image = pg.Surface([width, height])###############
        self.image.fill(BLACK)
        self.rect = self.surf.get_rect(center = coords)
        
        pg.draw.rect(self.image, (255,255,255), self.rect)

        
        self.pos = vec((coords[0],coords[1]-20))
        self.vel = vec(0,0)
        self.acc = vec(0,0)
    def move(self):
        self.acc = vec(0,0.45)
    
        pressed_keys = pg.key.get_pressed()            
        if pressed_keys[K_LEFT]:
            self.acc.x = -ACC
            self.surf = pg.transform.flip(self.img,True,False)
        if pressed_keys[K_RIGHT]:
            self.acc.x = ACC
            self.surf = pg.transform.flip(self.img,False,False)
             
        #self.acc.x += self.vel.x * FRIC
        self.vel += self.acc
        self.pos += self.vel + 0.5 * self.acc
         
        if self.pos.x > WIDTH-10:
            self.pos.x = WIDTH-10
        if self.pos.x < 10:
            self.pos.x = 10
        if self.pos.y > HEIGHT:
            self.pos.y = HEIGHT
        if self.pos.y < 22:
            self.pos.y = 22
            
        self.rect.center = self.pos
    def launch(self):
        self.vel.y = -20
        self.vel.x = 20



size = (WIDTH,HEIGHT)

screen = pg.display.set_mode(size)
pg.display.set_caption("Trajectory game")



running = True


asl   = pg.sprite.Group()
ball = Ball((255,255))
asl.add(ball)

clock = pg.time.Clock()

# Main loop
while running:
    # events
    for event in pg.event.get():
        # Did the user hit a key?
        if event.type == KEYDOWN:
            # Was it the Escape key?
            if event.key == K_ESCAPE:
                running = False    
            if event.key == K_SPACE:
                player.jump(tiles,tops)

        # Did the user click the window close button? If so, stop the loop.
        elif event.type == QUIT:
            running = False


    pressed_keys = pg.key.get_pressed()



    #draw
    screen.fill((0,0,0))
        

    for entity in asl:
        screen.blit(entity.surf, entity.rect)


    #update
    pg.display.flip()
    clock.tick(FPS)

pg.quit()
