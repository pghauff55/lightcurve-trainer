
import pygame
from math import *
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
from PIL import Image
import numpy as np
# Last time when sphere was re-displayed
last_time = 0
import random
import noise
import os



def read_texture(filename):
    """
    Reads an image file and converts to a OpenGL-readable textID format
    """
    #img = Image.open(filename)
    image=Image.open(filename)
    im_arr = np.fromstring(image.tobytes(), dtype=np.uint8)
    im_arr = im_arr.reshape((image.size[1], image.size[0], 3)) 
    
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
    glTexImage2D(GL_TEXTURE_2D, 0, GL_RGB,
                 image.size[0], image.size[1], 0, GL_RGB, GL_UNSIGNED_BYTE, img_data)
    return textID
    
    
def read_3dtexture():
    
    
    image=Image.open("layer0.png")
    im_arr = np.frombuffer(image.tobytes(), dtype=np.uint8)
    im_arr = im_arr.reshape((image.size[1], image.size[0], 4)) 
    image=Image.open("layer1.png")
    im_arr0=np.frombuffer(image.tobytes(), dtype=np.uint8)
    im_arr0 = im_arr0.reshape((image.size[1], image.size[0], 4)) 
    im_arr = np.concatenate((im_arr,im_arr0),axis=0)
    image=Image.open("layer2.png")
    im_arr1=np.frombuffer(image.tobytes(), dtype=np.uint8)
    im_arr1 = im_arr1.reshape((image.size[1], image.size[0], 4)) 
    im_arr = np.concatenate((im_arr,im_arr1),axis=0)
    
    
    
    
    textID = glGenTextures(1)
    glBindTexture(GL_TEXTURE_3D, textID)
    glTexParameteri(GL_TEXTURE_3D, GL_TEXTURE_MIN_FILTER, GL_LINEAR)
    glTexParameteri(GL_TEXTURE_3D, GL_TEXTURE_MAG_FILTER, GL_LINEAR)
    glTexParameteri(GL_TEXTURE_3D, GL_TEXTURE_WRAP_S, GL_REPEAT)
    glTexParameteri(GL_TEXTURE_3D, GL_TEXTURE_WRAP_T, GL_REPEAT)
    glTexParameteri(GL_TEXTURE_3D, GL_TEXTURE_WRAP_R, GL_REPEAT)
    glTexImage3D(GL_TEXTURE_3D, 0, GL_RGBA,512, 512, 3, 0, GL_RGBA, 
             GL_UNSIGNED_BYTE, im_arr);
    return   textID    



SCALE=10             
def update_point(coords, seed,MAP_SIZE):
    return noise.pnoise2(coords[0]/SCALE,
                          coords[1]/SCALE,
                          octaves=66,
                          persistence=0.9,
                          lacunarity=2,
                          repeatx=MAP_SIZE[0],
                          repeaty=MAP_SIZE[1],
                          base=seed
                         )
                         
def generate_heightmap(map_size):
    seed = int(random.random()*1000)
    minimum = 99999999
    maximum = 0
    heightmap = np.zeros(map_size)

    for x in range(map_size[0]):
        for y in range(map_size[1]):
            new_value = update_point((x, y), seed,map_size)
            if(new_value>maximum):
                 maximum=new_value
            if(new_value<minimum):
                 minimum=new_value
            heightmap[x][y] = new_value
    return 0.1*(heightmap-minimum)/(maximum-minimum)+0.9
    
                                          
