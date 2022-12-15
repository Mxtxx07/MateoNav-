from account_user import Acoount

class User(Acoount):
    
    def __init__(self,id, nombre, edad, mail, telf):
        super().__init__(id, nombre, edad, mail, telf)
    