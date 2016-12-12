#!/usr/bin/env python3
'''
Exercicio breakWhile
----------------------------------
Escreva um programa que solicite ao usuario que digite algo no terminal
e como saida o programa escrevera a informaçao relativa ao cumprimento
da String digitada.
para sair encerrar o programa o usuario devera escrever a palavra 'sair'.
'''

texto = ""
while True:
    texto = input("Digite algo que voce deseje: ")
    print ("O tamanho do texto que voce digitou tem", len(texto),"caracteres")
    if texto == "sair":
        break


