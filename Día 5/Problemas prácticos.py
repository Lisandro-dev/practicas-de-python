#Ejercicio 1:
def devolver_distintos(a,b,c):
    lista=[a,b,c]

    lista.sort()
    suma=a+b+c
    if suma>15:
        print(lista[2])
    elif suma<10:
        print(lista[0])
    else:
        print(lista[1])
    print(lista)
#se ejecuto bien pero no use el min y el max, a la lista le podria haber asignado directamente los valores
devolver_distintos(10,1,2)

#Ejercicio 2

def palabras(palabra):
    lista=[]
    for letra in palabra:
        if letra not in lista:
            lista.append(letra)
    lista.sort()
    print(lista)
palabras("palabra")


#Ejercicio 3

def doble_cero(*args):
    a=1
    for x in args:
        if x==0 and a==0:
            return True
        else:
            a=x
    return False

print(doble_cero(2,5,0,4,8,7,9,1,4))



