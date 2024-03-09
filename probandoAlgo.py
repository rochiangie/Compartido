import pygame
import time

def reproducir_musica():
    pygame.mixer.init()
    pygame.mixer.music.load("music.mp3")
    pygame.mixer.music.play(-1)  # -1 para reproducir en bucle

def mostrar_panel_informativo():
    print("¡Bienvenido al Gestor de Emociones!")
    print("Escucha la música tranquila de fondo y cuéntame cómo te sientes.")

def obtener_estado_emocional():
    estado_emocional = input("¿Cómo te sientes hoy? Describe tus emociones: ")
    return estado_emocional

def main():
    mostrar_panel_informativo()
    reproducir_musica()
    
    while True:
        estado_emocional = obtener_estado_emocional()
        print("Gracias por compartir tus emociones.")
        print("------------------------------")

if __name__ == "__main__":
    main()
