import pygame
import math
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
from PIL import Image
import numpy


def read_texture(filename):
    """
    Reads an image file and converts to a OpenGL-readable textID format
    """
    #img = Image.open(filename)
    image=Image.open(filename).convert('RGBA')
    im_arr = numpy.fromstring(image.tobytes(), dtype=numpy.uint8)
    im_arr = im_arr.reshape((image.size[1], image.size[0], 4)) 
    
    img_data = im_arr
    textID = glGenTextures(1)
    glBindTexture(GL_TEXTURE_2D, textID)
    glPixelStorei(GL_UNPACK_ALIGNMENT, 1)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_CLAMP)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_CLAMP)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_REPEAT)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_REPEAT)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_NEAREST)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_NEAREST)
    glTexEnvf(GL_TEXTURE_ENV, GL_TEXTURE_ENV_MODE, GL_DECAL)
    glTexImage2D(GL_TEXTURE_2D, 0, GL_RGBA,
                 image.size[0], image.size[1], 0, GL_RGBA, GL_UNSIGNED_BYTE, img_data)
    return textID


def main():
    pygame.init()
    display = (1200, 800)
    pygame.display.set_mode(display, DOUBLEBUF | OPENGL)
    pygame.display.set_caption('PyOpenGLobe')
    pygame.key.set_repeat(1, 10)    # allows press and hold of buttons
    gluPerspective(40, (display[0]/display[1]), 0.1, 50.0)
    glTranslatef(0.0, 0.0, -5)    # sets initial zoom so we can see globe
    lastPosX = 0
    lastPosY = 0
    texture0 = read_texture('./2k_sun.jpg')
    texture1 = read_texture('world1.png')
    counter_light=0
    while True:
        for event in pygame.event.get():    # user avtivities are called events

            # Exit cleanly if user quits window
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            # Rotation with arrow keys
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    glRotatef(1, 0, 1, 0)
                if event.key == pygame.K_RIGHT:
                    glRotatef(1, 0, -1, 0)
                if event.key == pygame.K_UP:
                    glRotatef(1, -1, 0, 0)
                if event.key == pygame.K_DOWN:
                    glRotatef(1, 1, 0, 0)

            # Zoom in and out with mouse wheel
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 4:  # wheel rolled up
                    glScaled(1.05, 1.05, 1.05)
                if event.button == 5:  # wheel rolled down
                    glScaled(0.95, 0.95, 0.95)

            # Rotate with mouse click and drag
            if event.type == pygame.MOUSEMOTION:
                x, y = event.pos
                dx = x - lastPosX
                dy = y - lastPosY
                mouseState = pygame.mouse.get_pressed()
                if mouseState[0]:

                    modelView = (GLfloat * 16)()
                    mvm = glGetFloatv(GL_MODELVIEW_MATRIX, modelView)

                    # To combine x-axis and y-axis rotation
                    temp = (GLfloat * 3)()
                    temp[0] = modelView[0]*dy + modelView[1]*dx
                    temp[1] = modelView[4]*dy + modelView[5]*dx
                    temp[2] = modelView[8]*dy + modelView[9]*dx
                    norm_xy = math.sqrt(temp[0]*temp[0] + temp[1]
                                        * temp[1] + temp[2]*temp[2])
                    glRotatef(math.sqrt(dx*dx+dy*dy),
                              temp[0]/norm_xy, temp[1]/norm_xy, temp[2]/norm_xy)

                lastPosX = x
                lastPosY = y

        # Creates Sphere and wraps texture
        glEnable(GL_DEPTH_TEST)
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        glClearColor(1,1,1,1)
        
  
  

        glMaterialfv(GL_FRONT_AND_BACK, GL_SPECULAR, [1,1,1,1]);
        glMaterialfv(GL_FRONT_AND_BACK, GL_SHININESS,[50]);
  
        glEnable(GL_LIGHTING)
        glEnable(GL_LIGHT0)

        glPushMatrix()
        glTranslatef(0.0,0.0,0.0)
        theta=math.pi*counter_light/100
        glLight(GL_LIGHT0, GL_POSITION,  (1.6*math.sin(theta), 0, 1.6*math.cos(theta), 1))
        glLightfv(GL_LIGHT0, GL_AMBIENT,  (0, 1.5, 1, 0.9))
        glLightfv(GL_LIGHT0, GL_DIFFUSE,  (0, 1.5, 1, 0.5))
        glLightfv(GL_LIGHT0, GL_SPECULAR,  (0, 1.5, 1, 0.2))
        glPopMatrix()
        glEnable(GL_COLOR_MATERIAL)
        glColorMaterial(GL_FRONT_AND_BACK, GL_AMBIENT_AND_DIFFUSE)
        glEnable(GL_BLEND)
        #glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA);
        glBlendEquation(GL_FUNC_ADD) 
        glBlendFuncSeparate(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA, GL_ONE, GL_ZERO);
        qobj = gluNewQuadric()
        gluQuadricTexture(qobj, GL_TRUE)
        glEnable(GL_TEXTURE_2D)
        glBindTexture(GL_TEXTURE_2D, texture1)
        glPushMatrix()
        glTranslatef(0,0,0)
        glColor4f(0.2, 0.2, 0.5, 0.5)
        gluSphere(qobj, 0.5+0.1*math.cos(theta), 50, 50)
        glPopMatrix()
        glColor4f(0.5, 0.2, 0.2, 0.8)
        glBindTexture(GL_TEXTURE_2D, texture0)
        gluSphere(qobj, 1, 50, 50)
        
        gluDeleteQuadric(qobj)
        glDisable(GL_TEXTURE_2D)      

        # Displays pygame window
        pygame.display.flip()
        pygame.time.wait(10)
        counter_light+=1
        if(counter_light>200):
             counter_light=0

main()
