cont1 = 0
cont2 = 0
cont3 = 0

while(True):
    num = int(input("Digite um numero inteiro: "))
    if (num==0): break

    if(num%5)==0:
        print("Dirija se a porta numero 1")
        cont1 = cont1 + 1
    elif(num%3)==0:
        print("Dirija se a porta numero 2")
        cont2 = cont2 + 1
    else:
        print("Dirija se a porta numero 3 ")
        cont3 = cont3 + 1

print("Porta 1 = + {cont1}")
print("Porta 1 =  {cont2}")
print("Porta 1 =  + {cont3}")
