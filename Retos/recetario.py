"""Hoy vas a crear un administrador de recetas. Básicamente esto es un programa
a través del cual un usuario puede leer, crear y eliminar recetas que se encuentren en una base
de datos.
tu código le va a dar primero la bienvenida al usuario, le va a informar
la ruta de acceso al directorio donde se encuentra nuestra carpeta de recetas, le va a informar
cuántas recetas hay en total dentro de esa carpeta, y luego le va a pedir que elija una de
estas opciones que tenemos aquí:
La opción 1 le va a preguntar qué categoría elige (carnes, ensaladas, etc.), y una vez que
el usuario elija una, le va a preguntar qué receta quiere leer, y mostrar su contenido.
2. En la opción 2 también se le va a hacer elegir una categoría, pero luego le va a pedir que
escriba el nombre y el contenido de la nueva receta que quiere crear, y el programa va
a crear ese archivo en el lugar correcto.
3. La opción 3 le va a preguntar el nombre de la categoría que quiere crear y va a generar
una carpeta nueva con ese nombre.
4. La opción 4, hará todo lo mismo que la opción uno, pero en vez de leer la receta, la va
a eliminar
5. La opción 5, le va a preguntar qué categoría quiere eliminar
6. Finalmente, la opción 6 simplemente va a finalizar la ejecución del código.
Este programa tiene algunas cuestiones importantes a considerar:
 Cada vez que el usuario realice exitosamente cualquiera de sus opciones, el programa le
va a pedir que presione alguna letra para poder volver al inicio, por lo que el código se
va a repetir una y otra vez, hasta que el usuario elija la opción 6. Esto implica que todo
el menú debe estar dentro de un loop while que se repita una y otra vez hasta que no se
cumpla la condición de que la elección del usuario sea 6
"""

from pathlib import Path
import os


def bienvenida():
    print('bienvenido a tu recetario\n')
    ruta =Path('D:\Software\ejercicios\Retos\Recetas')
    print('Tus recetas estan en ', ruta)
    return ruta

def numero_de_recetas(ruta):
    recetas = ruta.glob('**/*.txt')
    cantidad_de_archivos = list(recetas)
    print('se encontraron ', len(cantidad_de_archivos) , 'recetas')

def menu():
    print("[1] Leer receta\n")
    print("[2] Crear receta\n")
    print("[3] Crear categoria\n")
    print("[4] eliminar receta\n")
    print("[5] eliminar categoria\n")
    print("[6] Finalizar programa\n")
    seleccion = int(input('Que vamos a hacer hoy??\t'))
    return seleccion

def leer_receta(entrada):
    print("[1] Carnes\n")
    print("[2] Ensalada\n")
    print("[3] Pasta\n")
    print("[4] postres\n")
    categoria = int(input('Que categoria te gustaria elegir '))
    if categoria == 1:
        print("Las recetas con carne son \n")
        carne = Path('D:\Software\ejercicios\Retos\Recetas\Carnes')
        recetas = carne.glob('**/*.txt')
        nombres = [nombre.name for nombre in recetas]
        for nombre in nombres:
            print(nombre)
        receta = int(input('Que receta quieres leer 1 o 2 ? '))
        return receta

    if categoria == 2:
        print("Las recetas con carne son \n")
        carne = Path('D:\Software\ejercicios\Retos\Recetas\Ensaladas')
        recetas = carne.glob('**/*.txt')
        nombres = [nombre.name for nombre in recetas]
        for nombre in nombres:
            print(nombre)
        receta = int(input('Que receta quieres leer 1 o 2 ? '))
        return receta
    
    if categoria == 3:
        print("Las recetas con carne son \n")
        carne = Path('D:\Software\ejercicios\Retos\Recetas\Pastas')
        recetas = carne.glob('**/*.txt')
        nombres = [nombre.name for nombre in recetas]
        for nombre in nombres:
            print(nombre)
        receta = int(input('Que receta quieres leer 1 o 2 ? '))
        return receta
                
    if categoria == 4:
        print("Las recetas con carne son \n")
        carne = Path('D:\Software\ejercicios\Retos\Recetas\Postres')
        recetas = carne.glob('**/*.txt')
        nombres = [nombre.name for nombre in recetas]
        for nombre in nombres:
            print(nombre)
        receta = int(input('Que receta quieres leer 1 o 2 ? '))
        return receta

