#Podemos hace saltos de linea en Python usando comillas triples
poema = """Mil peces blancos
como si hierviera
el color del agua"""
print(poema)
#podemos buscar una palabra dentro de un texto y que nos devuelva un booleano
print("agua" in poema)
print("sol" not in poema)
#podemos contar la longitud de un texto utilizando la propiedad len
print(len(poema))
#Tambien se puede multiplicar un texto
print(poema*3)