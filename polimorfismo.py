class animal:
    """#esto es un metodo abstracto. se define en la clase principal para que sea modificada por la
    clases hijo, es necesaria para cada metodo"""
    def hablar(self):
        pass

class perro:
    def hablar(self):
        return 'guau'

class gato:
    def hablar(self):
        return 'miau'

class vaca:
    def hablar(self):
        return 'muu'

def sonido(animal):
    print(animal.hablar())

mi_perro=perro()
mi_gato=gato()
mi_vaca= vaca()

sonido(mi_vaca)
sonido(mi_perro)
sonido(mi_gato)