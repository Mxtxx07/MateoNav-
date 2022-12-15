class Route:
    inicio    = [int, int]
    fin       = [int, int]
    tiempo    = int
    distancia = int
    
    def __init__(self, inicio, fin, tiempo, distncia):
        self.inicio    = inicio
        self.fin       = fin
        self.tiempo    = tiempo
        self.distancia = distncia
        