#Herencia de Python

class Persona:
    nombre   = str
    apellido = str
    edad     = int
    
    def __init__(self,nombre,apellido,edad):
        self.nombre   = nombre
        self.apellido = apellido
        self.edad     = edad
        
    def conversar(self,otra_persona):
        return f"Hola{otra_persona.nombre}, me llamo {self.nombre}, tengo {self.edad} años"
    
    
class Hijo (Persona):
    ciudad = str
    
    def __init__(self, nombre, apellido, edad, ciudad):
       Persona.__init__(self, nombre, apellido, edad)
       self.ciudad = ciudad 
       
padre = Persona (" Victor", "Grados", 50)
print(vars(padre))

hijo = Hijo(" Elena", "Grados", 20, "Quito")
print(vars(hijo))


print(padre.conversar(hijo))
print(hijo.conversar(padre))

class Persona2:
    nombre   = str
    apellido = str
    edad     = int
    
    def __init__(self,nombre,apellido):
        self.nombre   = nombre
        self.apellido = apellido
        
    def conversar(self,otra_persona):
        return f"Hola{otra_persona.nombre}, me llamo {self.nombre}, tengo {self.edad} años"
    
class Hijo2(Persona2):
    estudios      = str
    lugarEstudios = str
    
    def __init__(self, nombre, apellido, materia, lugarEstudios):
        super().__init__(nombre, apellido)
        self.materia       = materia
        self.lugarEstudios = lugarEstudios
        
    def informar(self, otra_persona):
        return f"Buenas tardes,{otra_persona.nombre} acabo de estudiar {self.materia} llegue hace unos 20 minutos de {self.lugarEstudios} "
    
padre2 = Persona2("Juan", "Flores")
hijo2  = Hijo2("Jose", "Perez", "Programacion OO", "ITS Yavirac")

print(hijo2.informar(padre2))

class Padre:
     nombre   = str
     apellido = str
     edad     = int
     ciudad   = str
    
     def __init__(self, nombre, apellido, edad, ciudad):
        self.nombre   = nombre
        self.apellido = apellido
        self.edad     = edad
        self.ciudad   = ciudad