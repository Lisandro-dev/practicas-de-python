from random import *
#Lo que hice fue importar una libreria llamada randint, le dije de random (libreria) importa todo
#el metodo randint te pide dos valores, un max y un minimo para devolver un valor aleatorio entre esos dos
aleatorio=randint(1,50)
print(aleatorio)

#Ahora lo que podemos hacer es usar uniform, este metodo trae tambien un numero aleatorio, pero con decimales
aleatorio=round(uniform(1,5),2)
print(aleatorio)

#ahora usamos directamente random, lo que hace es devolver un numero decimal entre 0 y 1
aleatorio=random()
print(aleatorio)

#ahora vamos a ver choice, lo que hace es devolver un elemento aleatorio de una lista

colores=['azul', 'verde', 'rojo']
aleatorio=choice(colores)
print(aleatorio)

#Por último vemos el metodo shuffle, que lo que hace es mezclar una lista en orden aleatorio
numeros = list(range(5,50,5))
shuffle(numeros)
print(numeros)

#Práctica 1
aleatorio = randint(1,10)
print(aleatorio)

#Práctica 2

aleatorio=round(random(), 1)
print(aleatorio)

#Práctica 3

nombres = ["Carlos", "Julia", "Nicole", "Laura", "Mailen"]
sorteo=choice(nombres)
print(sorteo)