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

#panel superior
panel_superior = Frame(aplicacion,bd=1,relief=FLAT)
panel_superior.pack(side=TOP)
#etiqueta titulo
etiqueta_titulo = Label(panel_superior, text='sistema de facturacion', fg='azure4',
                        font=('Dosis',58),bg='burlywood',width=27)
etiqueta_titulo.grid(row=0,column=0)

#panel izquierdo
panel_izquierdo = Frame(aplicacion,bd=1,relief=FLAT)
panel_izquierdo.pack(side=LEFT)
#panel costos
panel_costos = Frame(panel_izquierdo,bd=1,relief=FLAT)
panel_costos.pack(side=BOTTOM)
#panel comidas
panel_comidas = LabelFrame(panel_izquierdo, text ="Comida",font=('Dosis',19,'bold'),
                            bd=1, relief=FLAT, fg='azure4')
panel_comidas.pack(side=LEFT)
#panel bebidas
panel_bebidas = LabelFrame(panel_izquierdo, text ="Bebida",font=('Dosis',19,'bold'),
                            bd=1, relief=FLAT, fg='azure4')
#panel postres
panel_postres = LabelFrame(panel_izquierdo, text ="Postres",font=('Dosis',19,'bold'),
                            bd=1, relief=FLAT, fg='azure4')
panel_postres.pack(side=LEFT)
#panel derecha
panel_derecha = Frame(aplicacion,bd=1,relief=FLAT)
panel_derecha.pack(side=RIGHT)

#panel calculadora
panel_calculadora = Frame(panel_derecha, bd =1 , relief = FLAT,bg = 'burlywood')
panel_calculadora.pack()

#panel recibo
panel_recibo = Frame(panel_derecha, bd =1 , relief = FLAT,bg = 'burlywood')
panel_recibo.pack()

#panel botones
panel_botones = Frame(panel_derecha, bd =1 , relief = FLAT,bg = 'burlywood')
panel_botones.pack()

#evitar que la pantalla se cierre
aplicacion.mainloop()
