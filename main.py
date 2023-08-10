import pygame
from OpenGL.GL import *
from init_display import initialize_display, handle_events, update_display, basic_transformations
from shapes import BresenhamCircle

def main():
    """Main execution loop."""
    display = initialize_display()  # Set up the display

    circle = BresenhamCircle(0, 0, 100) 

    # Main loop
    while True:
        handle_events()             # Check for Pygame events
        circle.draw()                
        update_display()

main()
