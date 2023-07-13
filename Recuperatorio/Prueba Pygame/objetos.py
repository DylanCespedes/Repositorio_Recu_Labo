import pygame
import colores
import random

########################################### OBJETOS ##########################################

def crear_malo(x,y, ancho, alto):

    imagenes_objetos = ["CD.png", "zapato.png", "herradura.png", "avion.png"]
    imagen_objetos = pygame.image.load(random.choice(imagenes_objetos))
    imagen_objetos = pygame.transform.scale(imagen_objetos, (ancho, alto))
    rect_objeto = imagen_objetos.get_rect()
    rect_objeto.x = x
    rect_objeto.y = y
    dict_objeto = {}
    dict_objeto["surface"] = imagen_objetos
    dict_objeto["rect"] = rect_objeto
    dict_objeto["visible"] = True
    dict_objeto["speed"] = random.randrange(10, 20, 1)

    return dict_objeto

def update(lista_objeto):
    for objeto in lista_objeto:
        rect_objeto = objeto["rect"]
        rect_objeto.y = rect_objeto.y + objeto["speed"]

def actualizar_pantalla(lista_objeto, personaje, window):
    for objeto in lista_objeto:
        if(personaje["rect"].colliderect(objeto["rect"])):
            personaje["vidas"] -= 1
            restar_objetos(objeto)
        
        objeto["rect"].y += objeto["speed"]
        if(objeto["rect"].y > 880):
            restar_objetos(objeto)
        window.blit(objeto["surface"], objeto["rect"])

    font = pygame.font.SysFont("Pou", 50)
    text = font.render("Vidas: {0}".format(personaje["vidas"]), True, (255, 0, 0))
    window.blit(text, (550,0))

def crear_lista_objeto(cantidad):
    lista_objeto = []
    for i in range(cantidad):
        y = random.randrange(-1000, 0, 60)
        x = random.randrange(0, 740, 60)
        objeto = crear_malo(x, y, 60, 60)
        lista_objeto.append(objeto)
    return lista_objeto

cantidad_imagenes = 4
lista_malos = crear_lista_objeto(cantidad_imagenes)

def restar_objetos(objeto):
    y = random.randrange(-1000, 0, 60)
    x = random.randrange(0, 740, 60)
    objeto["rect"].x = random.randrange(0, 740, 60)
    objeto["rect"].y = random.randrange(-1000, 0, 60)

def mostrar_game_over(window):
    fuente = pygame.font.SysFont("Pou", 30)
    texto = fuente.render("Game Over", True, (colores.ROJO))
    rect_text = texto.get_rect(center=(window.get_width() / 2, window.get_height() / 30))
    window.blit(texto, rect_text)

