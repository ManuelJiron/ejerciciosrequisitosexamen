from models.nodo import Nodo

class Movimiento:
    def __init__(self, categoria, descripcion):
        self.categoria = categoria
        self.descripcion = descripcion

class RegistroMovimientos:
    def __init__(self):
        self.inicio = None
        self.fin = None
        self.puntero_actual = None

    def añadir_movimiento(self, movimiento):
        nodo_movimiento = Nodo(movimiento)
        if not self.inicio:
            self.inicio = self.fin = nodo_movimiento
        else:
            self.fin.siguiente = nodo_movimiento
            nodo_movimiento.anterior = self.fin
            self.fin = nodo_movimiento
        self.puntero_actual = self.fin

    def retroceder(self):
        if self.puntero_actual and self.puntero_actual.anterior:
            self.puntero_actual = self.puntero_actual.anterior
            return self.puntero_actual.data
        return None

    def avanzar(self):
        if self.puntero_actual and self.puntero_actual.siguiente:
            self.puntero_actual = self.puntero_actual.siguiente
            return self.puntero_actual.data
        return None
