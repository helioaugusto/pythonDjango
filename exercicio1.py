#!/usr/bin/env python3

'''
Exercício com execução condicional
====================================
Escreva um programa que solicite do usuário uma entrada de número, teste se o mesmo é 
positivo ou negativo e escreva o resultado na tela.
'''

numero = int(input("Digite um número inteiro:"))
if numero > 0:
	print("O número que você digitou é positivo.")
elif numero == 0:
        print("Voce digitou o numero ZERO")
else:
	print("O número que você digitou é negativo.")
