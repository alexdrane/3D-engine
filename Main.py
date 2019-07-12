from Objects import *
from pygame import *
from ViewPoints import *

WIDTH,HEIGHT = 1800,1000

diamondConstruct = constructor([


  vec(0,0,100),
  vec(-100,0,0),
  vec(0,100,0),
  vec(100,0,0),
  vec(0,-100,0),
  vec(-70,0,-30),
  vec(0,70,-30),
  vec(70,0,-30),
  vec(0,-70,-30)
  
  ],[
  [1,2,3],
  [1,3,4],
  [1,4,5],
  [1,5,2],
  [7,6,2,3],
  [8,7,3,4],
  [9,8,4,5],
  [6,9,5,2],
  [6,7,8,9]
  

  ])

diamondList = []
for i in range(30):
  diamondList.append(shape(vec(randint(-10000,10000),randint(-10000,10000),randint(-10000,10000)),diamondConstruct))

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
      if event.key == K_LCTRL:
        zvel += 12
      if event.key == K_SPACE:
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
      if event.key == K_LCTRL:
        zvel -= 12
      if event.key == K_SPACE:
        zvel += 12
      



  x,y = pygame.mouse.get_rel()
  viewPt.rotate(0,0,x/20)
  viewPt.move(vec(xvel,yvel,zvel))
  for d in diamondList:
    d.draw(viewPt,DISPLAY,WIDTH,HEIGHT)
  fpsClock.tick(60)
  pygame.display.update()
