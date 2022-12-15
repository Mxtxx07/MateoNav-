from account_driver import Acoount

class Driver(Acoount):
    licencia = str
    auto     = str
    
    def __init__(self,id, nombre, edad, mail, telf, licencia, auto):
        super().__init__(id, nombre, edad, mail, telf)
        self.licencia = licencia
        self.auto     = auto
        
        