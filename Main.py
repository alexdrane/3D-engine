from Objects import *
from pygame import *
from ViewPoints import *
from Shapes import *

WIDTH,HEIGHT = 1800,1000



shapesList = []
for i in range(15):
  num = randint(1,4)
  if num==1:
    const = diamondConstruct
  elif num==2:
    const = pyramidConstruct
  elif num==3:
    const = squareConstruct
  else:
    const = plusConstruct
  shapesList.append(shape(vec(randint(-4000,4000),randint(-4000,4000),randint(-4000,4000)),const))

viewPt = viewFrame(vec(0,0,0))

pygame.init()
DISPLAY = pygame.display.set_mode((WIDTH,HEIGHT),FULLSCREEN)
xvel,yvel,zvel = (0,0,0)
fpsClock = pygame.time.Clock()
zDegChange,yDegChange = 0,0
count = 0
pygame.mouse.set_visible(False) 
while True:
  count+=1
  DISPLAY.fill((0,20,25))
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
  viewPt.rotate(0,y/20,x/20)
  viewPt.move(vec(xvel,yvel,zvel))
  for s in shapesList:
    s.rotate(0.5,0.4,0.2)
    s.draw(viewPt,DISPLAY,WIDTH,HEIGHT)
  fpsClock.tick(60)
  pygame.display.update()
