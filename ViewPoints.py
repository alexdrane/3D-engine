from VecLib import *
from RotateLib import *
from random import *
from math import *
from trig import *

class viewFrame():
  def __init__(self,viewpoint):
    self.viewpoint = viewpoint
    self.orient = (0,0,0)
    self.objects = []
    self.setScreen()

  def add(self,obj):
    self.objects.append(obj)

  def draw(self,DISPLAY,WIDTH,HEIGHT):
    distArr = {}
    for obj in self.objects:
      new = subVect(obj.centre,self.viewpoint)
      mag = magnitude(new)
      distArr[mag] = obj
    while len(distArr) > 0:
      obj = distArr[max(distArr)]
      del distArr[max(distArr)]
      obj.draw(self,DISPLAY,WIDTH,HEIGHT)
      self.objects[self.objects.index(obj)].update()

  def setScreen(self):
    self.screen = addVect(self.viewpoint,vec(900,800,500))

  def move(self,v):
    moveVect = rotate(0,0,self.orient[2],v)
    self.viewpoint = addVect(self.viewpoint,moveVect)
    self.setScreen()

  def rotate(self,x,y,z):
    if -90<(self.orient[1]+y)<90:
      self.orient = ((self.orient[0]+x)%360,(self.orient[1]+y),(self.orient[2]+z)%360)
    else:
      self.orient = ((self.orient[0]+x)%360,self.orient[1],(self.orient[2]+z)%360)
