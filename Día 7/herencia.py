class Animal():
    def nacer(self):
        print("Este animal ha nacido")
    def __int__(self, edad, color):
        self.edad =edad
        self.color=color
    pass

class Perro(Animal):
    pass

#Averiguo la clase padre de perro
print(Perro.__bases__)
piolin = Perro(3,"rojo")
