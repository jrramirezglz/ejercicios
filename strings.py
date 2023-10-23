saludo = 'Hola Ramon vamos a probar esto'
longitud = len(saludo)
print('la longitud de la cadena es de {}'.format(longitud))
print(saludo[-6])
print(saludo.index('H'))
resultado = saludo.upper()
print(resultado) #HOLA RAMON VAMOS A PROBAR ESTO
resultado = saludo[2].upper()
print(resultado)# L
resultado = saludo.lower()
print(resultado)#hola ramon vamos a probar esto
resultado = saludo.split()
print(resultado) #['Hola', 'Ramon', 'vamos', 'a', 'probar', 'esto']
resultado = saludo.split('t')
print(resultado) #['Hola Ramon vamos a probar es', 'o']
a = 'aprender'
b = 'python'
c = 'es'
d = 'genial'
e = '/'.join([a, b, c, d])
print(e) #aprender/python/es/genial
resultado = saludo.find('Ramon')
print(resultado) #5
resultado = saludo.replace('Ramon', 'Mariela')
print(resultado) #Hola Mariela vamos a probar esto