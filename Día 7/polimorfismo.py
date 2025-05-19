class Vaca:
    def __init__(self, nombre):
        self.nombre=nombre

    def hablar(self):
        print(self.nombre + " dice muuu")

class Oveja:
    def __init__(self, nombre):
         self.nombre = nombre

    def hablar(self):
         print(self.nombre + " dice beeee")

vaca1=Vaca("Aurora")
oveja1=Oveja("Dolly")
vaca1.hablar()
oveja1.hablar()
def animal_habla(animal):
    animal.hablar()

animal_habla(vaca1)
palabra = "polimorfismo"
lista = ["Clases", "POO", "Polimorfismo"]
tupla = (1, 2, 3, 80)

def iterador(elemento):
    print(len(elemento))
iterador(lista)