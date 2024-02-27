mi_archivo = open('prueba.txt') #abre el archivo
print(mi_archivo.read()) #lee el archivo
mi_archivo.close() #cierra el archivo
mi_archivo = open('prueba.txt')
print(mi_archivo.readline())
una_linea = mi_archivo.readline()
print(una_linea)

print(una_linea.upper())
mi_archivo.close() #cierra el archivo
mi_archivo = open('prueba.txt') #abre el archivo
print(mi_archivo.read()) #lee el archivo
for l in mi_archivo:
    print('AQUI DICE : '+ l)
