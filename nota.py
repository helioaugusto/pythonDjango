#Programa Note While

nota = float(input("Digite uma nota de 0 a 10:"))
while nota < 0 or nota >10:
    print(" Você digitou uma nota inválida.")
    nota = float(input("Digite uma nota de 0 a 10:"))
print ("Nota valida")

