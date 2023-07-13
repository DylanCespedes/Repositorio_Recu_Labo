import pygame
import colores

#Clase Titulo y boton para crear un menu principal y un menu de pausa

class Titulo:
    def __init__(self, x, y, texto):
        self.x = x
        self.y = y
        self.texto = texto

    def dibujar(self, pantalla):
        fuente = pygame.font.SysFont("Pou", 48)
        texto_render = fuente.render(self.texto, True, colores.BLANCO)
        texto_rect = texto_render.get_rect(center=(self.x, self.y))
        pantalla.blit(texto_render, texto_rect)

#Clase Boton
class Boton:
    def __init__(self, x, y, ancho, alto, texto):
        self.rect = pygame.Rect(x, y, ancho, alto)
        self.texto = texto

    def dibujar(self, pantalla):
        pygame.draw.rect(pantalla, colores.BLANCO, self.rect)
        fuente = pygame.font.SysFont("Pou", 35)
        texto_render = fuente.render(self.texto, True, colores.NEGRO)
        texto_rect = texto_render.get_rect(center=self.rect.center)
        pantalla.blit(texto_render, texto_rect)

    def verificar_click(self, pos):
        return self.rect.collidepoint(pos)

#Clase nivel

class Nivel:
    def __init__(self, imagen, ancho, alto):
        self.imagen = pygame.image.load(imagen).convert()
        self.imagen = pygame.transform.scale(self.imagen, (ancho, alto))

    def dibujar(self, pantalla):
        pantalla.blit(self.imagen, (0, 0))

#Creo una clase de error personalizado

class MenuError(Exception):
    pass