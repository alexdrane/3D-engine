from VecLib import *
from RotateLib import *
from random import *
from math import *
from trig import *

class constructor():
  def __init__(self,vects,faces):
    self.faces = faces
    self.vects = vects

class shape():
  def __init__(self,centre,const):
    self.centre = centre
    self.const =  const
    self.rotation = (0,0,0)

  def draw(self,viewPoint,DISPLAY,WIDTH,HEIGHT):

    relCentre = subVect(self.centre,viewPoint.viewpoint)

    realVects = []
    for vector in self.const.vects:
      relVect = addVect(self.centre,vector)
      difVect = subVect(relVect,viewPoint.viewpoint)
      rotatedVect = rotate(0,viewPoint.orient[1],-viewPoint.orient[2],difVect)
      realVects.append(addVect(rotatedVect,viewPoint.viewpoint))
    
    for face in self.const.faces:
      arr = []
      draw = True
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
          difVect.z/fract+HEIGHT/2
          ])
      if draw:
        pygame.draw.lines(DISPLAY,(255,255,255),True,arr,4)
    
      
    
