class Tablero:
    """Clase que representa el tablero de juego."""

    def __init__(self, tamano):
        self.dimensiones = (tamano, tamano)
        self.casillas = [[0 for _ in range(tamano)] for _ in range(tamano)]

    def mostrar_tablero(self):
        for fila in self.casillas:
            print(" ".join(str(celda) for celda in fila))