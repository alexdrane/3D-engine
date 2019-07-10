import random
from random import *
import math
from math import *
import pygame
from pygame import *
import sys


WIDTH = 1800
HEIGHT = 1000

def findif(v1,v2,xyz):
  if xyz == "x":
    return v1.x-v2.x
  elif xyz == "y":
    return v1.y-v2.y
  elif xyz == "z":
    return v1.z-v2.z

class view:
  def __init__(self,origin):
    self.viewpoint = origin
    self.setScreen()

  def move(self,x,y,z):
    self.viewpoint = vec(self.viewpoint.x+x,self.viewpoint.y+y,self.viewpoint.z+z)
    self.setScreen()

  def setScreen(self):
    self.screen =  vec(self.viewpoint.x+900,self.viewpoint.y+500,self.viewpoint.z+500)

class vec:
  def __init__(self,x,y,z):
    self.x = x
    self.y = y
    self.z = z

  def val(self):
    return (self.x,self.y,self.z)

class shape:
  def __init__(self,vects,faces):
    self.vects = vects
    self.faces = faces

  def draw(self,DISPLAY):
    for face in self.faces:
      newArr = []
      newVects = []
      pri = True
      for num in face:
        newVects.append(self.vects[num-1])
      for v in newVects:
        dif = findif(v,viewPt.viewpoint,"y")/findif(viewPt.screen,viewPt.viewpoint,"y")
        if dif <= 0:
          pri = False
          break
        else:
          newX = findif(v,viewPt.viewpoint,"x")/dif
          newZ = findif(v,viewPt.viewpoint,"z")/dif
          newArr.append((WIDTH/2+newX,HEIGHT/2-newZ))
      if len(newArr) > 1 and pri:    
        pygame.draw.lines(DISPLAY,(255,255,255),True,newArr,4)


class construct(shape):
  def __init__(self,vects,faces):
    shape.__init__(self,vects,faces)

class centredShape(shape):
  def __init__(self,centre,scale,construct):
    newVects = []
    for v in construct.vects:
      newVects.append(vec(centre.x+v.x*scale,centre.y+v.y*scale,centre.z+v.z*scale))
    shape.__init__(self,newVects,construct.faces)
      
class poly:
  def __init__(self,vects):
    self.vects = vects

  def draw(self,DISPLAY):
    newArr = []
    for v in self.vects:
      dif = findif(v,viewPt.viewpoint,"y")/findif(viewPt.screen,viewPt.viewpoint,"y")
      if dif <= 0:
        pass
      else:
        newX = findif(v,viewPt.viewpoint,"x")/dif
        newZ = findif(v,viewPt.viewpoint,"z")/dif
        newArr.append((900+newX,500-newZ))
    pygame.draw.lines(DISPLAY,(255,255,255),False,newArr,3)
      
      
viewPt = view(vec(0,0,0))

pris = shape([

  vec(-300,2500,-200),
  vec(400,2500,-200),
  vec(400,3000,-200),
  vec(-300,3000,-200),
  vec(-300,2750,153),
  vec(400,2750,153)

],[

  [1,2,3,4],
  [1,2,6,5],
  [3,4,5,6]
  
  ])

sqr = shape([

  vec(400,1500,-200),
  vec(800,1500,-200),
  vec(800,1900,-200),
  vec(400,1900,-200),
  vec(400,1500,200),
  vec(800,1500,200),
  vec(800,1900,200),
  vec(400,1900,200),
  ],
  [
    [1,2,3,4],
    [5,6,7,8],
    [1,2,6,5],
    [3,4,8,7]
    ])

tri = shape([
  vec(-800,1100,-200),
  vec(-400,1100,-200),
  vec(-400,1500,-200),
  vec(-800,1500,-200),
  vec(-600,1300,200)
  ],
  [
  [1,2,5],
  [2,3,5],
  [3,4,5],
  [4,1,5]
    ])



diamondConstruct = construct([


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
  [2,3,4,5],
  [1,2,3],
  [1,4,5],
  [6,7,8,9],
  [4,5,9,8],
  [2,3,7,6]
  

  ])

diamondList = []
for i in range(10):
  scale = (random()-0.5)*2.5
  if scale<0:
    scale-=0.6
  else:
    scale+=0.6
  diamondList.append(centredShape(vec(randint(-4000,4000),randint(400,4000),randint(500,1200)),scale,diamondConstruct))


octaHedra = shape([

  vec(2000,2600,-200),
  vec(1700,2600,100),
  vec(2000,2300,100),
  vec(2300,2600,100),
  vec(2000,2900,100),
  vec(2000,2600,400)

  
  ],[
  [2,3,4,5],
  [1,2,3],
  [6,3,4],
  [1,4,5],
  [5,2,6],
  [1,2,5,4,6,4]

   ])

hexPris = shape([

  vec(-900,2000,-200),
  vec(-825,2130,-200),
  vec(-675,2130,-200),
  vec(-600,2000,-200),
  vec(-675,1870,-200),
  vec(-825,1870,-200),
  vec(-900,2000,400),
  vec(-825,2130,400),
  vec(-675,2130,400),
  vec(-600,2000,400),
  vec(-675,1870,400),
  vec(-825,1870,400),
  ],[
    [1,2,3,4,5,6],
    [7,8,9,10,11,12],
    [1,2,8,7],
    [3,4,10,9],
    [5,6,12,11]



    ])


pygame.init()
DISPLAY = pygame.display.set_mode((WIDTH,HEIGHT),FULLSCREEN)
xvel,yvel,zvel = (0,0,0)
fpsClock = pygame.time.Clock()
while True:
  DISPLAY.fill((0,20,25))
  for event in pygame.event.get():
    if event.type == KEYDOWN:
      if event.key == K_a:
        xvel -= 12
      if event.key == K_d:
        xvel += 12
      if event.key == K_s:
        yvel -= 12
      if event.key == K_w:
        yvel += 12
      if event.key == K_SPACE and viewPt.viewpoint.z == 0:
        zvel = 24
      if event.key == K_ESCAPE:
        pygame.quit()
        sys.exit()
    if event.type == KEYUP:
      if event.key == K_a:
        xvel += 12
      if event.key == K_d:
        xvel -= 12
      if event.key == K_s:
        yvel += 12
      if event.key == K_w:
        yvel -= 12

  if viewPt.viewpoint.z > 0:
    zvel -= 1
  elif viewPt.viewpoint.z < 0:
    zvel = 0
    viewPt.viewpoint.z = 0

  viewPt.move(xvel,yvel,zvel)
  for diamond in diamondList:
    diamond.draw(DISPLAY)
  octaHedra.draw(DISPLAY)
  hexPris.draw(DISPLAY)
  tri.draw(DISPLAY)
  pris.draw(DISPLAY)
  sqr.draw(DISPLAY)
  fpsClock.tick(60)
  pygame.display.update()
  
