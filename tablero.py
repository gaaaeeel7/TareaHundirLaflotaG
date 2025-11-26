class Tablero:
    """Clase que representa el tablero de juego."""

    def __init__(self, tamano):
        self.dimensiones = (tamano, tamano)
        self.casillas = [[0 for _ in range(tamano)] for _ in range(tamano)]