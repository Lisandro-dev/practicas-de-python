import random
from random import randint

#Lista inicial
palitos = ['-','--','---','----']
#mezclar palitos
def mezclar(lista):
    shuffle(lista)
    return lista

def probarSuerte():
    intento=''
    while intento not in['1','2','3','4']:
        intento = input("Elige un número del 1 al 4: ")
    return int(intento)
#Comprobar el intento

def chequearIntento(lista, intento):
    if lista[intento-1] == '-':
        print("A lavar los platos")
        print(f'te toco {lista[intento-1]}')
        print(lista)
    else: print('Te salvaste')
    print(f'te toco {lista[intento - 1]}')
    print(lista)

#chequearIntento(mezclar(palitos),probarSuerte())
 #Práctica 1
def lanzar_dados():
    dado1 = randint(1, 6)
    dado2 = randint(1, 6)
    return dado1,dado2

def evaluar_jugada(n1,n2):
    suma=n1+n2
    if suma<=6:
        print(f"La suma de tus dados es {suma}. Lamentable")
    elif suma > 6 and suma < 10:
        print(f"La suma de tus dados es {suma}. Tienes buenas chances")
    else:
        print(f"La suma de tus dados es {suma}. Parece una jugada ganadora")
dado1, dado2=lanzar_dados()
evaluar_jugada(dado1,dado2)

#Práctica 2
lista_numero=[1,3,2,4,6,4,7,3,7,23]
def reducir_lista(lista):
    #Para eliminar los duplicados utilizo el método set
    sin_duplicado=list(set(lista))
    #ahora eliminamos el más alto
    sin_duplicado.remove(max(sin_duplicado))
    return sin_duplicado

def promedio(lista):
    #verifico que no este vacia con este if:
    if lista:
        return sum(lista) / len(lista)
    return 0

para_prom=reducir_lista(lista_numero)
print(f"La lista reducida es {para_prom}")
prom=promedio(para_prom)
print(f"el promedio es {prom}")

#Práctica 3
lista_num=[1,5,8,7,3,4]
def lanzar_moneda():
    lanzamiento=random.choice(["Cara", "Cruz"])
    return lanzamiento
def probar_suerte(lanzamiento, lista):
    if lanzamiento == "Cara":
        print(f"La lista fue salvada, y es {lista}")
    else:
        lista=[]
        print(f"La lista se destruyo y es {lista}")
intento=lanzar_moneda()
probar_suerte(intento,lista_num)
