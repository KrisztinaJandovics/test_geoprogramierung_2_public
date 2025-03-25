class temperatur:
        def __init__(self, temperatur=0.0):
                self._tempertur = float(temperatur) #das ist integer ich soll aufpassen, dass es float wird. Sehe Foto

        def settemperature(self, temperatur):
                self._tempertur = temperatur
        
        def gettemperature(self):
                return self._tempertur
        def __str__(self):
                return f"Celsius: {str(self._tempertur)}"
        #erste Teil. Alle def sind hinzugefügt. temperatur=prperty(gettemperature, settemperature) ist hinzugefügt
        def __int__(self):
                return 1
        def __float__(self):
                return self._tempertur
        def __add__(self, addValue):
                return temperatur(self._tempertur + float(addValue))
        def __gt__(self, compareValue):
                return float(self) > float(compareValue)
        def __lt__(self, compareValue):
                return float(self) < float(compareValue)
        temperatur = property(gettemperature, settemperature)
t0=temperatur(20)
t1=temperatur(30)
"""print(str(t0+t1)) # ich kann da t0 oder t1 schreiben, es wird immer Wert ausgegeben"""
print(int(t0+t1)) #gibt 1 aus, weil ich in __int__ 1 zurückgebe "return 1"
print(float(t0+t1)) #gibt 50 aus, weil ich in __float__ self._tempertur zurückgebe
print(str(t0+t1)) #gibt Celsius: 50.0 aus, weil ich in __str__ Celsius: {str(self._tempertur)} zurückgebe
