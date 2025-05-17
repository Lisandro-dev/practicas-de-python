class Pajaro:
    alas=True
    def piar(self):
        print("Pio, pio")

    def __init__(self, color, especie):
        self.color=color
        self.especie=especie
        print(f"soy un pajaro de color {color}")
        print(f"mi especie de pajaro es {especie}")

    def volar(self,metros):
        print(f"El pajaro vuela {metros} metros")

    def pintar_pajaro(self, color):
        self.color=color
        print(f"Ahora el pajaro es de color {color}")
        self.piar()

    @classmethod
    def poner_huevos(cls, cantidad):
        print(f"El pajaro puso {cantidad} huevos")
        cls.alas=False
        print(Pajaro.alas)

    @staticmethod
    def mirar():
        print("el pajaro mira")
pass



tordo = Pajaro("negro", "tordo")
tordo.color
tordo.piar()
tordo.volar(50)
tordo.pintar_pajaro("anaranjado")
tordo.alas=False
print(tordo.alas)
Pajaro.poner_huevos(50)
tordo.poner_huevos(50)
#Tipos de metodo, de instancia (se crean usando def, y contienen self), acceden y modifican al objeto
#Metodos de clase @classmethod entre parentesis llevan el (cls)
#Metodos estaticos @staticmethod, es util cuando un metodo no puede modificar el metodo de instancia o clase

