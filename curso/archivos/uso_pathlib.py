from pathlib import Path, PureWindowsPath
from os import system
carpeta = Path('D:/Software/archivos_prueba_python/test.txt') # no es necesario abrir o cerrar el archivo
ruta_windows = PureWindowsPath(carpeta)
print(carpeta.read_text()) #contenido del archivo
print(carpeta.name) #nombre del archivo
print(carpeta.suffix) #extencion
print(carpeta.stem) #nombre sin extencion

if not carpeta.exists(): #revisa si existe el archivo
    print('Archivo nop existe')
else:
    print('Archivo existe Genial')
print(ruta_windows)

base = Path.home() #ruta absoluta al directorio princiupal "usuario"
guia = Path("barcelona", 'sagrada familia') # el objeto pad agrega \ a las palabras
print(base)
print(guia)
guia = Path(base,"barcelona", 'sagrada_familia') # el objeto pad agrega \ a las palabras
print(guia)
guia2 = Path(base,'europa','España', Path("barcelona", 'sagrada_familia')) # el objeto pad agrega \ a las palabras
guia3 = guia2.with_name('la_pedrera.txt')
print(guia2)#C:\Users\jr_ra\europa\España\barcelona\sagrada_familia
print(guia3) #C:\Users\jr_ra\europa\España\barcelona\la_pedrera.txt
system('cls')
print(guia2.parent)#devuelve el antecedor mas inmediato C:\Users\jr_ra\europa\España\barcelona
