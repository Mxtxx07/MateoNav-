class Madre:
    nombre   = str
    apellido = str
    edad     = int
    ciudad   = str
    
    def __init__(self, nombre, apellido, edad, ciudad):
        self.nombre   = nombre
        self.apellido = apellido
        self.edad     = edad
        self.ciudad   = ciudad
        
    def bienvenido(self, hijo):
        return f'Buena {hijo.nombre} bienvenido a casa, la cena esta  en el micro yo me encunetro de viaje en  {self.ciudad} att: {self.nombre} {self.apellido}'
    
ejemplo = Madre("VERONICA", "FLORES", 56, "QUITO")

print(ejemplo)
        