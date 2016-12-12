import random 
quant = int(input("Qnatidade"))
cont = 1
nomes = []
while cont <= quant:
    nome = input("O nome {} nome".format(cont))
    nomes.append(nome)
    cont+=1
random.shuffle(nomes)
escolha = random.choice(nomes)
print("Nome sorte:",escoolha)
