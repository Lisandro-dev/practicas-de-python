texto = "Este es un texto de ejemplo"

#Forma de llamar a un metodo en python
resultado=texto.upper()
#El metodo split sirve para separar los valores de una frase en palabras de una lista, además
#si se le agrega como parametro un caracter separar la frase por ese valor
otro_resultado=texto.split("e")
#Join se utiliza para unir:
a="Aprender"
b="python"
c="es genial"
e=" ".join([a,b,c])
#find sirve para buscar un determinado caracter dentro del string (como index)
#cuando find no encuentra nada devuelve el valor -1
resultado_find=texto.find("t")
#replace reemplaza un fragmento del texto por otro, necesita el texto a eliminar y el texto a colocar
resultado_repalce=texto.replace("ejemplo", "mentira")
print(resultado)
print(otro_resultado)
print(e)
print(resultado_find)
print(resultado_repalce)