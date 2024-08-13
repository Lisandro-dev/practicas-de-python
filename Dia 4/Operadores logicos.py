#Los operadores logicos son and, or y not
#Por cuestiones de legibilidad es conveniente poner cada comparación entre parentesis
mi_bool= 4<5 and 6<5
print(mi_bool)
#Con el operador or una de las dos condiciones tiene que ser verdadera
otro_bool=(10==10) or (12==3)
print(otro_bool)

texto="Esta frase es breve"
busqueda= ("frase" in texto) and ("breve" in texto)
print(busqueda)

#Cuando anteponemos el not, se esta fijando si no es verdad la comparación

compa= not "a"=="a"
print(compa)

#Práctica 1
num1=36
num2=72/2
num3=48
resultado1=num1>num2 and num1 < num3
print(resultado1)

#Práctica2
resultado2=num1>num2 or num1<num3
print(resultado2)

#Práctica3
frase="Cuando algo es lo suficientemente importante, lo haces incluso si las probabilidades de que salga bien no te acompañan"
palabra1="éxito"
palabra2="tecnología"
resultado3= not palabra1 in frase and not palabra2 in frase
print(resultado3)