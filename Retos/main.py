from Retos.calculadora import calculadora
from Retos.calculadora import operaciones

for operacion in operaciones:
    print(f"{operacion.name} { operacion.value}\t") 
menu = operaciones(int(input('que operacion quieres realizar ? ')))
my_calculator = calculadora()
my_calculator.set_val1()
my_calculator.set_val2()
my_calculator.resultado(menu)