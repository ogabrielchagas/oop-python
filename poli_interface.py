class Forma():

    def area(self):
        pass

class Quadrado(Forma):
    
    def __init__(self, lado):
        self.lado = lado

    def area(self):
        return self.lado ** 2
    
class Circulo(Forma):
    def __init__(self, raio):
        self.raio = raio

    def area(self):
        return 3.1415 * self.raio ** 2
    
quadrado = Quadrado(5)
print(quadrado.area())

quadrado2 = Quadrado(7)
print(quadrado2.area())

circulo = Circulo(4)
print(circulo.area())

circulo2 = Circulo(14)
print(circulo2.area())