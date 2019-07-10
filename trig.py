import math

def fsin(x):
  if x == 180 or x == 360:
    return(0.0)
  else:
    return(math.sin(x*(math.pi/180)))

def fcos(x):
  if x == 90 or x == 270:
    return(0.0)
  else:
    return(math.cos(x*(math.pi/180)))

def f_sin(x):
  return(math.asin(x)/(math.pi/180))

def findarea(a,b,C):
  return(a*b*fsin(C))/2

def findang(a,b,B):
  return(f_sin(a/(b/fsin(B))))

def finddeg(x,y):
  hyp = math.sqrt(x**2+y**2)
  ang = 0
  try:
    ang = (findang(x,hyp,90))
  except:
    pass
  #print(ang)
  if y <= 0:
    return ang%360
  else:
    return 180-ang

def pythagoras(x,y):
  return math.sqrt(x**2+y**2)

def degtosides(deg,hyp):
  x = hyp*fcos(deg)
  y = hyp*fsin(deg)
  return (y,-x)
  
#print(findang(10,10,90))
