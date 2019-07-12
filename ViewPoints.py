from VecLib import *
from RotateLib import *
from random import *
from math import *
from trig import *

class viewFrame():
  def __init__(self,viewpoint):
    self.viewpoint = viewpoint
    self.orient = (0,0,0)
    self.setScreen()

  def setScreen(self):
    self.screen = addVect(self.viewpoint,vec(900,800,500))

  def move(self,v):
    moveVect = rotate(0,0,self.orient[2],v)
    self.viewpoint = addVect(self.viewpoint,moveVect)
    self.setScreen()

  def rotate(self,x,y,z):
    self.orient = ((self.orient[0]+x)%360,(self.orient[1]+y)%360,(self.orient[2]+z)%360)
