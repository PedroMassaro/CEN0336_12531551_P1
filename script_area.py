#!/usr/bin/env python3

#Nesse bloco o script irá receber os valores fornecidos pelo usuário
import sys

num1 = sys.argv[1]
num2 = sys.argv[2]

#Verificação de entrada:

#1-Verificar se o número valores fornecidos está correto - Deve ser 2 inteiros
if len(sys.argv) != 3:
    print("Erro: Você deve fornecer exatamente dois números inteiros positivos.")
    sys.exit(1)

#2-Verificar se os valores recebidos são números inteiros positivos
if not (num1.isdigit() and num2.isdigit()):
    print("Erro: Ambos os valores fornecidos devem ser números inteiros positivos.")
    sys.exit(1)

#3-Converção dos objetos para inteiros
a = int(num1)
b = int(num2)

#4-Verificar se os valores são menores que 500
if a >= 500 or b >= 500:
    print("Erro: Ambos os números devem ser menores que 500.")
    sys.exit(1)

#Output

#Cálculo a área do triângulo retângulo
area = ((a*b)/2) 

#Output do resultado obtido
print(f"A área do triângulo retângulo com lados a={a} e b={b}, é {area}")
