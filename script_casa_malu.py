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
        return

    width, height = 800, 600
    window = glfw.create_window(width, height, "OpenGL Casa", None, None)

    if not window:
        glfw.terminate()
        return

    glfw.make_context_current(window)

    glOrtho(0, width, 0, height, -1, 1)
    glClearColor(0.0, 0.0, 0.0, 1.0)

    while not glfw.window_should_close(window):
        glfw.poll_events()

        glClear(GL_COLOR_BUFFER_BIT)
#quadrado 1: linhas verticais
        draw_line(300, 350, 300, 250)
        draw_line(400, 350, 400, 250)
#linhas horizontais     
        draw_line(300, 350, 400, 350)
        draw_line(300, 250, 400, 250)
        
        
        
#quadrado 2: linhas horizontais     

   
        draw_line(350, 300, 350, 400)
        draw_line(350, 400, 400, 400)
# linhas verticais
        draw_line(400, 400, 400, 300)
        draw_line(350, 300, 400, 300)
        
        draw_line(325, 400, 300, 350) 
        draw_line(325, 400, 350, 350)
        
        glfw.swap_buffers(window)
        
    glfw.terminate()

if __name__ == "__main__":
    main()   
   
