from plotter import generar_reporte
from search import *


def option_menu():
    print("-------------------------------------")
    print(
        "Ingrese la accion que desea hacer.\n1. Generar reporte.\n2. Busqueda de ID.\n3. Busqueda por nombre\n4. Salir"
    )
    print("Ingrese la opcion: ", end='')
    op = int(input())
    print("-------------------------------------")
    return op


def print_person(person):
    print(f"ID: {person.id}")
    print(f"Nombre: {person.nombre}")
    print(f"Edad: {person.edad}")
    print(f"¿Paga impuestos? {person.impuestos}")


def id_search_menu(censo):
    print("Esta funcion ejecuta una busqueda binaria en el ID.")
    print("Ingrese el id que desea buscar: ", end='')
    id = int(input())
    id = busqueda_binaria(0, len(censo) - 1, censo, id)
    if id == -1:
        print("No se encontró un registro con ese id.")
        return
    print_person(censo[id])


def name_search_menu(censo):
    print("Esta funcion ejecuta una busqueda lineal en el nombre.")
    print("Ingrese el nombre que desea buscar: ", end='')
    name = input()
    if len(name) > 4:
        print("El nombre es maximo de 4 caracteres.")
        return
    name = name.upper()
    index = busqueda_lineal(censo, name)
    if index == -1:
        print("El registro no se ha encontrado.")
        return
    print_person(censo[index])


def print_exit(arr):
    print("Ha seleccionado salir, hasta pronto.")


def principal_menu(censo):
    options = [1, 2, 3, 4]

    actions = [
        principal_menu,
        generar_reporte,
        id_search_menu,
        name_search_menu,
        print_exit
    ]

    op = -1
    while op != 4:
        op = option_menu()
        if op not in options:
            print("Seleccione una opcion valida.")
            continue
        actions[op](censo)
