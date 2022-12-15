from payment import Payment

class PaymentCard(Payment):
    cuenta      = int
    banco       = str
    datotarjeta = []
    
    
    def __init__(self, cuenta, banco, datotarjeta,valor,fecha):
            super().__init__(id,valor , fecha)
            self.cuenta      = cuenta
            self.banco       = banco
            self.datotarjeta = datotarjeta