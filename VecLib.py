

class vec:
  def __init__(self,x,y,z):
    self.x = x
    self.y = y
    self.z = z

  def val(self):
    return (self.x,self.y,self.z)

def subVect(v1,v2):
  return vec(v1.x-v2.x,v1.y-v2.y,v1.z-v2.z)

def addVect(v1,v2):
  return vec(v1.x+v2.x,v1.y+v2.y,v1.z+v2.z)
