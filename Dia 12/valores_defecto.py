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
panel_bebidas.pack(side=LEFT)
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

#lista de productos
lista_comidas = ['pollo',"cordero",'salmon', 'puerco','pez','sopa', 'pizza','tacos']
lista_bebidas = ['agua',"vino",'jugo', 'refresco','vino','tequila', 'ron','cafe']
lista_postres = ['pastel',"helado",'fruta', 'flan','brownies','mousse', 'pan','galletas']
#generar items comida
variable_comida=[]
cuadros_comida=[]
texto_comida=[]

contador = 0
for comida in lista_comidas:
    variable_comida.append('')
    variable_comida[contador]=IntVar()
    comida = Checkbutton(panel_comidas, text = comida.title(), font=('Dosis', 19, 'bold'),
                         onvalue =1, offvalue=0, variable=variable_comida[contador])
    comida.grid(row=contador,column=0, sticky=W)
    #crear los cuadros de entrada
    cuadros_comida.append('')
    texto_comida.append('')
    texto_comida[contador]= StringVar()
    texto_comida[contador].set('0')
    cuadros_comida[contador] = Entry(panel_comidas,
                                     font=('Dosis',18,'bold'),
                                     bd=1,width=6,state=DISABLED,
                                     textvariable=texto_comida[contador])
    cuadros_comida[contador].grid(row=contador,column=1)
    contador+=1

#generar items bebida
variable_bebida=[]
cuadros_bebida=[]
texto_bebida=[]
contador = 0
for bebida in lista_bebidas:
    variable_bebida.append('')
    variable_bebida[contador]=IntVar()
    bebida = Checkbutton(panel_bebidas, text = bebida.title(), font=('Dosis', 19, 'bold'),
                         onvalue =1, offvalue=0, variable=variable_bebida[contador])
    bebida.grid(row=contador,column=0, sticky=W)
        #crear los cuadros de entrada
    cuadros_bebida.append('')
    texto_bebida.append('')
    texto_bebida[contador]= StringVar()
    texto_bebida[contador].set('0')
    cuadros_bebida[contador] = Entry(panel_bebidas,
                                     font=('Dosis',18,'bold'),
                                     bd=1,width=6,state=DISABLED,
                                     textvariable=texto_bebida[contador])
    cuadros_bebida[contador].grid(row=contador,column=1)
    contador+=1
#generar items postres
variable_postres=[]
cuadros_postres=[]
texto_postres=[]
contador = 0
for postres in lista_postres:
    variable_postres.append('')
    variable_postres[contador]=IntVar()
    postres = Checkbutton(panel_postres, text = postres.title(), font=('Dosis', 19, 'bold'),
                         onvalue =1, offvalue=0, variable=variable_postres[contador])
    postres.grid(row=contador,column=0, sticky=W)
        #crear los cuadros de entrada
    cuadros_postres.append('')
    texto_postres.append('')
    texto_postres[contador]= StringVar()
    texto_postres[contador].set('0')
    cuadros_postres[contador] = Entry(panel_postres,
                                     font=('Dosis',18,'bold'),
                                     bd=1,width=6,state=DISABLED,
                                     textvariable=texto_postres[contador])
    cuadros_postres[contador].grid(row=contador,column=1)
    contador+=1

#evitar que la pantalla se cierre
aplicacion.mainloop()