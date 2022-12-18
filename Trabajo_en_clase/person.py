class Persona:
    nombre = str
    edad= int
    centroestudios= str

    def init(self,nombre,edad,centroestudios):
        self.nombre=nombre
        self.edad=edad
        self.centroestudios=centroestudios
    
    def conversar(self, otra_persona):
        return f'Hola {otra_persona.nombre} me llamo {self.nombre}, estudio en {self.centroestudios}'

if __name__ == '__main__':
    Persona2 = Persona("Juan",18,"Yavirac")
    Persona1 = Persona("Alisson",21,"UCE")
    
    print (Persona1.conversar(Persona2))