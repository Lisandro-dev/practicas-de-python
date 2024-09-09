#El loop while sirve para ejecutar un bloque de codigo mientras se cumpla una condición
monedas = 5
while monedas >= 1:
    print(f'Tengo {monedas} monedas')
    monedas=monedas-1
else: print('No tengo más monedas')
#Vamos a ejecutar el codigo ahora pero la ejecución dependerá del usuario
respuesta='s'
while respuesta == 's':
    respuesta=input(('Quieres continuar? (s/n)'))
else:
    print('Finalizo el programa')

#La funcion de la palabra reservada pass es para reservar un espacio al programador, por ejemplo podemos
#definir un while y despues con pass, pasar a otro bloque de codigo sin generar un error en el programa
while respuesta==10:
    pass
#La funcion de break es romper el bloque de codigo
nombre=input('Cual es tu nombre?')
for letra in nombre:
    if letra=='r':
        break
    print(letra)
# La palabra continue hace que se continue con la iteración del progama
apellido=input('ahora decime tu apellido')
for item in apellido:
    if item=='f':
        continue
    print(item)
#Ejercicio 1
numero=10
while numero>=0:
    print(numero)
    numero=numero-1
#Ejericio 2
ejercicio=50
while ejercicio>=0:
    if ejercicio%5==0:
        print(ejercicio)
    ejercicio=ejercicio-1

#Ejercicio 3
lista_numeros = [4,5,8,7,6,9,8,2,4,5,7,1,9,5,6,-1,-5,6,-6,-4,-3]
for numero in lista_numeros:
    if numero>=0:
        print(numero)
    else:break