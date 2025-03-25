class vector3:
    def __init__(self, x=0.0, y=0.0, z=0.0):
        self._x = x
        self._y = y
        self._z = z
    def setx(self, x):
        self._x = x
    def getx(self):
        return self._x
    def sety(self, y):
        self._y = y
    def gety(self):
        return self._y
    def setz(self, z):
        self._z = z
    def getz(self):
        return self._z
    def __mul__(self, multiplikation):
        return vector3(self._x * multiplikation.x, self._y * multiplikation.y, self._z * multiplikation.z)  # Use properties
    def multipl(self, multiplikation):
        return vector3(self._x * multiplikation.x, self._y * multiplikation.y, self._z * multiplikation.z)  # Use properties
    def __dot__(self, skalar):
        return self._x * skalar.x + self._y * skalar.y + self._z * skalar.z
    def skalar(self, skalar):
        return self._x * skalar.x + self._y * skalar.y + self._z * skalar.z
    def __cross__(self, kreuzprodukt):
        return vector3(self._y * kreuzprodukt.z - self._z * kreuzprodukt.y, self._z * kreuzprodukt.x - self._x * kreuzprodukt.z, self._x * kreuzprodukt.y - self._y * kreuzprodukt.x)
    def kreuz(self, kreuzprodukt):
        return vector3(self._y * kreuzprodukt.z - self._z * kreuzprodukt.y, self._z * kreuzprodukt.x - self._x * kreuzprodukt.z, self._x * kreuzprodukt.y - self._y * kreuzprodukt.x)
    x = property(getx, setx)
    y = property(gety, sety)
    z = property(getz, setz)

a = vector3(3, 4, 2)
b = vector3(2, 1, 0)
c = a.multipl(b)
c = a * b
d=a.skalar(b)
e=a.kreuz(b)
print(f"Komponentenweise Multiplikation:   x:{c.x} y:{c.y} z:{c.z}") 
print(f"Skalarprodukt:   {d}") 
print(f"Kreuzprodukt:   x:{e.x} y:{e.y} z:{e.z}") 
