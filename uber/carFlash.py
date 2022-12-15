from carFlash import Car

class CarFlash(Car):
    encargos = bool
    pesoMax  = int
    
    def __init__(self, placa, model, color, año, matricula, driver, encargos, pesoMax,):
        super().__init__(placa, model, color, año, matricula, driver)
        self.encargos = encargos
        self.pesoMax  = pesoMax