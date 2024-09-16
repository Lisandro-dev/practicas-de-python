lista=[52,12,4,87,98,125]
print(f'El menor numero de la lista es {min(lista)} y el mayor numero de la lista es {max(lista)}')

#En cuanto a las letras, primero busca entre las mayusculas y luego entre las minusculas
palabras='Cantero'
print(f'La menor letra por defecto es {min(palabras)} mientras que la menor sin disntinguir minusculas es {min(palabras.lower())}')

#Práctica 1
lista_numeros = [44542247/2, 21310/5, 2134747*33, 44556475, 121676, 6654067, 353254, 123134, 55**12, 611**5]
valor_maximo= max(lista_numeros)
print(valor_maximo)

#Práctica 2

lista_numeross = [44542247, 21310, 2134747, 44556475, 121676, 6654067, 353254, 123134, 552512, 611665]
rango=max(lista_numeross)-min(lista_numeross)
print(rango)

#Práctica 3:

diccionario_edades = {"Carlos":55, "María":42, "Mabel":78, "José":44, "Lucas":24, "Rocío":35, "Sebastián":19, "Catalina":2,"Darío":49}
edad_minima=min(diccionario_edades.values())
ultimo_nombre=max(diccionario_edades)
print(f'La edad minima de la lista es {edad_minima} y el último nombre de la misma es {ultimo_nombre}')