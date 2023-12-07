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
#Initializing glfw library
    if not glfw.init():
        raise Exception ("glfw can not be initialized")
    
    width, height = 1280, 720
    window = glfw.create_window(width, height, "Camisa", None, None)


    #creating a window
    # window = glfw.create_window(1280, 720, "My OpenGL window", None, None)

    #check if window was created
    if not window:
        glfw.terminate()
        raise Exception ("glfw window can not be created")

    #Set window's position
    glfw.set_window_pos(window, 400, 200)

    #Make the context current
    glfw.make_context_current(window)

    glClearColor(0, 0.1, 0.1, 1)
    glOrtho(0, width, 0, height, -1, 1)

    #The main application loop
    while not glfw.window_should_close(window):
        glfw.poll_events()

        glClear(GL_COLOR_BUFFER_BIT)

        draw_line(550, 450, 550, 290)
        draw_line(680, 450, 680, 290)
        draw_line(550, 290, 680, 290)

        glfw.swap_buffers(window)

    #terminate glfw, free up allocated resources
    glfw.terminate()

if __name__ == "__main__":
    main()  