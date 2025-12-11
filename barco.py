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

    def metodo_estado(self):
        print(f"Barco: {self.nombre}")
        print(f"Longitud: {self.longitud}")
        print(f"Golpes recibidos: {self.golpes_recibidos}")
        print(f"Hundido: {self.metodo_hundir()}")


# Ajuste de coordenadas en Barco (Remoto 2)


# Bloque de pruebas
if __name__ == "__main__":
    # Submarino de longitud 1
    submarino = Barco("Submarino", 1)
    submarino.recibir_impacto()
    submarino.metodo_estado()

    print("---")

    # Buque de longitud 3
    buque = Barco("Buque", 3)
    buque.recibir_impacto()
    buque.recibir_impacto()
    buque.metodo_estado()

    buque.recibir_impacto()
    buque.metodo_estado()