def crear_receta():
    print("[1] Carnes\n")
    print("[2] Ensalada\n")
    print("[3] Pasta\n")
    print("[4] postres\n")
    new_cat = int(input('A que categoria pertenece la nueva receta ? '))
    if (new_cat == 1):
        ruta =Path('D:\Software\ejercicios\Retos\Recetas\Carnes')
        nombre = input('Como se llama la receta ? \n')
        ruta =Path(ruta,nombre+'.txt')
        receta =open(ruta,'a')
        receta.write(input('Escribe tu receta'))
    elif (new_cat == 2):
        ruta =Path('D:\Software\ejercicios\Retos\Recetas\Ensalada')
        nombre = input('Como se llama la receta ? \n')
        ruta =Path(ruta,nombre+'.txt')
        receta =open(ruta,'a')
        receta.write(input('Escribe tu receta'))
    elif (new_cat == 3):
        ruta =Path('D:\Software\ejercicios\Retos\Recetas\Pasta')
        nombre = input('Como se llama la receta ? \n')
        ruta =Path(ruta,nombre+'.txt')
        receta =open(ruta,'a')
        receta.write(input('Escribe tu receta'))
    elif (new_cat == 4):
        ruta =Path('D:\Software\ejercicios\Retos\Recetas\Postre')
        nombre = input('Como se llama la receta ? \n')
        ruta =Path(ruta,nombre+'.txt')
        receta =open(ruta,'a')
        receta.write(input('Escribe tu receta'))
    else:
        print('Categoria invalida \n ')

def crear_categoria():
    categoria = Path('D:\Software\ejercicios\Retos\Recetas')
    categoria_nueva = input("Que categoria te gustaria agregar ? ")
    categoria = Path(categoria,categoria_nueva)
    os.mkdir(categoria)

def eliminar_receta():
    print("[1] Carnes\n")
    print("[2] Ensalada\n")
    print("[3] Pasta\n")
    print("[4] postres\n")
    categoria = int(input('Que categoria te gustaria elegir '))
    if categoria == 1:
        print("Las recetas con carne son \n")
        carne = Path('D:\Software\ejercicios\Retos\Recetas\Carnes')
        recetas = carne.glob('**/*.txt')
        nombres = [nombre.name for nombre in recetas]
        for nombre in nombres:
            print(nombre)
        receta = int(input('Que receta quieres eliminar 1 o 2 ? '))
        return receta

    if categoria == 2:
        print("Las recetas con carne son \n")
        carne = Path('D:\Software\ejercicios\Retos\Recetas\Ensaladas')
        recetas = carne.glob('**/*.txt')
        nombres = [nombre.name for nombre in recetas]
        for nombre in nombres:
            print(nombre)
        receta = int(input('Que receta quieres eliminar 1 o 2 ? '))
        return receta
    
    if categoria == 3:
        print("Las recetas con carne son \n")
        carne = Path('D:\Software\ejercicios\Retos\Recetas\Pastas')
        recetas = carne.glob('**/*.txt')
        nombres = [nombre.name for nombre in recetas]
        for nombre in nombres:
            print(nombre)
        receta = int(input('Que receta quieres eliminar 1 o 2 ? '))
        return receta
                
    if categoria == 4:
        print("Las recetas con carne son \n")
        carne = Path('D:\Software\ejercicios\Retos\Recetas\Postres')
        recetas = carne.glob('**/*.txt')
        nombres = [nombre.name for nombre in recetas]
        for nombre in nombres:
            print(nombre)
        receta = int(input('Que receta quieres eliminar 1 o 2 ? '))
        return receta
 
rutas=bienvenida()
numero_de_recetas(rutas)
seleccion = menu()
if(seleccion == 1):
    receta = leer_receta(seleccion)
elif(seleccion == 2):
    crear_receta()
elif(seleccion == 3):
    crear_categoria()
elif(seleccion == 4):
    eliminar_receta()
elif(seleccion == 5):
    eliminar_receta()
else: 
    print('Seleccion invalida!!!!')
