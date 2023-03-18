numero = int(input("Digite um numero: "))
metade = (numero/2)
i = 1

while(numero):
    if((numero % 2)== 0):
        print("O numero digitado não é primo ")
        break
        
    elif((numero % 1)== 0) and ((numero % numero)== 0):
        print("O numero digitado é primo ")
        break
