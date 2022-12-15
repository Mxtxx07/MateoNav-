from carConf import Car

class CarConf(Car):
    aceptado = bool
    tapizado = str
    asientos = int
    
    def __init__(self, placa, model, color, año, matricula, driver, aceptado, tapizado, asientos):
        super().__init__(placa, model, color, año, matricula, driver)
        self.aceptado = aceptado
        self.tapizado = tapizado
        self.asientos = asientos