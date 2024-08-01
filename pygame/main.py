import pygame
import random
import math
from pygame import mixer
# formula para calcular colisiones 
#inicializar pygame
pygame.init()

#crea la pantalla
pantalla = pygame.display.set_mode((800,600)) #pixelesTUPLAS colores solidos

#titulo e icono
pygame.display.set_caption('Invacion espacial')#titulo
icono = pygame.image.load('ovni.png') #icono dentro de la carpeta
pygame.display.set_icon(icono)#carga la imagen
fondo = pygame.image.load('fondo.jpg')

#agregar musica
mixer.music.load('MusicaFondo.mp3')
mixer.music.play(-1)

#jugador
img_jugador = pygame.image.load('cohete.png')#carga la imagen
jugador_x = 368 #800/2 (mitad de la pantall) - 64/2 (la mitad del tamano del jugador)
jugador_y = 500 #500 -la altura del jugador
jugador_x_cambio = 0
jugador_y_cambio = 0

#enemigo
img_enemigo = []
enemigo_x = []
enemigo_y = []
enemigo_x_cambio = []
enemigo_y_cambio = []
cantidad_enemigos = 8

for e in range(cantidad_enemigos):
    #enemigo
    img_enemigo.append(pygame.image.load('enemigo.png'))#carga la imagen)
    enemigo_x.append(random.randint(0,736)) #800/2 (mitad de la pantall) - 64/2 (la mitad del tamano del jugador)
    enemigo_y.append(random.randint(50,200)) #600 -la altura del jugador
    enemigo_x_cambio.append(0.5)
    enemigo_y_cambio.append(50)

#bala
img_bala = pygame.image.load('bala.png')#carga la imagen
bala_x = 0 #800/2 (mitad de la pantall) - 64/2 (la mitad del tamano del jugador)
bala_y = 500 #500
bala_x_cambio = 0
bala_y_cambio = 1
bala_visible = False

#puntaje
puntaje = 0
fuente = pygame.font.Font('freesansbold.ttf',32)
texto_x = 10
texto_y = 10

#texto final del juego
fuente_final = pygame.font.Font('freesansbold.ttf',40)

def texto_final():
    mi_fuente_final = fuente_final.render('JUEGO TERMINADO',True,(255,255,255))
    pantalla.blit(mi_fuente_final,(60,200))


#funncion mostrar puntaje
def mostrar_puntaje(x,y):
    texto = fuente.render(f"puntaje : {puntaje}",True,(255,255,255)) #cxolor blanco
    pantalla.blit(texto,(x,y))

#funcion jugador
def jugador(x,y):# acepta valores para movimiento
    pantalla.blit(img_jugador,(x,y)) #pon el icono en pantalla TUPLA poscion

#funcion enemigo
def enemigo(x,y,ene):# acepta valores para movimiento
    pantalla.blit(img_enemigo[ene],(x,y)) #pon el icono en pantalla TUPLA poscion

#funcion disparar bala
def disparar_bala(x,y):
    global bala_visible
    bala_visible = True
    pantalla.blit(img_bala,(x+16,y+10)) #estas coordenadas para aparezca en medio de la bala

#funcion evaluar colision
def colision(x_1,y_1,x_2,y_2):
    distancia = math.sqrt(math.pow(x_1-x_2,2) + math.pow(y_2-y_1,2))
    if distancia < 27:
        return True
    else:
        return False
    
#loop del juego
se_ejectua = True
while se_ejectua:
    #pantalla.fill((205,144,228))#cambiar el color de 3la pantalla TUPLAS
    pantalla.blit(fondo,(0,0))
    #iterar eventos
    for evento in pygame.event.get(): #revisa los eventos
        if evento.type == pygame.QUIT: #pygame.QUIT es cuando cierra la ventana con X
            se_ejectua = False
        if evento.type == pygame.KEYDOWN:# Se presiona una tecla
            if evento.key ==pygame.K_LEFT:# si se presiona la flecha izquierda
                jugador_x_cambio = -0.5
                print('flecha izquierda')
            if evento.key ==pygame.K_RIGHT:# si se presiona la flecha derecha
                print('flecha Derecha')  
                jugador_x_cambio = +0.5
            if evento.key ==pygame.K_SPACE:# si se presiona la barra espaciadora
                sonido_bala=mixer.Sound('disparo.mp3')
                sonido_bala.play()
                if not bala_visible:
                    bala_x = jugador_x
                    disparar_bala(bala_x,bala_y) 

        if evento.type == pygame.KEYUP:# Se suelta una tecla  
            if evento.key ==pygame.K_LEFT or evento.key ==pygame.K_RIGHT:
                jugador_x_cambio = 0

    #modificar ubicacion jugador             
    jugador_x +=jugador_x_cambio

    #mantener dentro de bordes jugador
    if jugador_x<= 0:
        jugador_x = 0

    if jugador_x>= 736:# 800 - 64(tamano de la imagen)
        jugador_x = 736

    #modificar ubicacion enemigo     
    for e in range(cantidad_enemigos):
        #fin del juego
        if enemigo_y[e]> 500:
            for k in range(cantidad_enemigos):
                enemigo_y[k]= 1000
            texto_final()
            break
        enemigo_x[e] +=enemigo_x_cambio[e]

        #mantener dentro de bordes enemigo
        if enemigo_x[e]<= 0:
            enemigo_x_cambio[e] = 0.5 #rebota al llegar a un borde
            enemigo_y[e] +=enemigo_y_cambio[e] #baja al llegar a un borde
        elif enemigo_x[e]>= 736:# 800 - 64(tamano de la imagen)
            enemigo_x_cambio[e] = -0.5 #rebota al llegar a un borde
            enemigo_y[e] +=enemigo_y_cambio[e] #baja al llegar a un borde

        #colision
        hay_colision = colision(enemigo_x[e],enemigo_y[e],bala_x,bala_y)
        if hay_colision:
            sonido_colision=mixer.Sound('golpe.mp3')
            sonido_colision.play()
            bala_y =500
            bala_visible =False
            puntaje += 1
            enemigo_x[e] = random.randint(0,736) #800/2 (mitad de la pantall) - 64/2 (la mitad del tamano del jugador)
            enemigo_y[e] = random.randint(50,200) #600 -la altura del jugador
        enemigo(enemigo_x[e],enemigo_y[e],e)

    #movimiento bala
    if bala_y<= -64: #tamano de la bala
        bala_y = 500
        bala_visible =False

    if bala_visible:
        disparar_bala(bala_x,bala_y)
        bala_y-=bala_y_cambio

    jugador(jugador_x,jugador_y)
    mostrar_puntaje(texto_x,texto_y)
    #Actualizar
    pygame.display.update() #actualiza
  