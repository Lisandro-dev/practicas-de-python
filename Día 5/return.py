#El return se utiliza cuando nuestra función debe devolver algo
def multipliar (numero1, numero2):
    return numero1*numero2

#Para mostrar el resultado en pantalla tenemos varias opciones, podemos hacer que se guarde en una variable
#o mostrar la llamada a la función dentro del print

resultado = multipliar(10,3)
print(resultado)
print(multipliar(3,2))

#Además, dentro de la función podemos establecer variables internas, como por ejemplo

def sumar(n1,n2):
    total=n1+n2
    return total
print(sumar(5,10))

#Práctica 1
def potencia(n1,n2):
    return n1**n2

print(potencia(2,8))

#Práctica 2
dolares=150
def usd_a_eur(dolares):
    return dolares*0.9
print(usd_a_eur(dolares))

#Práctica 3
palabra="Python"
def invertir_palabra(palabra):
    mayuscula=palabra.upper()
    dado_vuelta=mayuscula[::-1]
    return dado_vuelta
print(invertir_palabra(palabra))