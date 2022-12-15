class  Account:
    id       = int
    nombre   = str
    edad     = int
    mail     = str
    telf     = int
    
    def __init__(self, id, nombre, edad, email, telf):
        self.id     = id
        self.nombre = nombre
        self.edad   = edad
        self.email  = email
        self.telf   = telf