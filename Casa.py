import glfw
from OpenGL.GL import *
from OpenGL.GLU import *
import math

def draw_line(start1, end1, start2, end2):
    glColor3f(0.0, 0.0, 1.0)
    glBegin(GL_LINE_STRIP)
    glVertex2f(start1, end1)
    glVertex2f(start2, end2)
    glEnd()

def main():

    if not glfw.init():
        raise Exception ("glfw can not be initialized")
    
    width, height = 1280, 720
    window = glfw.create_window(width, height, "Camisa", None, None)

    if not window:
        glfw.terminate()
        raise Exception ("glfw window can not be created")

    glfw.set_window_pos(window, 400, 200)

    glfw.make_context_current(window)

    glClearColor(0, 0.1, 0.1, 1)
    glOrtho(0, width, 0, height, -1, 1)

    while not glfw.window_should_close(window):
        glfw.poll_events()

        glClear(GL_COLOR_BUFFER_BIT)
#Linhas laterais
        draw_line(550, 450, 550, 290)
        draw_line(750, 450, 750, 290)
#Linha Inferior
        draw_line(550, 290, 750, 290)   
#Linha Superior
        draw_line(550, 450, 750, 450)
#Telhado
        draw_line(550, 450, 650, 550)
        draw_line(650, 550, 750, 450)
#Porta
        draw_line(640, 290, 640, 335)
        draw_line(640, 335, 665, 335)
        draw_line(665, 335, 665, 290)
        draw_line(658, 310, 660, 310)
#Janela Esquerda
        #Laterais
        draw_line(580, 420, 580, 375)
        draw_line(620, 375, 620, 420)
        #Superiores
        draw_line(580, 375, 620, 375)
        draw_line(620, 420, 580, 420)
        #Dentro
        draw_line(600, 420, 600, 375)
        draw_line(580, 398, 620, 398)
#Janela Superior
        draw_line(630, 470, 670, 470)
        draw_line(630, 510, 670, 510)
        draw_line(630,470, 630, 510)
        draw_line(670,470, 670, 510)
        #Dentro
        draw_line(650, 470, 650,510)
        draw_line(630, 490, 670, 490)
#Chaminé
        draw_line(700, 500, 700, 550)
        draw_line(700, 550, 730, 550)
        draw_line(730, 550, 730, 470)
        
        glfw.swap_buffers(window)

    glfw.terminate()

if __name__ == "__main__":
    main()  