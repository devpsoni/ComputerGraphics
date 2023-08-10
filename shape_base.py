from OpenGL.GL import *

class Shape:
    # Initialization with vertices and edges
    def __init__(self, vertices=[], edges=[]):
        self.vertices = vertices
        self.edges = edges

    # Method to draw the shape using OpenGL commands
    def draw(self):
        glBegin(GL_LINES)
        for edge in self.edges:
            for vertex in edge:
                glVertex2fv(self.vertices[vertex])
        glEnd()
