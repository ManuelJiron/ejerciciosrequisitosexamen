from models.nodo import Nodo

class Cliente:
    def __init__(self, nombre, años, malestar, nivel_prioridad):
        self.nombre = nombre
        self.años = años
        self.malestar = malestar
        self.nivel_prioridad = nivel_prioridad

class ColaClientes:
    def __init__(self):
        self.inicio = None

    def agregar_cliente(self, cliente):
        nodo_cliente = Nodo(cliente)
        if not self.inicio:
            self.inicio = nodo_cliente
        else:
            puntero = self.inicio
            while puntero.siguiente:
                puntero = puntero.siguiente
            puntero.siguiente = nodo_cliente

    def atender_cliente(self):
        if self.inicio:
            cliente_atendido = self.inicio.data
            self.inicio = self.inicio.siguiente
            return cliente_atendido
        return None

    def listar_clientes(self):
        puntero = self.inicio
        while puntero:
            c = puntero.data
            print(c.nombre, c.años, c.malestar, c.nivel_prioridad)
            puntero = puntero.siguiente
