from models.nodo import Nodo

class Alumno:
    def __init__(self, id_estudiante, nombre, apellido, masa, altura, genero, nota_media):
        self.id_estudiante = id_estudiante
        self.nombre = nombre
        self.apellido = apellido
        self.masa = masa
        self.altura = altura
        self.genero = genero
        self.nota_media = nota_media

class ColeccionAlumnos:
    def __init__(self):
        self.inicio = None

    def insertar(self, alumno):
        nodo_nuevo = Nodo(alumno)
        if not self.inicio:
            self.inicio = nodo_nuevo
        else:
            nodo_actual = self.inicio
            while nodo_actual.siguiente:
                nodo_actual = nodo_actual.siguiente
            nodo_actual.siguiente = nodo_nuevo

    def ordenar_por(self, campo):
        if not self.inicio or not self.inicio.siguiente:
            return
        ordenado = True
        while ordenado:
            ordenado = False
            nodo_actual = self.inicio
            while nodo_actual.siguiente:
                if getattr(nodo_actual.data, campo) > getattr(nodo_actual.siguiente.data, campo):
                    nodo_actual.data, nodo_actual.siguiente.data = nodo_actual.siguiente.data, nodo_actual.data
                    ordenado = True
                nodo_actual = nodo_actual.siguiente

    def mostrar(self):
        nodo_actual = self.inicio
        while nodo_actual:
            alumno = nodo_actual.data
            print(alumno.id_estudiante, alumno.nombre, alumno.apellido, alumno.masa, alumno.altura, alumno.genero, alumno.nota_media)
            nodo_actual = nodo_actual.siguiente
