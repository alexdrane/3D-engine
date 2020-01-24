import random
from random import *
import math
from math import *
import pygame
from pygame import *
import sys
from trig import *
import VecLib
from VecLib import vec

def rotationMatrix(B,A,C):
  return [
    [fcos(C)*fcos(B)-fsin(C)*fsin(A)*fsin(B)      ,     -fsin(C)*fcos(A)    ,   fcos(C)*fsin(B)+fsin(C)*fsin(A)*fsin(B)],
    [fsin(C)*fcos(B)+fcos(C)*fsin(A)*fsin(B)    ,       fcos(C)*fcos(A)      ,   fsin(C)*fsin(B)-fcos(C)*fsin(A)*fcos(B)],
    [-fcos(A)*fsin(B)                           ,        fsin(A)            ,   fcos(A)*fcos(B)]
    ]

def rotate(x,y,z,vector):
  rM = rotationMatrix(x,y,z)
  newVec = vec(
    rM[0][0]*vector.x+rM[0][1]*vector.y+rM[0][2]*vector.z,
    rM[1][0]*vector.x+rM[1][1]*vector.y+rM[1][2]*vector.z,
    rM[2][0]*vector.x+rM[2][1]*vector.y+rM[2][2]*vector.z
    )

  return newVec
