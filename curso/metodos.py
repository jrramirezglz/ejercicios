class pajaro:
    alas = True #elemento de clase
#metodos de instancia afectan al self modifican los atributos
    def __init__(self, color,especie):
        self.color = color #elemento de instancia
        self.especie= especie
    
    def piar(self):
        print('pio')
    
    def volar(self,metros):
        print(f"El pajaro vuela {metros} metros")
    
    def pintar_negro(self):
        self.color = 'negro'
        print(f"Ahora el pajaro es {self.color}")

    @classmethod
    def poner_huevos(cls,cantidad):
        print(f"puso {cantidad} huevos")
        cls.alas = False
        print(pajaro.alas)

    @staticmethod
    def mirar(): # no se refiere a la clase ni al objeto no modifica nada
        print('El pajaro mira')


piolin=pajaro('amarillo', 'canario')
piolin.volar(50)
# no necesita una instancia para hacer la accion pero no puede modificar o acceder a atributos self
pajaro.poner_huevos(3)
pajaro.mirar()