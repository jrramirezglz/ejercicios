class Animal:

    def __init__(self,edad,color):
        self.edad = edad
        self.color = color

    def nacer(self):
        print("este animal ha nacido")

    def hablar(self):
        print("este animal emite un sonido")

class Pajaro(Animal):
    def __init__(self,edad,color,altura_vuelo): #forma de agregar atributos...reescribiendo 
        self.edad = edad
        self.color = color
        self.altura_vuelo= altura_vuelo

    def __init__(self,edad,color,altura_vuelo):        
        #de esta forma ya no tengo quer volver a escribir  los parametros de la clase padre!!! Los jala
        super().__init__(edad,color) 
        self.altura_vuelo= altura_vuelo

    def hablar(self):
        print("pio")

    def volar(self, metros):
        print(f"el pajaro vuela {metros} metros")

piolin = Pajaro(3,'amarillo',60)
piolin.nacer()
piolin.hablar() #metodo heredado pero sobreescrito "pio"
piolin.volar(100)

mi_animal = Animal(5, 'negro')

class padre:
    def hablar(self):
        print("Hola")

class madre:
    def reir(self):
        print("jaja")

    def hablar(self):
        print("Que tal")

class hijo(padre,madre):
    pass

class nieto(hijo):
    pass

mi_nieto = nieto()

mi_nieto.reir() #jajaja
mi_nieto.hablar() #hola como padre porque heredo primero el el class hijo(padre,madre):