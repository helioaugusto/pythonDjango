#!/usr/bin/env python3

# Usuário informa dados pessoais

nome = input("Digite seu nome:")
idade = int(input("Digite sua idade:"))
if idade<=10:
    print(nome,"você é criança.")
elif idade>=11&idade<=16:
    print(nome,"você é jovem.")
elif idade>=17&idade<=30:
    print(nome,"você é adulto")
else:
    print(nome,"você é experiente.")
    
    
