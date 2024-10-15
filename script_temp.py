#!/usr/bin/env python3

import sys

#Entrada das temperaturas em celsius pelo usuário
temp_input = input("Digite as temperaturas em graus Celsius (separadas por espaço): ")

#Agrupa a entrada em uma lista de strings
temp_celsius = temp_input.split()

#Verifica se há apenas númerios como entrada
for temp1 in temp_celsius:
  if not (temp1.lstrip('-').isdigit()):
   print('Erro: Você deve incluir apenas números, separados por espaço, em seu input.')
   sys.exit(1)

#Lista para armazenar as temperaturas em Fahrenheit
temp_fahrenheit = []

#Loop para converter e armazena cada valor da lista para Fahranheit
for temp2 in temp_celsius:
  cel = float(temp2)
  fah = ((9/5)*cel)+32
  temp_fahrenheit.append((cel, fah))

# Exibe as temperaturas convertidas em formato de tabela
print("Celsius   Fahrenheit")
for cel, fah in temp_fahrenheit:
  print(f"{cel:<9} {fah:<9.1f}")
