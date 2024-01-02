mi_lista = ['a', 'b', 'c']
mi_lista2 = ['d', 'e', 'f']
print(type(mi_lista))
print(mi_lista)#['a', 'b', 'c']
resultado = len(mi_lista)
print(resultado)#3
resultado = mi_lista[0:2]
print(resultado)#['a', 'b']
print(mi_lista+mi_lista2)#['a', 'b', 'c', 'd', 'e', 'f']
mi_lista3 = mi_lista+mi_lista2
print(mi_lista3)#['a', 'b', 'c', 'd', 'e', 'f']
mi_lista3[0] = 'hola'
print(mi_lista3)#['hola', 'b', 'c', 'd', 'e', 'f']
mi_lista3.append('g')
print(mi_lista3)#['hola', 'b', 'c', 'd', 'e', 'f', 'g']
mi_lista3.pop()
print(mi_lista3) #['hola', 'b', 'c', 'd', 'e', 'f']
mi_lista3.pop(0)
print(mi_lista3) #['b', 'c', 'd', 'e', 'f']
eliminado = mi_lista3.pop(0)
print(mi_lista3)#['c', 'd', 'e', 'f']
print(eliminado)#b
lista = ['b', 'c', 'a','d']
lista.sort() #NO GUARDA LA LISTA ORDENADA EN NINGUN LADO NO SE PUEDE ASIGNAR
# A NINGUNA VARIABLE
print(lista)#['a', 'b', 'c', 'd']
lista.reverse()
print(lista)#['d', 'c', 'b', 'a']
ordenada =sorted(lista)
print(ordenada)