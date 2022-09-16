import pygame as pg
from pygame.locals import *
pg.init()

WHITE = (255,255,255)

HEIGHT=750
WIDTH =1400

vec = pg.math.Vector2

FPS = 60
bw = 20
bh = 20

di = vec(10,-10)

class Ball(pg.sprite.Sprite):
    def __init__(self,coords):
        super().__init__()
        self.surf = pg.Surface([bw, bh])
        self.surf.fill(WHITE)
        self.rect = self.surf.get_rect(center = coords)
        
        pg.draw.rect(self.surf, WHITE, [coords[0]-10,coords[1]-10,coords[0]+10,coords[1]+10])

        
        self.pos = vec((coords[0],coords[1]))
        self.vel = vec(0,0)
        self.acc = vec(0,0)
    def move(self):
        self.acc = vec(0,0.45)
    
        pressed_keys = pg.key.get_pressed()            
##        if pressed_keys[K_LEFT]:
##            di.x -= 1
##        if pressed_keys[K_RIGHT]:
##            di.x += 1
             
        #self.acc.x += self.vel.x * FRIC
        self.vel += self.acc
        self.pos += self.vel + 0.5 * self.acc
         
        if self.pos.x > WIDTH:
            self.pos.x = 10
        if self.pos.x < 10:
            self.pos.x = 10
        if self.pos.y > HEIGHT-10:
            self.pos.y = HEIGHT-10
            self.vel.x = 0
        if self.pos.y < 10:
            self.pos.y = 10
            
        self.rect.center = self.pos
    def launch(self):
        if self.pos.y >= HEIGHT-10:
            self.vel.y = di.y
            self.vel.x = di.x



size = (WIDTH,HEIGHT)

screen = pg.display.set_mode(size)
pg.display.set_caption("Trajectory game")



running = True


asl   = pg.sprite.Group()
ball = Ball((10,HEIGHT-10))
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
                ball.launch()
            if event.key == K_RIGHT:
                di.x += 1
            if event.key == K_LEFT:
                di.x -= 1
            if event.key == K_UP:
                di.y -= 1
            if event.key == K_DOWN:
                di.y += 1

        # Did the user click the window close button? If so, stop the loop.
        elif event.type == QUIT:
            running = False


    pressed_keys = pg.key.get_pressed()

    ball.move()

    #draw
    screen.fill((0,0,0))
        

    for entity in asl:
        screen.blit(entity.surf, entity.rect)



    font = pg.font.Font('freesansbold.ttf', 50)
    text = font.render('X: '+str(di.x), 1, WHITE)
    screen.blit(text, (50,10))
    text = font.render('Y: '+str(di.y), 1, WHITE)
    screen.blit(text, (WIDTH - 300,10))


    #update
    pg.display.flip()
    clock.tick(FPS)

pg.quit()
