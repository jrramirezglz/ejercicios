archivo = open('prueba.txt','a') # r = read w=write a = escribe al final del archivo (sirve para logs)
archivo.write("hola\n")
archivo.write("Soy el nuevo texto")
lista = ['Hola', 'mundo', 'aqui', 'estoy']
archivo.writelines(lista)
archivo.close()