#!/usr/bin/env python3
num = 21
resposta = 0
while resposta != num:
    resposta = int(input("Digite um número: "))     
    if resposta == num:
        print ("Parabéns! Você Acertou")
        break
    elif resposta > num:
        print(" O número é menor")
  
    else:
        print(" O número é maior")
  
