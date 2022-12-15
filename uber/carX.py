from car import Car

class CarX(Car):
    
    def __init__(self, placa, model, color, año, matricula, driver):
        super().__init__(placa, model, color, año, matricula, driver)