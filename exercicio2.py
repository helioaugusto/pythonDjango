#!/usr/bin/env python3

'''
Exercício com execução condicional em cadeia
====================================
Escreva um programa que solicite do usuário a entrada de dois número,
e analise qual dos dois é maior e em seguida escreva o resultado na tela.

'''

num1=int(input("Digite o primeiro número: "))
num2=int(input("Digite o segundo número: "))

if num1>num2:
    print(num1, "é maior que",num2)
elif num1==num2:
    print(num1, "é igual a",num2)
else:
    print(num2, "é maior que",num1)
    
