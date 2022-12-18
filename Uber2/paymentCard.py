from payment import Payment

class PaymentCard(Payment):
    cuenta      = int
    banco       = str
    datoTarjeta = {}
    
    def __init__(self, id, ammount, user, driver, type, cuenta, banco, datoTarjeta):
        super().__init__(id, ammount, user, driver, type)
        self.cuenta    = cuenta
        self.banco     = banco
        self.datoTarjeta = datoTarjeta