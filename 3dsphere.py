import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
import math

pygame.init()
display = (400, 300)
screen = pygame.display.set_mode(display, DOUBLEBUF | OPENGL)
glEnable(GL_DEPTH_TEST)
sphere = gluNewQuadric() #Create new sphere
glMatrixMode(GL_PROJECTION)
gluPerspective(45, (display[0]/display[1]), 0.1, 50.0)
glMatrixMode(GL_MODELVIEW)
gluLookAt(0, -8, 0, 0, 0, 0, 0, 0, 1)
viewMatrix = glGetFloatv(GL_MODELVIEW_MATRIX)
glLoadIdentity()

#position the light
glLightfv(GL_LIGHT0, GL_POSITION,  (0, 1.0, 0, 1.0));

run = True
counter_light=0
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE or event.key == pygame.K_RETURN:
                run = False
    keypress = pygame.key.get_pressed()
    # init model view matrix
    glLoadIdentity()
    # init the view matrix
    glPushMatrix()
    glLoadIdentity()
    # apply the movment
    if keypress[pygame.K_w]:
        glTranslatef(0,0,0.1)
    if keypress[pygame.K_s]:
        glTranslatef(0,0,-0.1)
    if keypress[pygame.K_d]:
        glTranslatef(-0.1,0,0)
    if keypress[pygame.K_a]:
        glTranslatef(0.1,0,0)
    # multiply the current matrix by the get the new view matrix and store the final vie matrix
    glMultMatrixf(viewMatrix)
    viewMatrix = glGetFloatv(GL_MODELVIEW_MATRIX)
    # apply view matrix
    glPopMatrix()
    glMultMatrixf(viewMatrix)
    
    
    #glClearColor(0.0f, 0.0f, 0.0f, 0.0f); // Clear The Background Color To Blue
    glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT) #Clear the screen
    glClearDepth(1.0);                    #// Enables Clearing Of The Depth Buffer
    glDepthFunc(GL_LESS);                 #// The Type Of Depth Test To Do
    glEnable(GL_DEPTH_TEST);            #// Enables Depth Testing
    glShadeModel(GL_SMOOTH);   
    
    glEnable(GL_LIGHTING)
    glEnable(GL_LIGHT0)

    glPushMatrix()
    glTranslatef(0.0,0.0, 5)
    theta=math.pi*counter_light/100
    glLight(GL_LIGHT0, GL_POSITION,  (math.sin(theta), 1, math.cos(theta), 1))
    glLightfv(GL_LIGHT0, GL_AMBIENT,  (0, 1.5, 1, 0))
    glLightfv(GL_LIGHT0, GL_DIFFUSE,  (0, 1.5, 1, 0))
    glPopMatrix()
    
    glPushMatrix()
    glTranslatef(-1.5, 0, 0) #Move to the place
    glColor4f(0.5, 0.2, 0.2, 0.1) #Put color
    glEnable(GL_COLOR_MATERIAL)
    glColorMaterial(GL_FRONT_AND_BACK, GL_AMBIENT_AND_DIFFUSE )
    sphere = gluNewQuadric();             #//Instatiate our sphere
    gluQuadricDrawStyle(sphere, GLU_FILL);#//Following three method calls instantiate the texturing style
    gluQuadricTexture(sphere, GL_TRUE);
    gluQuadricNormals(sphere, GLU_SMOOTH);
    gluSphere(sphere, 1.0, 32, 16) #Draw sphere
    glPopMatrix()
   
    glPushMatrix()
    glTranslatef(-1.5, 0, 0) #Move to the place
    glColor4f(0.2, 0.5, 0.2, 0.8) #Put color
    gluSphere(sphere, 0.9, 32, 16) #Draw sphere
    glPopMatrix()
    
    glDisable(GL_LIGHT0)
    glDisable(GL_LIGHTING)
    
    pygame.display.flip() #Update the screen
    counter_light+=1
    if(counter_light>200):
        counter_light=0
    pygame.time.wait(10)

pygame.quit()
