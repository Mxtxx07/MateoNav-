from account_admin import Acoount

class Admin(Acoount):
    
    def __init__(self,id, nombre, edad, mail, telf):
        super().__init__(id, nombre, edad, mail, telf)