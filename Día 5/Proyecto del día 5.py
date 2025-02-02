#importar metodo choice y crear una lista de palabras
#funcion para pedir letra, para validar letra, para ver si gano, primero escribir funciones

from random import choice

palabras=["barco", "cuaderno", "piscina"]
vidas=6
letras_correctas=[]
letras_incorrectas=[]
aciertos=0
juego_terminado = False

#Función para elegir una palabra al azar

def elegir_palabra(lista):
    palabra=choice(lista)
    letras_de_palabra=len(set(palabra))
    return palabra, letras_de_palabra

def pedir_letra():
    letra=''
    es_valida= False
    abecedario='abcdefghijklmnñopqrstuvwxyz'
    #mientas no se cumpla como verdadero en valida
    while not es_valida:
        letra_elegida = input("Elige una letra: ").lower()
        if letra_elegida in abecedario and len(letra_elegida) ==1:
            es_valida = True
        else:
            print("no has elegido una letra correcta: ")
    return letra_elegida

def mostrar_palabra(palabra_elegida):
    lista_oculta=[]
    for l in palabra_elegida:
        if l in letras_correctas:
            lista_oculta.append(l)
        else:
            lista_oculta.append('-')
    print(' '.join(lista_oculta))

def chequear_letra(letra_elegida, palabra_oculta, vidas, coincidencias):
    fin=False
    if letra_elegida in palabra_oculta:
        letras_correctas.append(letra_elegida)
        coincidencias +=1
    else:
        letras_incorrectas.append(letra_elegida)
        vidas -= 1
    if vidas == 0:
        fin =  perder()
    elif coincidencias == letras_de_palabras:
        fin = ganar(palabra_oculta)
    return vidas, fin, coincidencias

def perder():
    print('Te has quedado sin vidas')
    print('La palabra oculta era '+ palabra)
    return True

def ganar(palabra_descubierta):
    mostrar_palabra(palabra_descubierta)
    print('Felicitaciones, has encontrado la palabra!!!')

palabra, letras_de_palabras = elegir_palabra(palabras)

while not juego_terminado:
    print("\n"+'*'*20+ '\n')
    mostrar_palabra(palabra)
    print('\n')
    print('Letras incorrectas: '+ '-'.join(letras_incorrectas))
    print(f"Vidas: {vidas}")
    print("\n" + '*' * 20 + '\n')
    letra=pedir_letra()

    vidas, terminado, aciertos=chequear_letra(letra, palabra, vidas, aciertos)

    juego_terminado = terminado