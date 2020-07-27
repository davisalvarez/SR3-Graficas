"""
UVG
GRAFICAS POR COMPUTADORA - seccion 20

Davis Alvarez - 15842

SR1: Points
"""
from render import *

img = render()

img.glInit() #5
img.glCreateWindow(1000,1000) #5
img.glClearColor(0.5,1,0.36) #10
img.glClear() #20
img.glViewPort(1,1,398,398) #10
img.glColor(0,0,0)#15
#img.glVertex(0.75,0.12)#30


img.paintModelOBJ("face.obj", (200,200), (10,10))

img.glFinish() #5







