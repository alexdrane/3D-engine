import random
from random import *
import math
from math import *
import pygame
from pygame import *
import sys
from trig import *


WIDTH = 1800
HEIGHT = 1000

def rotationMatrix(B,A,C):
  return [
    [fcos(C)*fcos(B)-fsin(C)*fsin(A)*fsin(B),-fsin(C)*fcos(A),fcos(C)*fsin(B)+fsin(C)*fsin(A)*fsin(B)],
    [fsin(C)*fcos(B)+fcos(C)*fsin(A)*fsin(B),fcos(C)*fcos(A),fsin(C)*fsin(B)-fcos(C)*fsin(A)*fcos(B)],
    [-fcos(A)*fsin(B),fsin(A),fcos(A)*fcos(B)]
    ]

def rotate(x,y,z,vector):
  rM = rotationMatrix(x,y,z)
  newVec = vec(
    rM[0][0]*vector.x+rM[0][1]*vector.y+rM[0][2]*vector.z,
    rM[1][0]*vector.x+rM[1][1]*vector.y+rM[1][2]*vector.z,
    rM[2][0]*vector.x+rM[2][1]*vector.y+rM[2][2]*vector.z
    )

  return newVec



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
    self.screen =  vec(self.viewpoint.x+900,self.viewpoint.y+800,self.viewpoint.z+500)

class vec:
  def __init__(self,x,y,z):
    self.x = x
    self.y = y
    self.z = z

  def val(self):
    return (self.x,self.y,self.z)


class construct():
  def __init__(self,vects,faces):
    self.vects,self.faces = vects,faces

class centredShape():
  def __init__(self,centre,scale,con):
    self.centre = centre
    self.vects = con.vects
    self.faces = con.faces
    self.scale = scale

  def draw(self,DISPLAY):
    posVects = []
    for v in self.vects:
      posVects.append(vec(self.centre.x+v.x*self.scale,self.centre.y+v.y*self.scale,self.centre.z+v.z*self.scale))

    for face in self.faces:
      newArr = []
      newVects = []
      pri = True
      for num in face:
        newVects.append(posVects[num-1])
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

  def rotate(self,x,y,z):
    c = 0
    for v in self.vects:
      newVec = rotate(x,y,z,v)
      self.vects[self.vects.index(v)] = newVec


      
      
viewPt = view(vec(0,0,0))






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
  scale = (random()-0.5)*3.5
  if scale<0:
    scale-=0.6
  else:
    scale+=0.6
  diamondList.append(centredShape(vec(randint(-4000,4000),randint(400,4000),randint(-500,1200)),scale,diamondConstruct))

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
    diamond.rotate(0,0,0.01)
    diamond.draw(DISPLAY)
  fpsClock.tick(60)
  pygame.display.update()
  
