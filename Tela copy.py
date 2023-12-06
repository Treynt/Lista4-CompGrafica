import glfw
from OpenGL.GL import *

#Initializing glfw library
if not glfw.init():
    raise Exception ("glfw can not be initialized")

#creating a window
window = glfw.create_window(1280, 720, "My OpenGL window", None, None)

#check if window was created
if not window:
    glfw.terminate()
    raise Exception ("glfw window can not be created")

#Set window's position
glfw.set_window_pos(window, 400, 200)

#Make the context current
glfw.make_context_current(window)

glClearColor(0, 0.1, 0.1, 1)

#The main application loop
while not glfw.window_should_close(window):
    glfw.poll_events()

    glClear(GL_COLOR_BUFFER_BIT)

    glfw.swap_buffers(window)

#terminate glfw, free up allocated resources
glfw.terminate()