# The sphere class
class Sphere:

    # Constructor for the sphere class
    def __init__(self, radius):

        # Radius of sphere
        self.radius = radius

        # Number of latitudes in sphere
        self.lats = 200

        # Number of longitudes in sphere
        self.longs = 200

        self.user_theta = 0
        self.user_height = 0

        # Direction of light
        self.direction = [2.0, 0.0, -5.0, 1.0]

        # Intensity of light
        self.intensity = [0.95, 0.95, 0.95, 1.0]

        # Intensity of ambient light
        self.ambient_intensity = [0.8, 0.8, 0.8, 1.0]

        # The surface type(Flat or Smooth)
        self.surface = GL_FLAT

    # Initialize
    def calc_display_list(self):
       
        
        
        
        
        
        print("Generate random maps.")
        random_maps=[]
        counter_maps=0
        while counter_maps<2:
            R=np.zeros((self.lats+1,self.longs+1))
            for i in range(0, self.lats + 1):
                for j in range(0, self.longs + 1):
                    R[i,j]=random.randint(0,20)*0.005+0.9
            random_maps.append(R)
            counter_maps+=1

        counter_maps=0
        while counter_maps<self.N/2:
            R=np.zeros((self.lats+1,self.longs+1))
            for i in range(0, self.lats + 1):
                for j in range(0, self.longs + 1):
                    R[i,j]=random_maps[0][i,j]+2*counter_maps*(random_maps[1][i,j]-random_maps[0][i,j])/self.N
            counter_maps+=1
            self.list_random_maps.append(R)
            self.list_vertex.append([])
            self.list_normals.append([])
        counter_maps=0
        while counter_maps<self.N/2:
            R=np.zeros((self.lats+1,self.longs+1))
            for i in range(0, self.lats + 1):
                for j in range(0, self.longs + 1):
                    R[i,j]=random_maps[1][i,j]+2*counter_maps*(random_maps[0][i,j]-random_maps[1][i,j])/self.N
            counter_maps+=1
            self.list_random_maps.append(R)
            self.list_vertex.append([])
            self.list_normals.append([])
  
        print("Calc vertexes.")
        
        counter_maps=0
        while counter_maps<self.N:
            self.calc_vertex()
            counter_maps+=1 
            
            
        print("Calc normals.")
        for k in range(self.N):
            self.list_vertex[k]=np.array(self.list_vertex[k]).reshape((self.lats+1,self.longs,3))
            self.list_normals[k]=np.array(self.list_normals[k]).reshape((self.lats+1,self.longs,3))
            print(".")
            for i in range(0, self.lats +1):
                for j in range(0, self.longs ):
                   v1=self.list_vertex[k][i-1,j-1]
                   v2=self.list_vertex[k][i-1,j]
                   v3=self.list_vertex[k][i,j-1]
                   vf1=v2-v1
                   vf2=v3-v1
  #                 vn1=np.cross(vf1,vf2)
  #                 v1=self.list_vertex[k][i-1,j-1]
  #                 v2=self.list_vertex[k][i-1,j-2]
  #                 v3=self.list_vertex[k][i,j-1]
  ##                 vf1=v2-v1
   #                vf2=v3-v1
   #                vn2=np.cross(vf1,vf2)
   #                v1=self.list_vertex[k][i-1,j-1]
   #                v2=self.list_vertex[k][i-1,j]
   #                v3=self.list_vertex[k][i-2,j-1]
   #                vf1=v2-v1
   #                vf2=v3-v1
   #                vn3=np.cross(vf1,vf2)
   #                v1=self.list_vertex[k][i-1,j-1]
   #                v2=self.list_vertex[k][i-1,j-2]
   #                v3=self.list_vertex[k][i-2,j-1]
   #                vf1=v2-v1
   #                vf2=v3-v1
                   vn4=np.cross(vf1,vf2)
                   vn_avg=np.linalg.norm(vn4)
                   self.list_normals[k][i,j]=np.linalg.norm(vn_avg)
 
                   
        return

    def init(self):
        print("initialise...")
        # Set background color to black
        glClearColor(0.0, 0.0, 0.0, 0.0)

        self.compute_location()
        glShadeModel(GL_FLAT)
        # Set OpenGL parameters
        glEnable(GL_DEPTH_TEST)

        # Enable lighting
        glEnable(GL_LIGHTING)

        # Set light model
        glLightModelfv(GL_LIGHT_MODEL_AMBIENT, self.ambient_intensity)

        # Enable light number 0
        glEnable(GL_LIGHT0)

        # Set position and intensity of light
        light_ambient = [0.2, 0.2, 0.2, 1.0]
        light_diffuse = [1.0, 1.0, 1.0, 1.0]
        light_specular = [1.0, 1.0, 1.0, 1.0]
        light_position = [-1.0, 1.0, -1.0, 0.0]
        glLightfv(GL_LIGHT0, GL_AMBIENT, light_ambient);
        glLightfv(GL_LIGHT0, GL_DIFFUSE, light_diffuse);
        glLightfv(GL_LIGHT0, GL_SPECULAR, light_specular);
        glLightfv(GL_LIGHT0, GL_POSITION, light_position); 

        glEnable(GL_LIGHT1)

        # Set position and intensity of light
        light_ambient = [0.2, 0.2, 0.2, 1.0]
        light_diffuse = [1.0, 1.0, 1.0, 1.0]
        light_specular = [1.0, 1.0, 1.0, 1.0]
        light_position = [1.0, -1.0, -1.0, 0.0]
        glLightfv(GL_LIGHT1, GL_AMBIENT, light_ambient);
        glLightfv(GL_LIGHT1, GL_DIFFUSE, light_diffuse);
        glLightfv(GL_LIGHT1, GL_SPECULAR, light_specular);
        glLightfv(GL_LIGHT1, GL_POSITION, light_position); 
        
        #GLfloat al[] = {0.2, 0.2, 0.2, 1.0};
        #glLightModelfv(GL_LIGHT_MODEL_AMBIENT, al); 
        glLightModeli(GL_LIGHT_MODEL_LOCAL_VIEWER,GL_TRUE); 
        # Setup the material
        
        glEnable(GL_COLOR_MATERIAL)
        glColorMaterial(GL_FRONT, GL_AMBIENT_AND_DIFFUSE)

        self.N=30
        self.list_vertex=[]
        self.list_normals=[]
        self.list_random_maps=[]
        self.counter_random=0
        basename=os.path.basename("./data_vertex_normals.npy")
        print(basename)
        
        if(True):
            print("Data file saving.")
            self.calc_display_list()
            np.save("data_vertex_normals.npy",[self.list_vertex,self.list_normals])
        else:
            print("Data file found.")
            data_vertex_normals=np.load("./data_vertex_normals.npy")
            self.list_vertex=data_vertex_normals[0]
            self.list_normals=data_vertex_normals[1]


        
        print("Display Lists.")
        glEnable(GL_NORMALIZE)
    
        
        mat_a = [0.1, 0.5, 0.8, 1.0]
        mat_d = [0.1, 0.5, 0.8, 1.0]
        mat_s = [1.0, 1.0, 1.0, 1.0]
        low_sh = [5.0]
        glMaterialfv(GL_FRONT, GL_AMBIENT, mat_a);
        glMaterialfv(GL_FRONT, GL_DIFFUSE, mat_d);
        glMaterialfv(GL_FRONT, GL_SPECULAR, mat_s);
        glMaterialfv(GL_FRONT, GL_SHININESS, low_sh); 
  
        self.index = glGenLists(self.N)            
        for k in range(self.N):
            glNewList(self.index+k,GL_COMPILE)
            for i in range(0, self.lats):
                glBegin(GL_QUAD_STRIP)
                for j in range(0, self.longs ):
                   glTexCoord3f((i+1)/self.lats,(j+1)/self.longs,np.linalg.norm(self.list_normals[k][i,j]))
                   glNormal3f(self.list_normals[k][i,j][0],self.list_normals[k][i,j][1],self.list_normals[k][i,j][2])
                   glVertex3f(self.list_vertex[k][i,j][0],self.list_vertex[k][i,j][1],self.list_vertex[k][i,j][2])
                   
                   glTexCoord3f((i)/self.lats,(j+1)/self.longs,20*np.linalg.norm(self.list_normals[k][i-1,j]))
                   glNormal3f(self.list_normals[k][i-1,j][0],self.list_normals[k][i-1,j][1],self.list_normals[k][i-1,j][2])
                   glVertex3f(self.list_vertex[k][i-1,j][0],self.list_vertex[k][i-1,j][1],self.list_vertex[k][i-1,j][2])
                glEnd()
            glBegin(GL_QUAD_STRIP)
            i=self.lats
            for j in range(0, self.longs ):
               glTexCoord3f((i+1)/self.lats,(j+1)/self.longs,np.linalg.norm(self.list_normals[k][i,j]))
               glNormal3f(self.list_normals[k][i,j][0],self.list_normals[k][i,j][1],self.list_normals[k][i,j][2])
               glVertex3f(self.list_vertex[k][i,j][0],self.list_vertex[k][i,j][1],self.list_vertex[k][i,j][2])
                   
               glTexCoord3f(0,(j+1)/self.longs,20*np.linalg.norm(self.list_normals[k][0,j]))
               glNormal3f(self.list_normals[k][0,j][0],self.list_normals[k][0,j][1],self.list_normals[k][0,j][2])
               glVertex3f(self.list_vertex[k][0,j][0],self.list_vertex[k][0,j][1],self.list_vertex[k][0,j][2])
            glEnd()
            glEndList()
        print("finished...")
    #######################################################################################################
    def compute_location(self):
        x = 2 * cos(self.user_theta)
        y = 2 * sin(self.user_theta)
        z = self.user_height
        d = sqrt(x * x + y * y + z * z)

        # Set matrix mode
        glMatrixMode(GL_PROJECTION)

        # Reset matrix
        glLoadIdentity()
        glFrustum(-d * 0.5, d * 0.5, -d * 0.5, d * 0.5, d - 1.1, d + 1.1)

        # Set camera
        gluLookAt(x, y, z, 0, 0, 0, 0, 0, 1)

    # Display the sphere
    def display(self):
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

        # Set color to white
        glColor3f(1.0, 1.0, 1.0)

        # Set shade model
        

        
        #glListBase(self.index)
        glCallList(self.index+self.counter_random)
        
        self.counter_random+=1
        if(self.counter_random>=self.N):
             self.counter_random=0
        #glutSwapBuffers()

  ####################################################################################################
    def calc_vertex(self):
        
        R=self.list_random_maps[self.counter_random]
        #R=generate_heightmap([self.lats,self.longs])
        
        self.counter_random+=1
        if(self.counter_random>=self.N):
              self.counter_random=0
        for i in range(0, self.lats +1 ):
            lat0 = pi * (-0.5 + float(float(i - 1) / float(self.lats)))
            z0 = sin(lat0)
            zr0 = cos(lat0)

            
            # Use Quad strips to draw the sphere
            #glBegin(GL_QUAD_STRIP)
            
            
            
            for j in range(0, self.longs ):
                lng = 2 * pi * float(float(j - 1) / float(self.longs))
                x = cos(lng)
                y = sin(lng)
                if(j==self.longs):
                    R0=R[i-1][0]
                else:
                    R0=R[i-1][j]
                #glNormal3f(x * zr0, y * zr0, z0)
                #glTexCoord3f(i/self.lats,j/self.longs,10*R0)
                #glVertex3f(R0*x * zr0,R0* y * zr0,R0* z0)

                #glNormal3f(x * zr1, y * zr1, z1)
                #glTexCoord3f((i+1)/self.lats,(j+1)/self.longs,10*R1)
                #glVertex3f(R1*x * zr1,R1* y * zr1,R1* z1)
                self.list_vertex[self.counter_random].append(np.array([R0*x * zr0,R0* y * zr0,R0* z0]))
                self.list_normals[self.counter_random].append(np.array([0,0,0]))
            #glEnd()

    # Keyboard controller for sphere
    def special(self, key, x, y):

        # Scale the sphere up or down
        if key == GLUT_KEY_UP:
            self.user_height += 0.1
        if key == GLUT_KEY_DOWN:
            self.user_height -= 0.1

        # Rotate the cube
        if key == GLUT_KEY_LEFT:
            self.user_theta += 0.1
        if key == GLUT_KEY_RIGHT:
            self.user_theta -= 0.1

        # Toggle the surface
        if key == GLUT_KEY_F1:
            if self.surface == GL_FLAT:
                self.surface = GL_SMOOTH
            else:
                self.surface = GL_FLAT

        self.compute_location()
        glutPostRedisplay()

    # The idle callback
    def idle(self):
        global last_time
        time = glutGet(GLUT_ELAPSED_TIME)

        if last_time == 0 or time >= last_time + 40:
            last_time = time
            glutPostRedisplay()

    # The visibility callback
    def visible(self, vis):
        if vis == GLUT_VISIBLE:
            glutIdleFunc(self.idle)
        else:
            glutIdleFunc(None)


