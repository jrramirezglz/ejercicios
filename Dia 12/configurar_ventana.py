from tkinter import *
#iniciar tkinter
aplicacion = Tk()

#tamano ventana
aplicacion.geometry('1020x630+0+0')# tamano 1020x630 en cordenasx = 0 y =0

#evitar maximizar
aplicacion.resizable(0,0)

#titulo de la ventana
aplicacion.title('Mi Restaurante - sistema de facturacion')

#color de fondo de la ventana
aplicacion.config(bg='burlywood') #bg background
#evitar que la pantalla se cierre
aplicacion.mainloop()
