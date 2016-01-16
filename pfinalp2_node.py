#!/usr/bin/python
# -*- coding: latin-1 -*-

#################################### PRACTICA 7 ######################################
######################### Autores: Raquel Noblejas Sampedro  #########################
#########################          Daniel Revilla Twose      #########################
######################################################################################

# Importamos las bibliotecas que vamos a usar.
import sys
import os

# Comandos para la instalacion de NodeJS para los servidores, comandos sacados de la practica 4 de CDPS.
os.system("apt-get update")
os.system("apt-get install software-properties-common -y")
os.system("apt-get install git -y")
os.system("apt-get install make g++ -y")
os.system("apt-get install python-software-properties -y")
os.system("add-apt-repository ppa:chris-lea/node.js -y")
os.system("apt-get update")
os.system("apt-get install nodejs -y")