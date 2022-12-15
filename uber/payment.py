from account_user import User
from account_driver import Driver

class Payment:
    id       = int
    cantidad = int
    user     = User("", "", "", "", "")
    driver   = Driver("", "", "", "", "")
    type     = str
    
    def __init__(self, id, cantidad, user, driver, type):
        self.id         = id
        self.cantidad   = cantidad
        self.user       = user
        self.driver     = driver
        self.type       = type
        