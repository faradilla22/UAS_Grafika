import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
from Cube import Cube
from Pyramid import Pyramid
from Prism import Prism

# Initialize Pygame
pygame.init()

# Set up display
display = (800, 600)
pygame.display.set_mode(display, DOUBLEBUF | OPENGL)

# Set up perspective
gluPerspective(45, (display[0] / display[1]), 0.1, 50.0)
glTranslatef(0.0, 0.0, -5)

# Initialize objects
cube = Cube()
pyramid = Pyramid()
prism = Prism()
objects = [cube, pyramid, prism]
current_object = 0

# Variables to track mouse movement and button state
dragging = False
prev_mouse_pos = (0, 0)

def draw_current_object():
    global objects, current_object
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    objects[current_object].draw()
    pygame.display.flip()

def rotate_obj(axis, angle):
    glRotatef(angle, *axis)

def scale_obj(scale_factor):
    glScalef(scale_factor, scale_factor, scale_factor)

# Main loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
            
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:  # Left mouse button
            dragging = True
            prev_mouse_pos = pygame.mouse.get_pos()
        elif event.type == pygame.MOUSEBUTTONUP and event.button == 1:
            dragging = False
        elif event.type == pygame.KEYDOWN:

            if event.key == pygame.K_SPACE:  # Switch object on spacebar press
                current_object = (current_object + 1) % len(objects)

            elif event.key == pygame.K_q:  # Translate object on x-axis positive
                glTranslatef(0.1, 0, 0)
            elif event.key == pygame.K_w:  # Translate object on x-axis negative
                glTranslatef(-0.1, 0, 0)
            elif event.key == pygame.K_e:  # Translate object on y-axis positive
                glTranslatef(0, 0.1, 0)
            elif event.key == pygame.K_r:  # Translate object on y-axis negative
                glTranslatef(0, -0.1, 0)
            elif event.key == pygame.K_t:  # Translate object on z-axis positive
                glTranslatef(0, 0, 0.1)
            elif event.key == pygame.K_y:  # Translate object on z-axis negative
                glTranslatef(0, 0, -0.1)

            elif event.key == pygame.K_a:  # Rotate object on x-axis positive
                rotate_obj((1, 0, 0), 1)
            elif event.key == pygame.K_s:  # Rotate object on x-axis negative
                rotate_obj((1, 0, 0), -1)
            elif event.key == pygame.K_d:  # Rotate object on y-axis positive
                rotate_obj((0, 1, 0), 1)
            elif event.key == pygame.K_f:  # Rotate object on y-axis negative
                rotate_obj((0, 1, 0), -1)
            elif event.key == pygame.K_g:  # Rotate object on z-axis positive
                rotate_obj((0, 0, 1), 1)
            elif event.key == pygame.K_h:  # Rotate object on z-axis negative
                rotate_obj((0, 0, 1), -1)

            elif event.key == pygame.K_z:  # Scale object on x-axis
                scale_obj(0.9)
            elif event.key == pygame.K_x:  # Scale object on x-axis
                scale_obj(1.1)
            elif event.key == pygame.K_c:  # Scale object on y-axis
                scale_obj(0.9)
            elif event.key == pygame.K_v:  # Scale object on y-axis
                scale_obj(1.1)
            elif event.key == pygame.K_b:  # Scale object on z-axis
                scale_obj(0.9)
            elif event.key == pygame.K_n:  # Scale object on z-axis
                scale_obj(1.1)

    if dragging:
        # Get current mouse position and calculate movement since last frame
        cur_mouse_pos = pygame.mouse.get_pos()
        dx, dy = cur_mouse_pos[0] - prev_mouse_pos[0], cur_mouse_pos[1] - prev_mouse_pos[1]

        # Update perspective based on mouse movement
        glRotatef(0.5 * dx, 0, 1, 0)
        glRotatef(0.5 * dy, 1, 0, 0)
        prev_mouse_pos = cur_mouse_pos

    draw_current_object()
    pygame.time.wait(10)