tabuada = int(input("Digite o número da tabela desejada: "))
print("A tabuada de",tabuada,"eh:")
for i in range(1,11):
    print(tabuada,"*",i,"=",tabuada*i)

print("+++++++++++++++")
for x in range(1,11):
    for y in range(1,11):
        print("%d x %d = %d" % (x,y,x*y))
    print("+++++++++++++++++")
