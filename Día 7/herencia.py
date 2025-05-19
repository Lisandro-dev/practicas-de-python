class Animal():
    def nacer(self):
        print("Este animal ha nacido")
    def __int__(self, edad, color):
        self.edad =edad
        self.color=color
    pass

class Perro(Animal):
    #hay dos maneras de agregar parametros, una es volver a declarar el init y el otro es con super
    def __int__(self, edad, color, vuela):
        super().__int__(edad, color)
        self.vuela=vuela
    def hablar(self):
        print("pio")
    pass

#Averiguo la clase padre de perro
print(Perro.__bases__)
piolin = Perro()
piolin.hablar()
print(Perro.__mro__)
