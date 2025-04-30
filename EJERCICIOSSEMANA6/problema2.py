from models.nodo import Nodo

class Parada:
    def __init__(self, identificador, duracion_hasta_siguiente):
        self.identificador = identificador
        self.duracion_hasta_siguiente = duracion_hasta_siguiente

class Trayecto:
    def __init__(self):
        self.inicio = None

    def añadir_parada(self, parada):
        nodo_parada = Nodo(parada)
        if not self.inicio:
            self.inicio = nodo_parada
        else:
            puntero = self.inicio
            while puntero.siguiente:
                puntero = puntero.siguiente
            puntero.siguiente = nodo_parada

    def calcular_duracion(self, punto_inicio, punto_final):
        puntero = self.inicio
        tiempo_total = 0
        en_ruta = False
        while puntero:
            if puntero.data.identificador == punto_inicio:
                en_ruta = True
            if en_ruta:
                tiempo_total += puntero.data.duracion_hasta_siguiente
            if puntero.data.identificador == punto_final:
                break
            puntero = puntero.siguiente
        return tiempo_total
