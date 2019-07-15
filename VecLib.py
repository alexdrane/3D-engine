from math import *

class vec:
  def __init__(self,x,y,z):
    self.x = x
    self.y = y
    self.z = z

  def val(self):
    return (self.x,self.y,self.z)

def magnitude(v):
  return sqrt(v.x**2+v.y**2+v.z**2)

def subVect(v1,v2):
  return vec(v1.x-v2.x,v1.y-v2.y,v1.z-v2.z)

def addVect(v1,v2):
  return vec(v1.x+v2.x,v1.y+v2.y,v1.z+v2.z)

def crossProduct(v1,v2):
  return vec(v1.y*v2.z-v1.z*v2.y,v1.z*v2.x-v1.x*v2.z,v1.x*v2.y-v1.y*v2.x)

def dotProduct(v1,v2):
  return v1.x*v2.x+v1.y*v2.y+v1.z*v2.z
