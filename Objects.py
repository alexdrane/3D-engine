from VecLib import *
from RotateLib import *
from random import *
from math import *
from trig import *

class constructor():
  def __init__(self,vects,faces):
    self.faces = faces
    self.vects = vects


class face():
    def __init__(self,vects):
        self.vects = vects
    


class shape():
  def __init__(self,centre,const,col):
    self.centre = centre
    self.const =  const
    self.orient = (0,0,0)
    self.rotVel = (0,0,0)#(randint(1,20)/200,randint(1,20)/200,randint(1,20)/200)
    self.vel = vec(0,0,0)
    self.col = col
  def update(self):
    self.rotate(self.rotVel[0],self.rotVel[1],self.rotVel[2])
    self.centre = addVect(self.centre,self.vel)
  def draw(self,viewPoint,DISPLAY,WIDTH,HEIGHT,lightSource):

    relCentre = subVect(self.centre,viewPoint.viewpoint)

    realVects = []
    relVects = []
    for vector in self.const.vects:
      rotVect = rotate(0,0,self.orient[2],vector)
      rotVect = rotate(0,self.orient[1],0,rotVect)
      rotVect = rotate(self.orient[0],0,0,rotVect)
      relVect = addVect(self.centre,rotVect)
      relVects.append(relVect)
      difVect = subVect(relVect,viewPoint.viewpoint)
      rotatedVect = rotate(0,0,-viewPoint.orient[2],difVect)
      rotatedVect = rotate(0,viewPoint.orient[1],0,rotatedVect)
      realVects.append(addVect(rotatedVect,viewPoint.viewpoint))

    for face in self.const.faces:
      faceNormal = crossProduct(subVect(relVects[face[1]-1],relVects[face[0]-1]),subVect(relVects[face[-1]-1],relVects[face[0]-1]))
      arr = []
      draw = True
      d1 = subVect(realVects[face[1]-1],realVects[face[0]-1])
      d2 = subVect(realVects[face[-1]-1],realVects[face[0]-1])
      if dotProduct(crossProduct(d2,d1),subVect(realVects[face[0]-1],viewPoint.viewpoint)) >=0:
        draw = False
      c = 0
      for n in face:
        vector = realVects[n-1]
        difVect = subVect(vector,viewPoint.viewpoint)
        difInY = difVect.y
        fract = difInY/(viewPoint.screen.y-viewPoint.viewpoint.y)
        if fract <=0:
          draw = False
          break
        arr.append([
          -difVect.x/fract+WIDTH/2,
          -difVect.z/fract+HEIGHT/2
          ])


      onScreen = False
      for v in arr:
          if 0<v[0]<WIDTH and 0<v[1]<HEIGHT:
              onScreen = True

      if draw:
        newCol = lightSource.illuminate(faceNormal,self.col,0.2)
        pygame.draw.polygon(DISPLAY,newCol,arr)
        #pygame.draw.lines(DISPLAY,(255,255,255),True,arr,2)



  def rotate(self,x,y,z):
    self.orient = ((self.orient[0]+x)%360,(self.orient[1]+y)%360,(self.orient[2]+z)%360)
