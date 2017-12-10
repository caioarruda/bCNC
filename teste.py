import pygame
import sys
import time
from pygame.locals import *
pygame.joystick.init()
pygame.display.set_mode((1,1))
_joystick = pygame.joystick.Joystick(0)
_joystick.init()

i = 0

axis = [0] * _joystick.get_numaxes()
botoes = [0] * _joystick.get_numbuttons()

while 1:
   for event in pygame.event.get():
      if event.type == 10: 
	 print 'btn: ' + str(event.button) + ' foi pressionado'
      if event.type == 7 and event.axis == 1:
         print 'axis: ' + str(event.axis) + ' foi pressionado'
	 _joystick.get_axis(event.axis)
