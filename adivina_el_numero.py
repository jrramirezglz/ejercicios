"""
el programa le va a preguntar al usuario su nombre, 
y luego le va a decir
algo así como “Bueno, Juan, he pensado un número entre 1 y 100, y tienes solo ocho intentos
para adivinar cuál crees que es el número”. 
Entonces, en cada intento el jugador dirá un
número y el programa puede responder cuatro cosas distintas:
 Si el número que dijo el usuario es menor a 1 o superior a 100, le va a decir que ha elegido
un número que no está permitido.
 Si el número que ha elegido el usuario es menor al que ha pensado el programa, le va a
decir que su respuesta es incorrecta y que ha elegido un número menor al número secreto.
 Si el usuario eligió un número mayor al número secreto, también se lo hará saber de la
misma manera.
 Y si el usuario acertó el número secreto, se le va a informar que ha ganado y cuántos
intentos le ha tomado. 
Si el usuario no ha acertado en este primer intento, se le va a volver a pedir que elija otro
número. Y así hasta que gane o hasta que se agoten los ocho intentos
"""
from random import *
intento = 0
nombre = input('Hola!!! Cual es tu nombre? \n')
respuesta = randint(1,100)
print(f"Bueno {nombre}, he pensado en un numero del 1 al 100," 
      f"y tienes solo 8 intentos para adivinar este numero")
while(intento < 8):
        intento +=1
        respuesta_usuario=int(input("Dime un numero \n"))
        if(respuesta_usuario< 1 and respuesta_usuario > 100):
            print('Numero invalido!!! El numero debe de ser entre 1 y 100')
        if(respuesta_usuario < respuesta):
            print("Respuesta Incorrecta!!! El numero es mayor")
        if(respuesta_usuario > respuesta):
            print("Respuesta Incorrecta!!! El numero es menor")
        if(respuesta_usuario==respuesta):
            print(f"Respuesta correcta!!! El numero es {respuesta}\n Solo te tomo {intento} intentos")
            break
if(respuesta_usuario != respuesta):
     print(f"Se terminaron los intentos!!! El numero era {respuesta}")