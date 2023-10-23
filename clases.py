class pokemon:

    def __init__(self, name, atk, health, color):
        self.nombre = name
        self.ataque = atk
        self.salud = health
        self.color = color

    def sanar(self):
        self.salud += 20

    def evolucionar(self, nNombre, nColor):
        self.nombre = nNombre
        self.color = nColor

    def setnombre(self, name):
        self.nombre = name

    def setatk(self, atk):
        self.nombre = atk

    def sethealt(self, healt):
        self.nombre = healt

    def setcolor(self, color):
        self.nombre = color

    def getname(self):
        return self.nombre

    def getatk(self):
        return self.ataque

    def gethealt(self):
        return self.salud

    def getcolor(self):
        return self.color


pokemon1 = pokemon('pikachu', 80, 100, 'amarillo')
print(pokemon1.getname())
print(pokemon1.getatk())
print(pokemon1.getcolor())
print(pokemon1.gethealt())
pokemon1.sanar()
print(pokemon1.gethealt())
pokemon1.evolucionar('raychu', 'naranja')
print(pokemon1.getname())
print(pokemon1.getcolor())
pokemon1.setnombre('NEW')
print(pokemon1.getname())

