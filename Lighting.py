from VecLib import *
from RotateLib import *
from random import *
from math import *
from trig import *

class Light():
    def __init__(self,pos):
        self.orpos = pos
        self.orient = (0,0,0)
        self.pos = pos

    def rotate(self,x,y,z):
        self.orient = (self.orient[0]+x,self.orient[1]+y,self.orient[2]+z)
        self.pos = rotate(self.orient[0],self.orient[1],self.orient[2],self.orpos)

    def illuminate(self,normal,col,lightLevel):
        scale = dotProduct(normalise(normal),normalise(self.pos))
        if scale > 1:
            scale = 1
        if scale < lightLevel:
            scale = lightLevel
        newCol = (col[0]*scale,col[1]*scale,col[2]*scale)
        return newCol
