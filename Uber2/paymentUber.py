from payment import Payment

class PaymentUber(Payment):
    cuenta: int
    banco : str
    
    def __init__(self, id, ammount, user, driver, type, cuenta, banco):
        super().__init__(id, ammount, user, driver, type)
        self.cuenta = cuenta
        self.banco  = banco