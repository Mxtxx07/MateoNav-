from padre import Persona
from padre import Persona2
from madre import Madre

class Hijo3(Persona):
    vivienda = str
    
    def __init__(self, nombre, apellido, edad, vivienda):
        super().__init__(nombre, apellido, edad)
        self.vivienda = vivienda
        
hijo3 = Hijo3("Diego", "Yanes", 29, "Centro")
padre3 = Persona("german", "Yanes", 55)

print(vars(hijo3))
print(vars(padre3))

print(hijo3.conversar(padre3))

class Hijo4(Persona2):
    edad     = int
    semestre = str
    
    def __init__(self, nombre, apellido, edad, semestre):
        super().__init__(nombre, apellido)
        self.edad     = edad
        self.semestre = semestre
        
    def felicitar(self, padre):
        return f'Felicidades {self.nombre}, acabas de terminar tu {self.semestre}, a tu {self.edad} años. att tu {padre.nombre}'
    
padre4 = Persona2("Ivan", "Borja")
hijo4 = Hijo4("Ivan", "Borja", 23, "Quinto")

print(vars(padre4))
print(vars(hijo4))

print(hijo4.felicitar(padre4))

class Hijofinal(Madre):
    nombre          = str
    apellidoPaterno = str
    apellidoMaterno = str
    edad            = int
    madre           = Madre("", "", "", "")
    
    def __init__(self, nombre, apellidoPaterno, apellidoMaterno, edad, ciudad, madre):
        super().__init__(nombre, edad, ciudad, madre)
        
        self.apellidoPaterno  = apellidoPaterno
        self.apellidoMaterno  = apellidoMaterno
        self.madre            = madre
        
padrefinal = ("Mateo", "Navas", 56, "QUITO")
madrefinal = Madre("Micaela", "Yanez", 56, "QUITO")
hijofinal  = Hijofinal("Diego", "Yanez", "Perez", 29, "QUITO",Madre("Micaela", "Yanez", 56, "QUITO"))


print(vars(hijofinal))