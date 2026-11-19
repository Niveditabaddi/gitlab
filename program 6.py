from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

# Transformation variables
angle = 0
tx, ty = 0, 0
scale = 1

# Current transformation mode
mode = 0   # 1-Rotate, 2-Translate, 3-Scale

# Draw a 3D polygon (cube for better visualization)
def draw_polygon():
    glBegin(GL_QUADS)

    # Front face
    glColor3f(1, 0, 0)
    glVertex3f(-1, -1, 1)
    glVertex3f(1, -1, 1)
    glVertex3f(1, 1, 1)
    glVertex3f(-1, 1, 1)

    # Back face
    glColor3f(0, 1, 0)
    glVertex3f(-1, -1, -1)
    glVertex3f(-1, 1, -1)
    glVertex3f(1, 1, -1)
    glVertex3f(1, -1, -1)

    # Top face
    glColor3f(0, 0, 1)
    glVertex3f(-1, 1, -1)
    glVertex3f(-1, 1, 1)
    glVertex3f(1, 1, 1)
    glVertex3f(1, 1, -1)

    # Bottom face
    glColor3f(1, 1, 0)
    glVertex3f(-1, -1, -1)
    glVertex3f(1, -1, -1)
    glVertex3f(1, -1, 1)
    glVertex3f(-1, -1, 1)

    # Right face
    glColor3f(1, 0, 1)
    glVertex3f(1, -1, -1)
    glVertex3f(1, 1, -1)
    glVertex3f(1, 1, 1)
    glVertex3f(1, -1, 1)

    # Left face
    glColor3f(0, 1, 1)
    glVertex3f(-1, -1, -1)
    glVertex3f(-1, -1, 1)
    glVertex3f(-1, 1, 1)
    glVertex3f(-1, 1, -1)

    glEnd()

# Display function
def display():
    global angle, tx, ty, scale

    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()

    gluLookAt(0, 0, 6, 0, 0, 0, 0, 1, 0)

    # Apply transformations
    glTranslatef(tx, ty, 0)
    glScalef(scale, scale, scale)
    glRotatef(angle, 1, 1, 1)

    draw_polygon()

    glutSwapBuffers()

# Animation
def idle():
    global angle, tx, ty, scale, mode

    if mode == 1:   # Rotation
        angle += 0.5

    elif mode == 2:  # Translation
        tx += 0.005
        if tx > 2:
            tx = -2

    elif mode == 3:  # Scaling
        scale += 0.005
        if scale > 2:
            scale = 0.5

    glutPostRedisplay()

# Menu function
def menu(option):
    global mode

    if option == 1:
        mode = 1
    elif option == 2:
        mode = 2

    elif option == 3:
        mode = 3
    elif option == 4:
        exit(0)

# Initialize
def init():
    glClearColor(0, 0, 0, 1)
    glEnable(GL_DEPTH_TEST)

# Reshape
def reshape(w, h):
    glViewport(0, 0, w, h)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(60, w / h, 1, 20)
    glMatrixMode(GL_MODELVIEW)

# Main
def main():
    glutInit()
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH)
    glutInitWindowSize(700, 700)
    glutCreateWindow(b"3D Polygon Animation using Transformations")

    init()
    glutDisplayFunc(display)
    glutReshapeFunc(reshape)
    glutIdleFunc(idle)

    # Create menu
    glutCreateMenu(menu)
    glutAddMenuEntry("Rotate", 1)
    glutAddMenuEntry("Translate", 2)
    glutAddMenuEntry("Scale", 3)
    glutAddMenuEntry("Exit", 4)

    glutAttachMenu(GLUT_RIGHT_BUTTON)

    glutMainLoop()

if __name__ == "__main__":
    main ()
