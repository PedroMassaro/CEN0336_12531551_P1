#!/usr/bin/env python3

import sys

#01-Verifica se o número de argumentos adicionado está correto
if len(sys.argv) != 8:
  print("Erro: O número argumentos adicionado não está.")
  print("Uso: python script_CDS.py <sequência_DNA> <n1> <n2> <n3> <n4> <n5> <n6>")
  sys.exit(1)

#Input - Sequência de DNA
dna_sequence = sys.argv[1]

#02-Verificando se dna_sequence é  string
if not isinstance(dna_sequence, str):
  print("Erro: O argumento 1 (Sequência de DNA) deve ser uma string")

#03-Input das posiçôes e verificando se são números inteiros
try:
  n1 = int(sys.argv[2])
  n2 = int(sys.argv[3])
  n3 = int(sys.argv[4])
  n4 = int(sys.argv[5])
  n5 = int(sys.argv[6])
  n6 = int(sys.argv[7])
except ValueError:
  print("Erro: Os argumentos 2 a 7 devem ser números inteiros.")
  sys.exit(1)


#04-Verifica se os argumentos de 2 a 7 não são maiores que o tamanho da sequência de DNA
max_len = max(n1,n2,n3,n4,n5,n6)

if max_len > len(dna_sequence):
   print("Erro: Um ou mais argumento de 2 a 7 excedem o tamanho da sequência de DNA.")
   sys.exit(1)

#Extração das sequências codificadoras - CDS 1, CDS 2 e CDS 3
cds1 = dna_sequence[(n1-1):n2]
cds2 = dna_sequence[(n3-1):n4]
cds3 = dna_sequence[(n5-1):n6]

#Passo 3-Extração dos intros entre CDS 1 e CDS 2, e verificando se a sequência inicia com os nucleotídeos GT e termina com os nucleotídeos AG
intron1 = dna_sequence[n2:(n3-1)]
len1 = len(intron1)
if not (intron1[0:2]=="GT" and intron1[(len1-2):len1]=="AG"):
        print("Erro: O intron entre CDS 1 e CDS 2 não é válido.")
        sys.exit(1)

#Passo 4-Extração dos intros entre CDS 2 e CDS 3, e verificando se a sequência inicia com>
intron2 = dna_sequence[n4:(n5-1)]
len2 = len(intron2)
if not (intron2[0:2]=="GT" and intron2[(len2-2):len2]=="AG"):
        print("Erro: O intron entre CDS 2 e CDS 3 não é válido.")
        sys.exit(1)

#Se ambos os passos 3 e 4 forem válidos, juntar o CDS 1, CDS 2 e CDS 3
juncao_sequence = cds1 + cds2 + cds3
print(f"A sequência concatenada das CDS 1, 2 e 3 é: {juncao_sequence}")
