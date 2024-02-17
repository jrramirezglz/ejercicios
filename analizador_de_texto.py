""""
    pedir al usuario un texto y luego 3 letras
    imprimir:
    Cuantas veces aparece cada letra
    Cuantas palabras hay en el texto
    Cual e sla primeta letra del texto y la ultima
    Mostrar texto con palabras invertido
    ver si la palabra python esta en la frase
"""

texto = input("dame cualquier texto " ).lower()
letras=[]
letras.append(input ('dame primera letra ').lower())
letras.append( input ('dame segunda letra ').lower())
letras.append(input ('dame tercera letra ').lower())
print('\n')
print("CANTIDAD DE LETRAS")
counta = texto.count(letras[0])
countb = texto.count(letras[1])
countc = texto.count(letras[2])

print(f"hemos encontrado la letra '{letras[0]}' repetida {counta} veces")
print(f"hemos encontrado la letra '{letras[1]}' repetida {countb} veces")
print(f"hemos encontrado la letra '{letras[2]}' repetida {countc} veces")

print('\n')
print("CANTIDAD DE PALABRAS")
palabras = texto.split()
print(f"hemos encontrado {len(palabras)} palabras")
letra_inicio = texto[0]
letra_final = texto[-1]
print(f"la primera letra es  '{letra_inicio}'  y la final es '{letra_final}'")
print('\n')
print("EL TEXTO INVERTIDO ES ")
palabras.reverse()
texto_invertido = ' '.join(palabras)
print(f"el texto inverso es '{texto_invertido}' ")
print('\n')
print("BUSCANDO LA PALABRA PYTHON")
pregunta = 'python' in texto

print(pregunta)