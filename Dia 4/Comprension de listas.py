palabra='Python'
lista=[]
for letra in palabra:
    lista.append(letra)

print(lista)
#Ahora voy a ahorrar codigo porniendo el for dentro de la lista
lista2=[letra for letra in palabra]
print(lista2)

#Ahora armemos una lista de numeros dentro de un rango

list3= [n for n in range(0,20,2)]
print(list3)

#Podemos ademas colocar un if en la lista

lista4=[n for n in range (0,20,2) if n*2 > 10]
print(lista4)

#Podemos agregar el else tambien, pero cambia la sintaxis

lista5=[n if n*2>10 else 'no' for n in range(0,20)]
print(lista5)

#Ejemplo
pies=[10,20,30,40,50]
metros=[medida * 3.81 for medida in pies]
print(metros)

#Práctica 1
valores = [1, 2, 3, 4, 5, 6, 9.5]
valores_cuadrados=[valor**2 for valor in valores]
print(valores_cuadrados)

#Práctica2
valores = [1, 2, 3, 4, 5, 6, 9.5]
valores_pares=[valor for valor in valores if valor%2==0]
print(valores_pares)

#Práctica 3

temperatura_fahrenheit = [32, 212, 275]
grados_celsius=[(grados_fahrenheit-32)*(5/9) for grados_fahrenheit in temperatura_fahrenheit]
print(grados_celsius)