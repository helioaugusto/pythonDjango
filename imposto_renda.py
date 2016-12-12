#!/usr/bin/env python3
#Programa para calcular imposto de renda

nome=input("Digite seu nome: ")
valor_salario=float(input("Digite o valor do seu salário: "))
if valor_salario > 1500:
    imposto=valor_salario - valor_salario * 0.75
    print(nome, "você pagará R$",imposto,"de imposto de renda")
else:
    print(nome, ",você não pagará imposto de renda")
    
    
