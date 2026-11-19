from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

# Camera position
eyeX, eyeY, eyeZ = 0.0, 0.0, 5.0

# Look-at point
centerX, centerY, centerZ = 0.0, 0.0, 0.0

# Draw color cube
def draw_cube():
    glBegin(GL_QUADS)

    # Front (Red)
    glColor3f(1, 0, 0)
    glVertex3f(-1, -1, 1)
    glVertex3f(1, -1, 1)
    glVertex3f(1, 1, 1)
    glVertex3f(-1, 1, 1)

    # Back (Green)
    glColor3f(0, 1, 0)
    glVertex3f(-1, -1, -1)
    glVertex3f(-1, 1, -1)
    glVertex3f(1, 1, -1)
    glVertex3f(1, -1, -1)

    # Top (Blue)
    glColor3f(0, 0, 1)
    glVertex3f(-1, 1, -1)
    glVertex3f(-1, 1, 1)
    glVertex3f(1, 1, 1)
    glVertex3f(1, 1, -1)

    # Bottom (Yellow)
    glColor3f(1, 1, 0)
    glVertex3f(-1, -1, -1)
    glVertex3f(1, -1, -1)
    glVertex3f(1, -1, 1)
    glVertex3f(-1, -1, 1)

    # Right (Magenta)
    glColor3f(1, 0, 1)
    glVertex3f(1, -1, -1)
    glVertex3f(1, 1, -1)
    glVertex3f(1, 1, 1)
    glVertex3f(1, -1, 1)

    # Left (Cyan)
    glColor3f(0, 1, 1)
    glVertex3f(-1, -1, -1)
    glVertex3f(-1, -1, 1)
    glVertex3f(-1, 1, 1)
    glVertex3f(-1, 1, -1)

    glEnd()

# Display
def display():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()

    # Camera (Perspective viewing)
    gluLookAt(eyeX, eyeY, eyeZ, centerX, centerY, centerZ, 0, 1, 0)

    draw_cube()
    glutSwapBuffers()

# Keyboard controls
def keyboard(key, x, y):
    global eyeX, eyeY, eyeZ

    key = key.decode("utf-8")

    if key == 'w':   # Move forward
        eyeZ -= 0.2
    elif key == 's': # Move backward
        eyeZ += 0.2
    elif key == 'a': # Move left
        eyeX -= 0.2
    elif key == 'd': # Move right
        eyeX += 0.2
    elif key == 'q': # Move up
        eyeY += 0.2
    elif key == 'e': # Move down
        eyeY -= 0.2

    glutPostRedisplay()

# Init
def init():
    glClearColor(0, 0, 0, 1)
    glEnable(GL_DEPTH_TEST)

# Reshape
def reshape(w, h):
    glViewport(0, 0, w, h)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(60, w/h, 1, 20)
    glMatrixMode(GL_MODELVIEW)

# Main
def main():
    glutInit()
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH)
    glutInitWindowSize(700, 700)
    glutCreateWindow(b"3D Color Cube - Camera Control")

    init()
    glutDisplayFunc(display)
    glutReshapeFunc(reshape)
    glutKeyboardFunc(keyboard)

    glutMainLoop()

if __name__ == "__main__":
    main()
