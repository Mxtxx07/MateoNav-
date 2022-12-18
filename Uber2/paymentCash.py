from payment import Payment

class PaymentCash(Payment):
    fechadePago = str
    
    def __init__(self, id, ammount, user, driver, type, fechadePago):
        super().__init__(id, ammount, user, driver, type)
        self.fechadePago = fechadePago