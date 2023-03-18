Nome = input("Seu nome ")
while(True):
    idade = int(input("Sua idade: "))
    
    if(idade<0):
        print("Sua idade nao pode ser negativa,digite novamente ")

    elif(idade>100):
        print("Por favor, dirija se para a arquibancada pois voce nao pode competir")

    else:
        break

end = input()