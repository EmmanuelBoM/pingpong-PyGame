import pygame

def main():
    pygame.init() #inicia pygame
    size = 800,600 #tamaño de la ventana
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption("Mi primer juego")

    width, height = 800,600
    speed = [2, 2]
    white = 255, 255, 255

    #se carga una imagen
    ball = pygame.image.load('D:/users/emman/Downloads/pingpong/pelotapixar.png')
    ballrect = ball.get_rect();

    #barra de rebote
    barra = pygame.image.load('D:/users/emman/Downloads/pingpong/barra.png')
    barrarect = barra.get_rect()
    barra2 = pygame.image.load('D:/users/emman/Downloads/pingpong/barra.png')
    barrarect2 = barra2.get_rect()

    #se ubica la barra a la mita de la ventana
    barrarect.move_ip(50,260)
    barrarect2.move_ip(750, 260)

    mar1 = 0
    mar2 = 0

    fuente = pygame.font.Font(None, 50) #Tipo de fuente por default
    texto = fuente.render("Jugador 1", 0, (100,100,0)) #el segundo parametro es el borde y la ultima es el color
    texto2 = fuente.render("Jugador 2", 0, (100,100,0))
    

    
        
    run = True
    while run:
        pygame.time.delay(5) #delay que contralará la velocidad            
        
        for event in pygame.event.get(): #se captura el evento que se produce
            if event.type == pygame.QUIT:
                run = False

        #se detecta si se ha pulsado alguna tecla
        keys = pygame.key.get_pressed()

        if keys[pygame.K_w]:
            barrarect = barrarect.move(0, -1)
        if keys[pygame.K_s]:
            barrarect = barrarect.move(0, 1)

        if keys[pygame.K_UP]:
            barrarect2 = barrarect2.move(0, -1)
        if keys[pygame.K_DOWN]:
            barrarect2 = barrarect2.move(0, 1)

        #se determina si hay colisiones 
        if barrarect.colliderect(ballrect):
            speed[0] = -speed[0]
        if barrarect2.colliderect(ballrect):
            speed[0] = -speed[0]

        ballrect = ballrect.move(speed) #se mueve el objeto
        #se determinan los límites del objeto
        if ballrect.left < 0 or ballrect.right > width:
            speed[0] = -speed[0]
        if ballrect.top < 0 or ballrect.bottom > height:
            speed[1] = -speed[1]
        if ballrect.left<0:
            mar2+=1
        if ballrect.right>width:
            mar1+=1

        
        #se borra la pantalla anterior con el fondo blanco
        marcador1 = fuente.render(str(mar1), 0, (100,100,0))
        marcador2 = fuente.render(str(mar2), 0, (100,100,0))
        screen.fill(white)
        screen.blit(ball, ballrect)
        screen.blit(barra,barrarect)
        screen.blit(barra2,barrarect2)
        screen.blit(texto, (0, 0)) #Esta linea es para ubicar el texto
        screen.blit(texto2, (600,0))
        screen.blit(marcador1, (100, 40)) #Esta linea es para ubicar el texto
        screen.blit(marcador2, (700,40))
        pygame.display.flip()
    pygame.quit() #se termina el juego

if __name__ == "__main__":
    main()