# The main function
def main():

    # Initialize the OpenGL pipeline
    #glutInit(sys.argv)
    pygame.init()
    display = (1200, 800)
    pygame.display.set_mode(display, DOUBLEBUF | OPENGL)
    pygame.display.set_caption('PyOpenGLobe')
    texture=read_3dtexture()
    #texture1 = read_texture('./2k_sun.jpg')
    # Instantiate the sphere object
    s = Sphere(1.0)

    s.init()
    lastPosX = 0
    lastPosY = 0
    while True:
        for event in pygame.event.get():    # user avtivities are called events

            # Exit cleanly if user quits window
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
                    # Rotate with mouse click and drag
            # Zoom in and out with mouse wheel
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 4:  # wheel rolled up
                    glScaled(1.05, 1.05, 1.05)
                if event.button == 5:  # wheel rolled down
                    glScaled(0.95, 0.95, 0.95)
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
                    norm_xy = sqrt(temp[0]*temp[0] + temp[1]
                                        * temp[1] + temp[2]*temp[2])
                    glRotatef(sqrt(dx*dx+dy*dy),
                              temp[0]/norm_xy, temp[1]/norm_xy, temp[2]/norm_xy)

                lastPosX = x
                lastPosY = y
        
        
       
       
       
        glEnable(GL_COLOR_MATERIAL)
        glColor4f(1.0, 1.0, 1.0, 1.0)
        glColorMaterial(GL_FRONT_AND_BACK, GL_DIFFUSE)
        
        glEnable(GL_TEXTURE_3D)        
        glBindTexture(GL_TEXTURE_3D, texture)
        #glEnable(GL_TEXTURE_2D)
        #glBindTexture(GL_TEXTURE_2D, texture1)
        s.display()
        glDisable(GL_TEXTURE_3D) 
        
        glDisable(GL_COLOR_MATERIAL)
        
        pygame.display.flip()
        pygame.time.wait(30)

# Call the main function
if __name__ == '__main__':
    main()
