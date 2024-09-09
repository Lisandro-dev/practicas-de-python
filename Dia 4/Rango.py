#Rango sirve para crear parametros de valores a pasar en un for:
for numero in range(0,101,2):
    print(numero)

#Lo que hice fue darle el rango de números a imprimir (desde donde empieza, donde termina, de cuanto en cuanto)
#Rango solo toma integer, ni double ni float

#Practica 1 Crea una lista formada por todos los números desde el 2500 al 2585 (inclusive). Almacena dicha lista en la variable mi_lista.
mi_lista=list(range(2500, 2586))

#Práctica 2: Utilizando la función range(), crea en una única linea de código una lista formada por todos los números múltiplos de 3 desde el 3 al 300 (inclusive). Almacena dicha lista en la variable mi_lista.
milista:list(range(0,301,3))

#Práctica 3: Utiliza la función range() y un loop para sumar los cuadrados de todos los números del 1 al 15 (inclusive). Almacena el resultado en una variable llamada suma_cuadrados.
suma_cuadrados=0
for numero in range(1,16):
    numero=numero**2
    suma_cuadrados=suma_cuadrados+numero

print(suma_cuadrados)