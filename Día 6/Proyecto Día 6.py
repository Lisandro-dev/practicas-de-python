# -*- coding: utf-8 -*-
import platform
from pathlib import Path
import os

terminado=True
ruta_recetario=Path('C:\\Recetas')
lista_recetas=[]
cantidad_rec=0
def bienvenida():
    print("Bienvenido al recetario")

def limpiar_consola():
    sistema=platform.system()
    if sistema == "Windows":
        os.system('cls')
    else:
        os.system('clear')

def ruta_acceso():
    ruta=ruta_recetario
    return ruta

def cantidad_recetas():
    ruta=ruta_acceso()
    print(f'Ruta obtenida: {ruta}')
    if ruta is None:
        print('Error: ruta_acceso( devolvio None')
        return
    global cantidad_rec
    for txt in Path(ruta).glob('**/*.txt'):
        cantidad_rec=cantidad_rec+1

    return cantidad_rec

def pedir_numero():
    numero_elegido=''
    es_valido= False
    opciones='123456'
    #mientas no se cumpla como verdadero en valida
    while not es_valido:
        numero_elegido = input(
            "Elige una de las siguientes opciones: \n"
            "1. Elegir categoría de receta\n"
            "2. Escribir una receta\n"
            "3. Crear una categoría de receta nueva\n"
            "4. Eliminar una receta\n"
            "5. Eliminar una categoría\n"
            "6. Finalizar recetario\n"
            "Opción: "
        )

        if numero_elegido in opciones and len(numero_elegido) == 1:
            es_valido = True
        else:
            print("No has elegido un número correcto, intenta de nuevo.")
    return int(numero_elegido)

def pedircategorias():
    ruta = Path("C:\\Recetas")
    categorias = [carpeta for carpeta in ruta.iterdir() if carpeta.is_dir()]
    if not categorias:
        print("No hay categorias disponibles")
        return None
    print("Por favor elige una categoría:")
    for i,categoria in enumerate(categorias, start=1):
        print(f"{i}.{categoria.name}")
    while True:
        try:
            opcion = int(input("Ingrese el número de la categoría: "))
            if 1 <= opcion <= len(categorias):
                return categorias[opcion - 1]  # Devuelve la categoría elegida
            else:
                print("Número fuera de rango, intente de nuevo.")
        except ValueError:
            print("Entrada no válida, ingrese un número.")

def listar_receta(categoria: Path):
    recetas=[archivo for archivo in categoria.glob("*.txt")]
    if not recetas:
        print("No hay recetas disponibles en esta categoría")
        return None
    for i, receta in enumerate(recetas, start =1):
        print(f"{i}.{receta.name}")
    while True:
        try:
            opcion = int(input("Ingrese el número de la receta: "))
            if 1 <= opcion <= len(recetas):
                return recetas[opcion - 1]
            else:
                print("Número fuera de rango, intente de nuevo.")
        except ValueError:
            print("Entrada no válida, ingrese un número.")

def leer_receta(archivo: Path):
    try:
        with archivo.open("r", encoding="utf-8") as file:
            print("\nContenido de la receta:")
            print(file.read())
    except Exception as e:
        print(f"Error al leer el archivo: {e}")

def nombre_receta():
    while True:
        nombre = input("Ingrese el nombre de la receta: ").strip()
        if nombre:
            return nombre + ".txt"
        else:
            print("El nombre no puede estar vacío. Intente de nuevo.")

def contenido_receta(nombre):
    with open(f"{nombre}.txt", 'a', encoding="utf-8") as archivo:  # Asegura que el archivo se cierre automáticamente
        while True:
            contenido = input("Ingrese el contenido de la receta (o escriba 'FIN' para terminar): ")
            if contenido.upper() == "FIN":
                break  # Sale del bucle si el usuario escribe 'FIN'
            archivo.write(contenido + "\n")  # Agrega el contenido con un salto de línea




bienvenida()

while terminado:
    opcion = pedir_numero()
    limpiar_consola()
    print(f"DEBUG: Opción elegida -> {opcion}")
    if opcion == 1:
        categoria_seleccionada = pedircategorias()
        limpiar_consola()
        if categoria_seleccionada:
            receta_pedida = listar_receta(categoria_seleccionada)
            limpiar_consola()
            if receta_pedida:
                leer_receta(receta_pedida)
    elif opcion == 2:  # Escribir una receta nueva
        print("Vamos a crear una receta!")
        categoria_seleccionada = pedircategorias()
        if categoria_seleccionada:  # Verifica que el usuario haya seleccionado una categoría válida
            limpiar_consola()
            nombre = nombre_receta()  # Obtiene el nombre de la receta
            ruta_completa = categoria_seleccionada / f"{nombre}.txt"  # Ruta donde se guardará la receta
            contenido_receta(ruta_completa)  # Guarda el contenido en el archivo
            print(f"Receta '{nombre}' creada con éxito en '{categoria_seleccionada.name}'!")


    elif opcion == 3:  # Crear una nueva categoría
        print("📁 Función para crear categorías aún no implementada.")
    elif opcion == 4:  # Eliminar una receta
        print("🗑 Función para eliminar recetas aún no implementada.")
    elif opcion == 5:  # Eliminar una categoría
        print("🗑 Función para eliminar categorías aún no implementada.")
    elif opcion == 6:  # Salir del programa
        print("👋 ¡Gracias por usar el recetario! Hasta pronto.")
        break

