#Para declarar una funcion se usa la palabra reservada def el nombre de la funcion, parametros  y dos puntos
def miPrimerFuncion():
    "Esta es mi primer función y va a imprimir hola"
    print("Hola")

miPrimerFuncion()

def miSegundaFuncion(nombre):
    "Esta función recibe un parametro, nombre y devuelve el saludo"
    print("Hola "+nombre)
miSegundaFuncion("Luis")
'''
Si pongo tres comilla simples
puedo hacer que los comentarios abarquen 
más de una linea
'''
#Práctica 1
def saludar():
    print("Hola mundo!")
saludar()

#Práctica 2
nombre_persona="Juan"
def bienvenida():
    print(f'¡Bienvenido {nombre_persona}!')
bienvenida()

#Práctica 3
un_numero=4
def cuadrado(un_numero):
    un_numero=un_numero**2
    print(f"El cuadrado es {un_numero}")

cuadrado(9)