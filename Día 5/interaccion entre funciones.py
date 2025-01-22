from random import shuffle

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

chequearIntento(mezclar(palitos),probarSuerte())