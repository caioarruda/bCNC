import pygame
import sys
import time
from pygame.locals import *
from subprocess import Popen
proc = Popen(["xboxdrv --detach-kernel-driver --silent"], shell=True,
stdin=None, stdout=None, stderr=None, close_fds=True)
pygame.joystick.init()
pygame.display.set_mode((1,1))
_joystick = pygame.joystick.Joystick(0)
_joystick.init()
btnFuncoes = ["incstep","decstep","x0","y0","z0","setfeed","hold","resume","stop","unlock"]
nomesBtnFuncoes = ["Aumentar Steps", "Diminuir Steps", "Zerar o X", "zerar o Y", "zerar o Z", "Setar Feed 100 passos","Pause", "Start", "Stop", "Unlock"]
eixosFuncoes = ["jogx", "jogy","jogz"]
nomesEixosFuncoes = ["Movimentar X", "Movimentar Y","Movimentar Z"]
botoes = [-1]*10
eixos = [-1]*3
direcs = [-1]*3
arquivo = ""

def definirBotao(funcao, index):
	global botoes
	flag = 1
	while flag:
		for event in pygame.event.get():
			if event.type == 10:
				print event.button
				flag = 0
				botoes[index] = event.button
				pygame.event.clear()
				break

def definirEixo(funcao, index):
	global eixos
	global direcs
	flag = 1
	while flag:
		for event in pygame.event.get():
			if event.type == 7 and abs(event.value) >= 1:
				print event.axis
				flag = 0
				eixos[index] = event.axis
				pygame.event.clear()
				time.sleep(1)
				break
			if event.type == 9:
				print event.hat
				flag = 0
				direcs[index] = event.hat
				pygame.event.clear()
				time.sleep(1)
				pygame.event.clear()
				break

def lerControle():
	print "Presione no controle e veja na tela:"
	print "Presione qualquer tecla no teclado pra sair"
	flag = 1
	while flag:
		for event in pygame.event.get():
			if event.type == 10: 
				print "botao: " + str(event.button) + " foi pressionado"
			if event.type == 7:
				if abs(event.value) >= 1:
					print "eixo: " + str(event.axis) + " foi pressionado"
			if event.type == 9:
				print "direcional: " + str(event.hat) + " foi pressionado"
			if event.type == 2:
					flag = 0;
	menu()

def configurarControle():
	global arquivo
	i = 0
	for funcao in btnFuncoes:
		print "Pressione o botao para funcao ["+nomesBtnFuncoes[i]+"] :"
		definirBotao(funcao, i)
		i = i + 1
	i = 0 
	for funcao in eixosFuncoes:
		print "Pressione o eixo para funcao ["+nomesEixosFuncoes[i]+"] :"
		definirEixo(funcao, i)
		i = i + 1
	i = 0
	for b in botoes:
		arquivo = arquivo + btnFuncoes[i]+"="+str(b)+"\r\n"
		i = i + 1
	i = 0
	for e in eixos:
		if eixos == -1:
			arquivo = arquivo + eixosFuncoes[i]+"="+str(direcs[i])+"\r\n"
		else:
			arquivo = arquivo + eixosFuncoes[i]+"="+str(e)+"\r\n"
		i = i + 1
	f = open("configJoy.ini","w")
	f.write(arquivo)
	f.close()
	menu()

def menu():
	print "COnfigurador de controles:"
	print "=========================="
	print "Selecione a opcao:"
	print "[C] Configurar Controle"
	print "[V] Visualizar Indices dos botoes"
	print "[Q] Sair"
	print "Selecione [C/V/Q]:"
	flag = 1
	while flag:
		for event in pygame.event.get():
			if event.type == 2:
				if event.key == 99:
					configurarControle()
					flag = 0
				if event.key == 118:
					lerControle()
					flag = 0
				if event.key == 113:
					print "Saindo...."
					flag = 0	
					sys.exit	 
menu()
