from carPet import Car

class CarPet(Car):
    trasporte = bool
    
    def __init__(self, placa, model, color, año, matricula, driver, transporte):
        super().__init__(placa, model, color, año, matricula, driver)
        self.trasporte = transporte