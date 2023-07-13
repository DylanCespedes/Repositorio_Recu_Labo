import pygame
import colores

def crear(x,y,ancho,alto):
    dic_personaje = {}
    dic_personaje["surface"] = pygame.image.load("Pou.png")
    dic_personaje["surface"] = pygame.transform.scale(dic_personaje["surface"], (ancho,alto))
    dic_personaje["rect_pos"] = pygame.Rect(x,y,45,100)
    dic_personaje["rect"] = pygame.Rect(x+ancho/4-0,y+60,50,20)
    dic_personaje["score"] = 0
    dic_personaje["vidas"] = 3
    return dic_personaje

def actualizar_pantalla(personaje,window):
    window.blit(personaje["surface"], personaje["rect_pos"])
    #pygame.draw.rect(window, colores.ROJO,personaje["rect"])

def update(personaje, incremento_x):
    nueva_x = personaje["rect_pos"].x + incremento_x
    if(nueva_x > 0 and nueva_x < 600):
        personaje["rect_pos"].x = personaje["rect_pos"].x + incremento_x
        personaje["rect"].x = personaje["rect"].x + incremento_x
