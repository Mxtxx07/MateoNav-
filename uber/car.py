from account_driver import Driver

class car(Driver):
    placa  = str
    modelo = str
    color  = str
    año    = str
    matricula = str
    driver = Driver("", "", "", "", "")
    
    def __init__(self, placa, model, color, año, matricula, driver):
        self.placa     = placa
        self.modelo    = model
        self.color     = color
        self.año       = año
        self.matricula = matricula
        self.driver    = driver