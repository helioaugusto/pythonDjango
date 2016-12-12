#!/usr/bin/env python3

print("Programa em linguagem de Programaçao Python")

num1=int(input("Digite um numero inteiro:"))
num2=int(input("Digite outro numero inteiro:"))
nome=input("Digite seu nome: ")
print(nome,",voce digitou os numeros: ",num1,"e",num2)
print("A soma dos numeros e: ",num1 + num2)
print()
print()

# Saber se e par ou impar
print("Programa para saber se um numero e par ou impar")
num=int(input("Digite um numero inteiro: "))
if num%2 != 0:
    print ("O numero : ",num, "e impar")
else:
    print ("O numero ",num, "e par")
