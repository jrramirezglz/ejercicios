import os
from pathlib import Path
ruta =os.getcwd() #obtiene el directorio actual
print(ruta)
ruta =os.chdir('D:\\Software\\archivos_prueba_python')#cambiar el directyorio usar doble barra
archivo=open('test.txt')
print(archivo.read())
print(ruta)
ruta = os.mkdir('D:\\Software\\archivos_prueba_python\\otra')#crea un fichero
ruta = 'D:\\Software\\archivos_prueba_python\\prueba.txt'
elemento = os.path.basename(ruta)
print(elemento)
elemento = os.path.dirname(ruta)
print(elemento)
ruta = 'D:\\Software\\archivos_prueba_python\\prueba.txt'
elemento = os.path.split(ruta)
print(elemento)

os.rmdir('D:\\Software\\archivos_prueba_python\\otra')#eliminar elementos

otro_archivo = open('D:\\Software\\archivos_prueba_python\\test.txt')#abrir archivos de otras rutas
print(otro_archivo.read())

carpeta =Path('D:/Software/archivos_prueba_python') #hacer un poath para que lo pueda usar cualquier sistema operativo
archivo = carpeta / 'test.txt'

mi_archivo = open(archivo)
print(mi_archivo.read())