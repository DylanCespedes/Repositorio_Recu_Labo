import pygame
import colores
import random

########################################### COMIDA ##########################################

def crear(x,y, ancho, alto):

    imagenes_comida = ["dona.png", "papas_fritas.png", "pancho.png", "pizza.png", "Hamburguesa.png", "pescado.png", "paleta.png", "sushi.png"]
    imagen_comida = pygame.image.load(random.choice(imagenes_comida))
    imagen_comida = pygame.transform.scale(imagen_comida, (ancho, alto))
    rect_comida = imagen_comida.get_rect()
    rect_comida.x = x
    rect_comida.y = y
    dict_comida = {}
    dict_comida["surface"] = imagen_comida
    dict_comida["rect"] = rect_comida
    dict_comida["visible"] = True
    dict_comida["speed"] = random.randrange(10, 20, 1)

    return dict_comida

def update(lista_comida):
    for comida in lista_comida:
        rect_comida = comida["rect"]
        rect_comida.y = rect_comida.y + comida["speed"]

def actualizar_pantalla(lista_comida, personaje, window):
    for comida in lista_comida:
        if(personaje["rect"].colliderect(comida["rect"])):
            personaje["score"] = personaje["score"] + 1
            restar_comida(comida)
        
        if(comida["rect"].y > 880):
            restar_comida(comida)
        window.blit(comida["surface"], comida["rect"])

    font = pygame.font.SysFont("Pou", 50)
    text = font.render("SCORE: {0}".format(personaje["score"]), True, (255, 0, 0))
    window.blit(text, (0,0))

def crear_lista_comida(cantidad):
    lista_comida = []
    for i in range(cantidad):
        y = random.randrange(-1000, 0, 60)
        x = random.randrange(0, 740, 60)
        comida = crear(x, y, 60, 60)
        lista_comida.append(comida)
    return lista_comida

cantidad_imagenes = 8
lista_comida = crear_lista_comida(cantidad_imagenes)

def restar_comida(comida):
    y = random.randrange(-1000, 0, 60)
    x = random.randrange(0, 740, 60)
    comida["rect"].x = random.randrange(0, 740, 60)
    comida["rect"].y = random.randrange(-1000, 0, 60)

#def eliminar_comida(comida):