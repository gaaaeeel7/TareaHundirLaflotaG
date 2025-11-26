class Barco:
    """Clase que representa un barco del juego Hundir la Flota."""

    def __init__(self, nombre, longitud):
        self.nombre = nombre
        self.longitud = longitud
        self.golpes_recibidos = 0
