palabra = 'python'
lista = []
for letra in palabra:
    lista.append(letra)
print(lista)

palabra2 = 'Ramon'

lista2 = [letra for letra in palabra2]
print(lista2)

lista3 = [n/2 for n in range(0,21,2)]
print(lista3)

lista4 = [n for n in range(0,21,2) if n*2 >10]
print(lista4)

lista5 = [n  if n*2 >10 else 'no' for n in range(0,21,2)]
print(lista5)