import glfw
from OpenGL.GL import *


if not glfw.init():
    raise Exception ("glfw can not be initialized")

window = glfw.create_window(1280, 720, "My OpenGL window", None, None)

if not window:
    glfw.terminate()
    raise Exception ("glfw window can not be created")

glfw.set_window_pos(window, 400, 200)

glfw.make_context_current(window)

glClearColor(0, 0.1, 0.1, 1)

while not glfw.window_should_close(window):
    glfw.poll_events()

    glClear(GL_COLOR_BUFFER_BIT)

    glfw.swap_buffers(window)

glfw.terminate()