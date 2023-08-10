import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *

def initialize_display(width=800, height=800):
    """Set up the Pygame display and orthogonal 2D projection."""
    pygame.init()
    pygame.display.set_mode((width, height), DOUBLEBUF|OPENGL)
    
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(0, width, 0, height, -1, 1)  # Define 2D orthographic projection
    glMatrixMode(GL_MODELVIEW)

    glTranslatef(width / 2, height / 2, 0)  # Center the 2D content

    return (width, height)

def handle_events():
    """Process any Pygame events. Quit if close button pressed."""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

def update_display():
    """Update the display by flipping buffers and waiting."""
    pygame.display.flip()
    pygame.time.wait(10)

def basic_transformations():
    """Perform basic transformations like rotation and clearing buffers."""
    glRotatef(1, 3, 1, 1)
    glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
