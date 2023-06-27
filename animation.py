import os, sys, math, pygame, pygame.mixer
from pygame.locals import *

black = (0,0,0)
red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)
white = (255,255,255)
run_me = True

screen_size = screen_width, screen_height = 1080, 720
screen = pygame.display.set_mode(screen_size)
pygame.display.set_caption('Animation')

clock = pygame.time.Clock()
fps_limit = 60

#circle 
colorcircle = (red)
colorcircle2=(blue)
posx = 1080/2
posy = 720/2
circle = pygame.draw.circle(screen, colorcircle, (posx, posy), 50)
r=posx*0.5
theta=40/180*math.pi
time1=0
time2=0
angular_vel1=30/180*math.pi
angular_vel2=43/180*math.pi
angle2=40/180*math.pi
phi=30.2/180*math.pi
delta_t=0.9
delta_t1=delta_t
delta_t2=delta_t
counter=0
dcounter=1
while run_me:
	clock.tick(fps_limit)
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			run_me = False
	screen.fill(white)
	x1=-r*math.sin(angle2)*math.cos(angular_vel1*time1)
	y1=r*math.sin(angle2)*math.sin(angular_vel1*time1)
	x2=r*math.sin(angle2)*math.cos(angular_vel2*time2+phi)
	y2=r*math.sin(angle2)*math.sin(angular_vel2*time2+phi)
	pygame.draw.circle(screen, colorcircle2,( posx, posy), r,width=1)
	pygame.draw.circle(screen, colorcircle,( posx+x1, posy+y1), posx*0.1)
	pygame.draw.circle(screen, colorcircle,( posx+x2, posy+y2), posx*0.1)
	pygame.draw.circle(screen, blue,( posx-(x2+x1)/2, posy-(y1+y2)/2), posx*0.07)
	pygame.draw.line(screen, black,(posx,posy),( posx-(x2+x1)/2, posy-(y1+y2)/2), width=2)
	pygame.draw.line(screen, black,(posx,posy),( posx+x1, posy+y1),width=2)
	pygame.draw.line(screen, black,(posx,posy),( posx+x2, posy+y2),width=2)
	distsquared=(x2-x1)*(x2-x1)
	dist=math.sqrt(distsquared)

	
	if (distsquared//40000<1):
		delta_t=delta_t*-1.0
		delta_t1=10.0*delta_t*(dist/posx*0.28)*(dist/posx*0.28)
		delta_t2=10.0*math.pow(1.07,counter)*delta_t*(dist/posx*0.28)*(dist/posx*0.28)
		time1=time1+delta_t1
		time2=time2+delta_t2
		counter=counter+dcounter
	delta_t1=delta_t*(dist/posx*0.28)*(dist/posx*0.28)
	delta_t2=math.pow(1.07,counter)*delta_t*(dist/posx*0.28)*(dist/posx*0.28)
	pygame.display.flip()
	time1=time1+delta_t1
	time2=time2+delta_t2

	if(counter>=50 or counter<=0):
		dcounter=dcounter*-1
		counter=counter+2*dcounter


pygame.quit()
