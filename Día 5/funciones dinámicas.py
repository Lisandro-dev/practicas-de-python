#Lo que estamos haciendo es pasarle dentro de nuestra funcion complejidades para que sea más dinámica
def chequear_tres_cifras(numero):
    return numero in range(100,1000)

resul=chequear_tres_cifras(344)
print(resul)

#tambien podria pasarle una variable a la funcion
numero=5445-100
print(chequear_tres_cifras(numero))

#Ahora en vez de un numero le vamos a pasar una lista
def chequear(lista):
    guardar=[]
    for n in lista:
        if n in range(100,1000):
            guardar.append(n)
        else:
            pass
    #Ahora le estoy pidiendo que agregue el elemento que cumple la condicion a una nueva lista y me la devuelva
    return guardar
#return cuando nos devuelve el valor corta el loop, es decir que si la comprobación se da en la primer coparación
#se va a cortar sin seguir veirificando, si no encuentra un valor entre 100 y 1000 me devuelve None
una_lista=[1,34,23,234,534,7456,2134,2]
print(chequear(una_lista))

#Práctica 1
lista_numeros=[2,4,5,7,87,24]

def todos_positivos(lista):
    for x in lista:
        if x < 0:
            return False
        else:
            pass
    return True
print(todos_positivos(lista_numeros))

#Práctica 2
def suma_menores(lista):
    n = 0
    for x in lista:
        if x>0 & x<1000:
            n=n+x
        else:
            pass
    return n

print(suma_menores(lista_numeros))
#Práctica 3
def cantidad_pares(lista):
    contador=0
    for x in lista:
        if x%2==0:
            contador+=1
        else:pass
    return contador

print(cantidad_pares(lista_numeros))