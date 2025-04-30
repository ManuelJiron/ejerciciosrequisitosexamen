from problema1 import ColeccionAlumnos, Alumno
from problema2 import Trayecto, Parada
from problema3 import ColaClientes, Cliente
from problema4 import RegistroMovimientos, Movimiento

if __name__ == "__main__":
    print("Seleccione la operación a realizar:")
    print("1. Organizar alumnos")
    print("2. Calcular trayecto de paradas")
    print("3. Gestión de clientes")
    print("4. Registro de movimientos")
    eleccion = input("Elección: ")

    if eleccion == "1":
        coleccion = ColeccionAlumnos()
        while True:
            id_estudiante = input("ID del alumno: ")
            nombre = input("Nombre: ")
            apellido = input("Apellido: ")
            masa = float(input("Masa (kg): "))
            altura = float(input("Altura (m): "))
            genero = input("Género: ")
            nota_media = float(input("Nota media: "))
            coleccion.insertar(Alumno(id_estudiante, nombre, apellido, masa, altura, genero, nota_media))
            if input("¿Agregar otro alumno? (s/n): ").lower() != "s":
                break
        campo = input("Ordenar por (id_estudiante, nombre, apellido, masa, altura, genero, nota_media): ")
        coleccion.ordenar_por(campo)
        coleccion.mostrar()

    elif eleccion == "2":
        trayecto = Trayecto()
        trayecto.añadir_parada(Parada("A", 5))
        trayecto.añadir_parada(Parada("B", 7))
        trayecto.añadir_parada(Parada("C", 4))
        punto_inicio = input("Parada de inicio: ")
        punto_final = input("Parada de destino: ")
        print("Duración estimada:", trayecto.calcular_duracion(punto_inicio, punto_final), "minutos")

    elif eleccion == "3":
        cola = ColaClientes()
        while True:
            print("\n1. Agregar cliente")
            print("2. Mostrar clientes")
            print("3. Atender cliente")
            print("4. Salir")
            subopcion = input("Opción: ")
            if subopcion == "1":
                nombre_cliente = input("Nombre completo: ")
                años = int(input("Edad: "))
                malestar = input("Malestar principal: ")
                nivel_prioridad = int(input("Nivel de prioridad (1-5): "))
                cola.agregar_cliente(Cliente(nombre_cliente, años, malestar, nivel_prioridad))
            elif subopcion == "2":
                cola.listar_clientes()
            elif subopcion == "3":
                cliente = cola.atender_cliente()
                if cliente:
                    print("Cliente atendido:", cliente.nombre)
                else:
                    print("No hay clientes en espera.")
            elif subopcion == "4":
                break

    elif eleccion == "4":
        registro = RegistroMovimientos()
        while True:
            print("\n1. Registrar movimiento")
            print("2. Retroceder movimiento")
            print("3. Avanzar movimiento")
            print("4. Salir")
            subopcion = input("Opción: ")
            if subopcion == "1":
                categoria = input("Categoría del movimiento (escribir, borrar, pegar, copiar): ")
                descripcion = input("Descripción: ")
                registro.añadir_movimiento(Movimiento(categoria, descripcion))
            elif subopcion == "2":
                movimiento = registro.retroceder()
                if movimiento:
                    print("Movimiento retrocedido:", movimiento.categoria)
                else:
                    print("No hay movimientos para retroceder.")
            elif subopcion == "3":
                movimiento = registro.avanzar()
                if movimiento:
                    print("Movimiento avanzado:", movimiento.categoria)
                else:
                    print("No hay movimientos para avanzar.")
            elif subopcion == "4":
                break

    else:
        print("Elección no válida.")
