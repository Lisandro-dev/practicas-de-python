texto = input("Por favor ingresa el texto a analizar: ")
ltr1 = input("Ingresa la primera letra: ").lower()
ltr2 = input("Ingresa la segunda letra: ").lower()
ltr3 = input("Ingresa la tercer letra: ").lower()
en_minuscula=texto.lower()
lista_de_letras=[ltr1,ltr2,ltr3]
#CON EL METODO COUNT PUEDO CONTAR LA CANTIDAD DE VECES QUE APARECE LA LETRA EN EL TEXTO
resultado1 = en_minuscula.count(ltr1)
resultado2 = en_minuscula.count(ltr2)
resultado3=en_minuscula.count(ltr3)
#CON EL METODO SPLIT VAMOS A SEPARAR EL TEXTO EN UNA LISTA
separado=en_minuscula.split()
cantidadPalabras=len(separado)
#OBTENER PRIMERA Y ULTIMA LETRA
primeraLetra=texto[0]
ultimaLetra=texto[-1]
#TEXTO INVERTIDO
separado.reverse()
unir=" ".join(separado)
#ver si la palabra python sta en el texo
validarPython="python" in texto
dic = {True: "si", False: "NO"}

#PRUEBAS
print("El texto ingresado es: " + texto)
#print(en_minuscula)
#print(f"Las letras son "+ ltr1 +" ," +ltr2+ " y "+ ltr3 )
#print(lista_de_letras)
print(f"La cantidad de veces que aparecen las letras es: \n{ltr1}: {resultado1}\n{ltr2}: {resultado2}\n{ltr3}: {resultado3}")
print(f"La cantidad de palabras del texto es de: {cantidadPalabras}")

print(f"La primera letra del texto es: {primeraLetra}, y la última letra es: {ultimaLetra}")
print(unir)
print(f"La palabra python {dic[validarPython]} se encuentra en el texto")