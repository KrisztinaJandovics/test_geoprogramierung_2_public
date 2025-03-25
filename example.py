
class Vector3:
    def __init__(self, x=0.0, y=0.0, z=0.0):
        self._x = x
        self._y = y
        self._z = z
        
    def setX(self, x):
        self._x = x
    
    def getX(self):
        return self._x
    
    def setY(self, y):
        self._y = y
    
    def getY(self):
        return self._y
    
    def setZ(self, z):
        self._z = z
    
    def getZ(self):
        return self._z
    
    def __str__(self):
        return f"x:{self.x} y:{self.y} z:{self.z}"
    
    def __add__(self, addVector):
        return Vector3(self.x + addVector.x, self.y + addVector.y, self.z + addVector.z)
    
    def addition(self, addVector):
        return Vector3(self.x + addVector.x, self.y + addVector.y, self.z + addVector.z)
    
    x = property(getX, setX)
    y = property(getY, setY)
    z = property(getZ, setZ)
    
    
v0 = Vector3(1, 2, 1)
v1 = Vector3(2,0,0)

v2 = v0.addition(v1)
v2 = v0 + v1

print(v2)