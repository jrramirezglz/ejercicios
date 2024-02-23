"""
El programa va a elegir una palabra secreta y le va a mostrar al jugador 
solamente una serie de guiones que representa la cantidad de letras que tiene la palabra. 
El jugador en cada turno deberá elegir una letra y si la letra se encuentra en la palabra 
oculta, el sistema le va a mostrar en qué lugares se encuentra. 
Pero si el jugador dice una letra que no se encuentra enla palabra oculta, pierde una vida. 
le vamos a decir que tiene seis vidas y se las iremos descontando de una
en una, cada vez que el jugador elija una letra incorrecta.
Si se agotan las vidas antes de adivinar la palabra, el jugador pierde. 
Pero si adivina la palabra completa antes de perder todas las vidas, el jugador gana.
 Primero vas a crear un código que importe el método choice, ya que lo vas a necesitar
para que el sistema pueda elegir una palabra al azar dentro de una lista de palabras que
también vas a crear al comienzo.
 Luego de eso, vas a crear tantas funciones como creas necesarias para que el programa
haga cosas como pedirle al usuario que elija una letra, para corroborar si lo que el usuario
ha ingresado es una letra válida, para chequear si la letra ingresada se encuentra en la
palabra o no, para verificar si ha ganado o no, etc.
 Recuerda escribir primero las funciones y luego el código que las implementa
ordenadamente.
"""
from random import *

def elegir_palabra():
    palabra_secreta = []
    nueva_palabra = []
    palabras_secretas=["ramon","mariela","romina","nala"]
    palabra_secreta = choice(palabras_secretas)
    palabra_secreta = list(palabra_secreta)
    for index in palabra_secreta:
        nueva_palabra.append("-")
    print(f'Hola!! Vamos a jugar EL JUEGO DEL AHORCADO \n La palabra' 
          f'que tienes que adivinar es \n {nueva_palabra}')
    return palabra_secreta,nueva_palabra

def elegir_letra():
    letra = input("dame una letra \n")
    return letra

def verificar_letra(palabra,secretro, letra):
    if letra in palabra:
        print("SIII")
        for index in palabra:
            print(index)
            if letra == index:
                posicion = palabra.index(letra)
                secretro[posicion]=letra
        print(secretro)
    else:
        print("NOOO")
vidas = 8
palabra,secreto = elegir_palabra()
while(vidas>0):
    letra = elegir_letra()
    verificar_letra(palabra, secreto, letra)
    vidas-=1
if(vidas==0):
    print('Lo siento, perdiste')