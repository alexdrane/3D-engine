from Objects import *
from pygame import *
from ViewPoints import *
from Shapes import *
from Lighting import Light


def main(WIDTH,HEIGHT):

  lightSource = Light(vec(10000,0,-10000))
  viewPt = viewFrame(vec(0,0,0))

  for i in range(10):
    num = randint(1,3)
    if num==1:
      const = diamondConstruct
    elif num==2:
      const = squareConstruct
    elif num == 3:
      const = pyramidConstruct
    viewPt.add(shape(vec(randint(-15,15)*200,randint(-15,15)*200,randint(-15,15)*200),const,(randint(0,255),randint(0,255),randint(0,255))))






  pygame.init()
  DISPLAY = pygame.display.set_mode((WIDTH,HEIGHT),FULLSCREEN)
  xvel,yvel,zvel = (0,0,0)
  fpsClock = pygame.time.Clock()
  zDegChange,yDegChange = 0,0
  count = 0
  pygame.mouse.set_visible(False)
  while True:
    count+=1
    DISPLAY.fill((0,60,75))
    for event in pygame.event.get():
      if event.type == KEYDOWN:
        if event.key == K_a:
          xvel += 12
        if event.key == K_d:
          xvel -= 12
        if event.key == K_s:
          yvel -= 12
        if event.key == K_w:
          yvel += 12
        if event.key == K_SPACE:
          zvel += 12
        if event.key == K_LCTRL:
          zvel -= 12
        if event.key == K_ESCAPE:
          pygame.quit()
          sys.exit()
      if event.type == KEYUP:
        if event.key == K_a:
          xvel -= 12
        if event.key == K_d:
          xvel += 12
        if event.key == K_s:
          yvel += 12
        if event.key == K_w:
          yvel -= 12
        if event.key == K_SPACE:
          zvel -= 12
        if event.key == K_LCTRL:
          zvel += 12




    x,y = pygame.mouse.get_rel()
    lightSource.rotate(0.1,0.05,0)
    viewPt.move(vec(xvel,yvel,zvel))
    viewPt.rotate(0,y/18,x/18)
    viewPt.draw(DISPLAY,WIDTH,HEIGHT,lightSource)
    #viewPt.viewpoint.print()
    fpsClock.tick(60)
    pygame.display.update()
