#!/bin/bash

#Comando que mostra a pasta/diretório onde você está:
echo 'Pasta/Diretório atual:'
pwd

#Comando que gera uma lista detalhada do conteúdo da pasta HOME e redireciona para o arquivo lista_HOME.txt
echo 'Gerando a lista detalhada do conteúdo da pasta HOME em lista_HOME.txt'
ls -lah ~ > lista_HOME.txt

#Comando que imprime a data atual na tela
echo 'Data e horário atual:'
date
