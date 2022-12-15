from carXL import Car

class CarXL(Car):
    
    asientos = str
    
    def __init__(self, placa, model, color, año, matricula, driver, asientos):
        super().__init__(placa, model, color, año, matricula, driver)
        self.asientos = asientos