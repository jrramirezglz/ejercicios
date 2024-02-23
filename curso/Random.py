from random import *

aleatorio = randint(1,50) #entero
print(aleatorio)

aleatorio2 = uniform(1,5) #float
print(aleatorio2)

aleatorio3 = random() #aleatorio en un rango de 0 - 1 
print(aleatorio3)

colores = ['azul', 'rojo', 'verde']
aleatorio4 = choice(colores)
print(aleatorio4)

numeros = list(range(5,50,5))
shuffle(numeros)
print(numeros)