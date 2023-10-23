from enum import Enum

class DiaDeLaSemana(Enum):
    Lunes = 1
    Martes = 2
    Miercoles = 3
    Jueves = 4
    Viernes = 5
    Sabado = 6
    Domingo = 7

for dia in DiaDeLaSemana:
    print(dia.name)
    print(dia.value)