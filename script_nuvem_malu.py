import glfw
from OpenGL.GL import *
from OpenGL.GLU import *
import math

def draw_circle(radius, num_segments, centerx, centery, size):
    glColor3f(1.0, 1.0, 1.0)
    glBegin(GL_TRIANGLE_FAN)
    glVertex2f(centerx, centery)
    for i in range(int((num_segments + 1)*size)):
        theta = (i / num_segments) * 2.0 * math.pi
        x = radius * math.cos(theta)
        y = radius * math.sin(theta)
        glVertex2f(x+centerx, y+centery)
    glEnd()
def main():
    if not glfw.init():
        return

    width, height = 800, 600
    window = glfw.create_window(width, height, "OpenGL Circle", None, None)

    if not window:
        glfw.terminate()
        return

    glfw.make_context_current(window)

    glOrtho(0, width, 0, height, -1, 1)
    glClearColor(0.0, 0.0, 0.0, 1.0)

    radius = 100
    num_segments = 100

    while not glfw.window_should_close(window):
        glfw.poll_events()

        glClear(GL_COLOR_BUFFER_BIT)

        draw_circle(radius, num_segments, 400, 310, 1)
        draw_circle(radius, num_segments, 300, 250, 1)
        draw_circle(radius, num_segments, 200, 150, 1)
        draw_circle(radius, num_segments, 360, 120, 1)
        draw_circle(radius, num_segments, 500, 120, 1)
        draw_circle(radius, num_segments, 450, 220, 1)
        glfw.swap_buffers(window)
        
    glfw.terminate()

if __name__ == "__main__":
    main()
