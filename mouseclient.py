import pygame
from pygame.locals import *

from OpenGL.GL import *
from OpenGL.GLU import *
import mouse
import socket
import os
import struct

verticies = (
    (1, -1, -1),
    (1, 1, -1),
    (-1, 1, -1),
    (-1, -1, -1),
    (1, -1, 1),
    (1, 1, 1),
    (-1, -1, 1),
    (-1, 1, 1)
    )

edges = (
    (0,1),
    (0,3),
    (0,4),
    (2,1),
    (2,3),
    (2,7),
    (6,3),
    (6,4),
    (6,7),
    (5,1),
    (5,4),
    (5,7)
    )


def Cube():
    glBegin(GL_LINES)
    for edge in edges:
        for vertex in edge:
            glVertex3fv(verticies[vertex])
    glEnd()


def main():
    # get the hostname
    os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (100,100)
    ipAddress = "192.168.2.1"

    host = ipAddress
    port = 5001  # initiate port no above 1024

    client_socket = socket.socket()  # get instance
    
    client_socket.connect((host, port))  


    My=0
    Mx=0
    mouseXpos=0
    mouseYpos=0
    pygame.init()
    display = (800,600)
    pygame.display.set_mode(display, DOUBLEBUF|OPENGL)

    gluPerspective(45, (display[0]/display[1]), 0.1, 50.0)

    glTranslatef(0.0,0.0, -5)
    k=0.01
    while True:
        data = client_socket.recv(1)
        print(data)
        if data:
            mybyte=int.from_bytes(data, 'big', signed=False) 
            mx=((mybyte&0xF0)>>4)-8
            my=(mybyte&0x0F)-8
            print(mybyte,mx,my)
            mouse.move(mx,my,absolute=False,duration=0.1)
            Mx=Mx+mx
            My=My+my
            mouseXpos=Mx
            mouseYpos=My
        glRotatef(k*(mouseXpos-400), 1, 0, 0)
        glRotatef(k*(mouseYpos-300), 0, 1, 0)
        glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
        Cube()
        pygame.display.flip()
        #pygame.time.wait(10)
        for event in pygame.event.get():
            if event.type == pygame.MOUSEMOTION:
               mouse_position = pygame.mouse.get_pos()
               #a_block.set_position(mouse_position[0],mouse_position[1])
               mouseXpos=mouse_position[0]
               mouseYpos=mouse_position[1]
#               data=(mouseXpos,mouseYpos)
#
#               client_socket.send(data.encode())
            if event.type == QUIT:
               pygame.quit()
               return
            elif event.type == MOUSEWHEEL:
               print(event)
               print(event.x, event.y)
               print(event.flipped)
               print(event.which)
               # can access properties with
               # proper notation(ex: event.y)
               # receive data stream. it won't accept data packet greater than 1024 bytes
 

main()
