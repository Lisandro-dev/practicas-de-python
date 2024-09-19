from random import *

nombre=input('Por favor dime tu nombre: ')
print(f'Hola {nombre} te propongo un juego, tenes ocho intentos para adivinar un numero')
numero=randint(1,100)
print(numero)
cantidad=8
while cantidad>0:
    intento0 = int(input('Ingresa un número'))
    if intento0<0 or intento0>100:
        print('El numero ingresado es incorrecto')
        print(numero)
    elif intento0>numero:
        cantidad=cantidad-1
        print(f'{intento0} es mayor al número secreto')
        print(numero)
    elif intento0<numero:
        cantidad=cantidad-1
        print(f'{intento0} es menor al numero secreto')
        print(numero)
    elif intento0==numero:
        print(f'{nombre} has ganado el desafio, acertaste el numero secreto')
        print(numero)

print(f'{nombre} te has quedado sin intentos')
