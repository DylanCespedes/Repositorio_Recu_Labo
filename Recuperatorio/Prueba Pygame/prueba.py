import pygame
import objetos
import colores
import personaje 
import Clases
import sqlite
import comida

import random
import sys
import sqlite3
import pygame_gui

ANCHO_PANTALLA = 772
ALTO_PANTALLA = 697

posicion_fondo = (0, 0)

pygame.init()

window = pygame.display.set_mode((ANCHO_PANTALLA, ALTO_PANTALLA))
pygame.display.set_caption("POU - FOOD DROP")

MANAGER = pygame_gui.UIManager((ANCHO_PANTALLA, ALTO_PANTALLA))
Text_input = pygame_gui.elements.UITextEntryLine(relative_rect=pygame.Rect((140, 200), (500, 50)), manager=MANAGER, 
                                                 object_id="#main_text_entry")

#Botones del menu
boton_jugar = Clases.Boton(270, 200, 200, 50, "Jugar")
boton_ver_puntaje = Clases.Boton(250, 300, 240, 50, "Ver Puntaje")
boton_salir = Clases.Boton(270, 400, 200, 50, "Salir")
botones = [boton_jugar, boton_salir, boton_ver_puntaje]

#Botones del menu de pausa

boton_volver_menu = Clases.Boton(250, 300, 270, 50, "Volver al menu")
botones_pausa = [boton_volver_menu]

#boton del menu de puntaje

boton_volver_menu = Clases.Boton(245, 500, 280, 50, "Volver al menu")
boton_puntaje = [boton_volver_menu]

#Botones game over

boton_volver_menu_game_over = Clases.Boton(250, 500, 270, 50, "Volver al menu")

botones_game_over = [boton_volver_menu_game_over]

#Fondo de nivel

nivel_1 = Clases.Nivel("Food Drip Pou nivel 1.jpg", 772, 697)
nivel_2 = Clases.Nivel("Food Drip Pou nivel 2.jpg", 772, 697)
nivel_3 = Clases.Nivel("Food Drip Pou nivel 3.jpg", 772, 697)

nivel_1_puntaje_maximo = 15
nivel_2_puntaje_maximo = 30

nivel_actual = nivel_1

#TIMER
timer = pygame.USEREVENT
pygame.time.set_timer(timer, 100)

#tamanio del personaje

player = personaje.crear(ANCHO_PANTALLA/2,ALTO_PANTALLA-100,100,100)

#tamanio de las listas del nivel 1

lista_comida = comida.crear_lista_comida(6)
lista_comida_mala = objetos.crear_lista_objeto(2)

#tamanio de las listas del nivel 2

lista_comida_modificada_nivel_2 = comida.crear_lista_comida(3)
lista_objetos_modificado_nivel_2 = objetos.crear_lista_objeto(6)

#tamanio de las listas del nivel 3

lista_comida_modificada_nivel_3 = comida.crear_lista_comida(2)
lista_objetos_modificado_nivel_3 = objetos.crear_lista_objeto(8)

#Musica

musica_fondo = pygame.mixer.Sound('Musiquita Pou.mp3')

musica_fondo_2 = pygame.mixer.Sound('pou peruano.mp3')

musica_fondo_3 = pygame.mixer.Sound('musiquita pou nivel 3.mp3')

musica_fondo_game_over = pygame.mixer.Sound("Game Over Pou.mp3")

volumen = 0.1

musica_fondo.set_volume(volumen)

musica_fondo_2.set_volume(volumen)

musica_fondo_3.set_volume(volumen)

#fuente del puntaje

fuente_puntaje = pygame.font.SysFont("Pou", 30)

#Ingreso del usuario

