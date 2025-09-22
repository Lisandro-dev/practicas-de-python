import pygame
import random
import math
from pygame import mixer


# Inicialización de Pygame
pygame.init()
# Configuración de la pantalla
pantalla = pygame.display.set_mode((800, 600))
puntaje=0
fuente=pygame.font.Font('freesansbold.ttf',32)
textox=10
textoy=10

def mostrar_puntaje(x,y):
    texto=f"puntaje: {puntaje}"
    texto_renderizado=fuente.render(texto,True,(255,255,255))
    pantalla.blit(texto_renderizado,(x,y))
# Título de la ventana
pygame.display.set_caption("Invasión Espacial")
icono=pygame.image.load('ovni.png')
pygame.display.set_icon(icono)

#fondo de pantalla
fondo=pygame.image.load('Fondo.jpg')

#música de fondo
mixer.music.load('MusicaFondo.mp3')
mixer.music.play(-1)

#Jugador variables
img_jugador=pygame.image.load('cohete.png')
jugadorx=368
jugadory=500
jugadorx_cambio=0
jugadory_cambio=0
#funcion jugador
def jugador(x,y):
    pantalla.blit(img_jugador,(x,y))

#enemigo variables
img_enemigo=[]
enemigox=[]
enemigoy=[]
enemigox_cambio=[]
enemigoy_cambio=[]
cantidad_enemigos=6

for e in range(cantidad_enemigos):
    img_enemigo.append(pygame.image.load('enemigo.png'))
    enemigox.append(random.randint(0,736))
    enemigoy.append(random.randint(50,200))
    enemigox_cambio.append(random.choice([0.2, 0.3, 0.4]))
    enemigoy_cambio.append(50)


#funcion enemigo
def enemigo(x,y, ene):
    pantalla.blit(img_enemigo[ene],(x,y))

#bala variables
img_bala=pygame.image.load('bala.png')
balax=0
balay=500
balax_cambio=0
balay_cambio=3
balay_estado= False  # listo - no se ve, disparo - se


#funcion disparar bala
def disparar_bala(x,y):
    global balay_estado
    balay_estado=True
    pantalla.blit(img_bala,(x + 16,y +10))

#Función para detectar colisiones
def hay_colision(x1, y1, x2, y2):
    distancia = math.sqrt((math.pow(x1-x2, 2)) + (math.pow(y2-y1, 2)))
    if distancia < 27:
        return True
    else:
        return False

# Bucle principal enemigogo
se_ejecuta = True
while se_ejecuta:
          
    pantalla.blit(fondo, (0,0))  # Rellenr la pantalla con un color

    # Manejo de eventos
    #cierre de ventana
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            se_ejecuta = False
    #presionar teclas        
        if evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_LEFT:
                jugadorx_cambio=-1
            if evento.key == pygame.K_RIGHT:
                jugadorx_cambio=1
            if evento.key == pygame.K_UP:
                jugadory_cambio=-0.1
            if evento.key == pygame.K_DOWN:
                jugadory_cambio=0.1   
            if evento.key == pygame.K_SPACE:
                if balay_estado==False:
                    balax=jugadorx
                    disparar_bala(balax,balay)
                    print("Disparo")
    #soltar teclas             
        if evento.type == pygame.KEYUP:
            if evento.key == pygame.K_LEFT or evento.key == pygame.K_RIGHT:
                print("Tecla soltada")
    #modificar ubicacion jugador            
    jugadorx+=jugadorx_cambio

    #movimiento bala
    if balay<=64:
        balay=500
        balay_estado=False
    
    if balay_estado==True:
        sonidodisparo=mixer.Sound('disparo.mp3')
        sonidodisparo.play()
        disparar_bala(balax,balay)
        balay-=balay_cambio

    #mantener dentro de la pantalla jugador
    if jugadorx<=0:
        jugadorx=0  
    elif jugadorx>=736:
        jugadorx=736
    #modificar ubicacion enemigo        
    for e in range(cantidad_enemigos):
        #fin del juego
        if enemigoy[e]>440:
            for k in range(cantidad_enemigos):
                enemigoy[k]=2000
            texto_final=fuente.render("JUEGO TERMINADO",True,(255,255,255))
            pantalla.blit(texto_final,(300,200))
            break
        enemigox[e]+=enemigox_cambio[e]

    #mantener dentro de la pantalla enemigo
        if enemigox[e]<=0:
            enemigox_cambio[e]=0.7 
            enemigoy[e]+=enemigoy_cambio[e]
        elif enemigox[e]>=736:
            enemigox_cambio[e]=-0.7
            enemigoy[e]+=enemigoy_cambio[e]
        #colicion   
        colision=hay_colision(enemigox[e], enemigoy[e], balax, balay)
        if colision:
            sonidocolision=mixer.Sound('Golpe.mp3')
            sonidocolision.play()
            balay=500
            balay_estado=False
            puntaje+=1
            enemigox[e]=random.randint(0,736)
            enemigoy[e]=random.randint(50,200)
        enemigo(enemigox[e],enemigoy[e], e)

    jugador(jugadorx,jugadory)
    mostrar_puntaje(textox,textoy)

    #actualizar ubicacion nave
    pygame.display.update()  # Actualizar la pantalla


