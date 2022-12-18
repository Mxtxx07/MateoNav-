class Route:
    inicio      =  [int, int]
    fin         =  [int, int]
    timepoAprox = int
    distanciaKm = int
    
    def __init__(self, inicio, fin, tiempoAprox, distanciaKm):
        self.inicio      = inicio
        self.fin         = fin
        self.timepoAprox = tiempoAprox
        self.distanciaKm = distanciaKm