def get_user():
    
    while True:

        UI_REFRESH_RATE = clock.tick(30)/1000

        titulo_ingresar = Clases.Titulo(ANCHO_PANTALLA // 2, 120, "Nombre:")

        titulo_nivel_2 = Clases.Titulo(135, 20, "Nivel 2 = " + str(nivel_1_puntaje_maximo))

        titulo_nivel_3 = Clases.Titulo(635, 20, "Nivel 3 = " + str(nivel_2_puntaje_maximo))

        imagen_de_input = pygame.image.load('Instrucciones.png')

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame_gui.UI_TEXT_ENTRY_FINISHED and event.ui_object_id == "#main_text_entry":
                nombre_jugador = str(event.text)
                return nombre_jugador

            MANAGER.process_events(event)                          

        pygame.display.update()

        window.fill(colores.GRIS)
        window.blit(imagen_de_input, (0,302))
        titulo_ingresar.dibujar(window)
        titulo_nivel_2.dibujar(window)
        titulo_nivel_3.dibujar(window)
        MANAGER.update(UI_REFRESH_RATE)
        MANAGER.draw_ui(window)

        pygame.display.update()

def menu_pausa():

    pygame.init()

    musica_fondo.stop()

    musica_fondo_2.stop()

    musica_fondo_3.stop()

    titulo = Clases.Titulo(ANCHO_PANTALLA // 2, 100, "Pausa")

    while True:
        lista_evento_pausa = pygame.event.get()

        for evento in lista_evento_pausa:
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            elif evento.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                if boton_volver_menu.verificar_click(pos) == False:
                    return True
            elif evento.type == pygame.KEYDOWN and evento.key == pygame.K_ESCAPE:
                return False
            
        window.fill(colores.CELESTE)
        titulo.dibujar(window)
        for boton in botones_pausa:
            boton.dibujar(window)
        pygame.display.flip()

#Reloj de juego
clock = pygame.time.Clock()

bandera_correr_puntaje = True

bandera_nivel_2 = False

bandera_nivel_3 = False

bandera_correr = True

bandera_game_over = False

bandera_pausa = False

bandera_juego_terminado = False

while bandera_correr:
    
    titulo = Clases.Titulo(ANCHO_PANTALLA // 2, 100, "Pou - FOOD DROP")

    musica_fondo.stop()

    lista_evento = pygame.event.get()

    for evento in lista_evento:
        if evento.type == pygame.QUIT:
            bandera_correr = False   

        elif evento.type == pygame.MOUSEBUTTONDOWN:
                if evento.button == 1:
                    pos = pygame.mouse.get_pos()
                    for boton in botones:
                        if boton.verificar_click(pos):
                            if boton == boton_jugar:
                                
                                nombre_jugador = get_user()

                                pygame.time.set_timer(timer, 100)
                                en_pausa = False

                                musica_fondo.play(-1)

                                while bandera_correr:
                                    
                                    lista_evento = pygame.event.get()

                                    bandera_correr = True

                                    #bandera_game_over = False

                                    if bandera_pausa == True:
                                        bandera_pausa = False
                                        bandera_nivel_2 = False
                                        bandera_nivel_3 = False
                                        bandera_game_over = False

                                        player = personaje.crear(ANCHO_PANTALLA/2,ALTO_PANTALLA-100,100,100)
                                        lista_comida = comida.crear_lista_comida(6)
                                        lista_comida_mala = objetos.crear_lista_objeto(2)
                                        break

                                    for evento in lista_evento:
                                        if evento.type == pygame.QUIT:
                                            bandera_correr = False

                                        if evento.type == pygame.KEYDOWN and evento.key == pygame.K_ESCAPE:
                                            en_pausa = not en_pausa
                                            bandera_pausa = menu_pausa()
                                 
                                    if not en_pausa:
                                        if evento.type == pygame.USEREVENT and evento.type == timer:
                                            if evento.type == timer:
                                                comida.update(lista_comida)

                                        lista_teclas = pygame.key.get_pressed()
            
                                        if lista_teclas[pygame.K_LEFT]:
                                            personaje.update(player, -20)

                                        if lista_teclas[pygame.K_RIGHT]:
                                            personaje.update(player, 20)

                                        window.fill(colores.NEGRO)
                                        if bandera_nivel_2 == False and bandera_nivel_3 == False:
                                            nivel_actual.dibujar(window)
                                        elif bandera_nivel_2 == True and bandera_nivel_3 == False:
                                            nivel_2.dibujar(window)
                                        elif bandera_nivel_3 == True and bandera_nivel_2 == True:
                                            nivel_3.dibujar(window)
                                            
                                        personaje.actualizar_pantalla(player, window)
                                        comida.actualizar_pantalla(lista_comida,player,window)
                                        objetos.actualizar_pantalla(lista_comida_mala, player, window)

                                        if player["score"] >= nivel_1_puntaje_maximo and bandera_nivel_2 == False:
                                            
                                            lista_comida = lista_comida_modificada_nivel_2
                                            lista_comida_mala = lista_objetos_modificado_nivel_2

                                            musica_fondo.stop()

                                            musica_fondo_2.play(-1)

                                            window.fill(colores.ROJO)
                                            personaje.actualizar_pantalla(player, window)
                                            
                                            pygame.display.flip()
                                            clock.tick(30)

                                            bandera_nivel_2 = True
                                        
                                        elif player["score"] >= nivel_2_puntaje_maximo and bandera_nivel_3 == False:
                                            
                                            lista_comida = lista_comida_modificada_nivel_3
                                            lista_comida_mala = lista_objetos_modificado_nivel_3
                                            
                                            musica_fondo_2.stop()

                                            musica_fondo_3.play(-1)

                                            window.fill(colores.VERDE)
                                            personaje.actualizar_pantalla(player, window)

                                            pygame.display.flip()
                                            clock.tick(30)

                                            bandera_nivel_3 = True

                                        if player['vidas'] <= 0 and bandera_game_over == False:

                                            sqlite.insertar_puntaje(nombre_jugador, player['score'])
                                            
                                            bandera_nivel_2 = False
                                            bandera_nivel_3 = False

                                            window.fill(colores.CELESTE)
                                            objetos.mostrar_game_over(window)

                                            titulo_top = Clases.Titulo(ANCHO_PANTALLA // 2, 100, "Top mejores")

                                            puntajes = sqlite.obtener_puntaje()
                                            pos_y = 150

                                            for jugador, puntaje in puntajes:
                                                texto_puntaje = fuente_puntaje.render(f"{jugador}: {puntaje}", True, colores.NEGRO)
                                                window.blit(texto_puntaje, (280, pos_y))
                                                pos_y += 25
                                            
                                            en_pausa = not en_pausa
                                            bandera_game_over = True

                                            musica_fondo.stop()

                                            musica_fondo_2.stop()

                                            musica_fondo_3.stop()

                                            musica_fondo_game_over.play()
                                        
                                            while bandera_game_over:

                                                event_list = pygame.event.get()
                                                for event in event_list:
                                                        if event.type == pygame.QUIT:
                                                            pygame.quit()
                                                            sys.exit()

                                                        elif event.type == pygame.MOUSEBUTTONDOWN:
                                                            pos = pygame.mouse.get_pos()
                                                            if boton_volver_menu.verificar_click(pos) == True:
                                                                bandera_game_over = False
                                                                bandera_pausa = True
                                                                break

                                                titulo_top.dibujar(window)
                                                for boton in botones_game_over:
                                                    boton.dibujar(window)
                                                pygame.display.flip()    

                                        pygame.display.flip()
                                        clock.tick(30)

                            elif boton == boton_ver_puntaje:
                                while bandera_correr_puntaje:  
                                    for evento in pygame.event.get():
                                        if evento.type == pygame.QUIT:
                                            bandera_correr_puntaje = False 
                                            en_pausa = True

                                    for evento in lista_evento:
                                            if evento.type == pygame.QUIT:
                                                bandera_correr = False

                                            elif evento.type == pygame.MOUSEBUTTONDOWN:
                                                if evento.button == 1:
                                                    pos_puntaje = pygame.mouse.get_pos()
                                                    for boton in boton_puntaje:
                                                        if boton.verificar_click(pos_puntaje):
                                                            bandera_correr_puntaje = False
                                    
                                    titulo_puntaje = Clases.Titulo(ANCHO_PANTALLA // 2, 100, "Top 5 mejores")

                                    puntajes = sqlite.obtener_puntaje()
                                    pos_y = 150
                                    window.fill(colores.AZUL)

                                    for jugador, puntaje in puntajes:
                                        texto_puntaje = fuente_puntaje.render(f"{jugador}: {puntaje}", True, colores.NEGRO)
                                        window.blit(texto_puntaje, (300, pos_y))
                                        pos_y += 25

                                    titulo_puntaje.dibujar(window)
                                    for boton in boton_puntaje:
                                        boton.dibujar(window)
                                    pygame.display.flip()
                                                    
                                    if len(sqlite.puntajes) == 0:
                                        raise Clases.MenuError("No se encontro ningun puntaje creado!!!")
                                                   
                            else:
                                pygame.quit()
                                sys.exit()

    window.fill(colores.CELESTE)
    titulo.dibujar(window)
    for boton in botones:
        boton.dibujar(window)
    pygame.display.flip()

pygame.quit()