lista = [ 'a', 'b', 'c', 'd']
#Lo que estoy diciendo en el for de abajo es: por cada letra (item) dentro de la lista imprimi el item
for letra in lista:
    numero_letra= lista.index(letra)+1
    print(f'La letra número {numero_letra} es la letra {letra}')
#Ahora vamos a realizar un for, que utilizando el metodo starwith (empieza con) nos traiga todos los nombres
#que empiecen con la letra L
nombres=['Pablo', 'Laura', 'Federico', 'Julia', 'Pedro']
for nombre in nombres:
    numero_nombre=nombres.index(nombre)+1
    if nombre.startswith('L'):
        print(f'El nombre {numero_nombre } empieza con L y es {nombre}')
    else: print(f'El nombre {numero_nombre} no empieza con L')
#Ahora empezamos a trabajar con acumuladores y contadores
numeros= [1,2,3,4,5]
acumulador=0
contador=0
for item in numeros:
    acumulador=acumulador+item
    contador= contador+1
    print(f'El valor acumulado es {acumulador} y suman {contador} items')

#Como iterar listas dentro de listas
for a,b in [[1,2],[3,4],[5,6]]:
    print(a)
    print(b)
#Ejercicio 1
alumnos_clase=['María', 'Isabel', 'José', 'Carlos']
for alumno in alumnos_clase:
    print(f'Hola {alumno}')
#Ejercicio 2
lista_numeros=[1,2,5,6,8,3,5,7,3,2,6]
suma_numeros=0
for numero in lista_numeros:
    suma_numeros=suma_numeros+numero
    print(suma_numeros)
#Ejercicio 3
lista2=[1,5,8,7,6,8,2,5,2,6,4,8,5,9,8,3,5,4,2,5,6,4]
suma_par=0
suma_impar=0
for numero in lista2:
    if (numero%2==0):
        suma_par=suma_par+numero
    else: suma_impar=suma_impar+numero

print(f'La suma de los pares es: {suma_par} y la de los impares es {suma_impar}')
