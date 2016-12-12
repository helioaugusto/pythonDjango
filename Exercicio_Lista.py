#!/usr/bin/env python3
'''
Iterando lista
----------------------------------
Dada uma lista de valores, fornecida abaixo, escreva um progrma para encontrar
o maior valor sequenciado da esquerda para direira. O programa deverá escrever
a cada loop o valor atual da lista e qual o maior valor até aquele momento.
'''

lista = [1,9,41,12,3,74,15,0]
MaiorAteAgora = 0
print("Antes", MaiorAteAgora)
for n in lista:
    if n > MaiorAteAgora:
        MaiorAteaAgora = n
    print(MaiorAteaAgora, n)
print("Depois",MaiorAteAgora)

    
















