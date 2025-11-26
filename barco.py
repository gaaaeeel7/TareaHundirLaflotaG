class Barco:
    """Clase que representa un barco del juego Hundir la Flota."""

    def __init__(self, nombre, longitud):
        self.nombre = nombre
        self.longitud = longitud
        self.golpes_recibidos = 0

    def recibir_impacto(self):
        if self.golpes_recibidos < self.longitud:
            self.golpes_recibidos += 1

    def metodo_hundir(self):
        return self.golpes_recibidos >= self.longitud


