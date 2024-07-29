mi_texto= "Esta es una prueba"
resultado = mi_texto.index("e")
resulta2 = mi_texto.index("e", 10, 18)
#El primer parametro es la letra que busco, el segundo parametro es desde donde y el tercero hasta donde
al_reves=mi_texto.rindex("a")
#el rindex funciona de la misma manera pero empieza a contar desde atras para adelante
print(type(resultado))
print(mi_texto[2])
print(resultado)
print(resulta2)
print(al_reves)