#args viene de argumentos, le podemos pasar la cantidad de argumentos que queramos
def suma(*args):
    total=0
    for x in args:
        total=total+x
    return total
print(suma(5,6,8,7,4,6,2,4,5,0,7))

#Práctica 1
def suma_cadrador(*args):
    total=0
    for x in args:
        total=total+(x*x)
    return total
print(suma_cadrador(5,4,8))

#Práctica 2

def suma_absolutos(*args):
    total=0
    for x in args:
        if x < 0:
            total=total+(x*-1)
        else:
            total=total+x
    return total
print(suma_absolutos(2,-2,2,-2))

#Práctica 3

def numeros_persona(nombre, *args):
    total=0
    for x in args:
        total=total+x
    return f"{nombre}, la suma de tus numeros en {total}"

print(numeros_persona("Luis", 2,5,6))
