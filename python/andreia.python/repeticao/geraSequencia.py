while (True):
    print("Digite dois valores POSITIVOS para ver a sequencia entre eles")
    aPartirDeOnde = int(input("Digite o valor positivo para ser o inicio da sequencia: "))
    if (aPartirDeOnde==0):
        break

    ateOnde = int(input("Digite o valor positivo para ser o final da sequencia: "))

    item = aPartirDeOnde
    strItens = ""

    if (aPartirDeOnde>ateOnde): #Crescente
        while (item<=ateOnde):
            strItens = strItens +" "+ str(item)
            item = item + 1

    else: #Decrescente
        (aPartirDeOnde<=ateOnde)
        while(item>=ateOnde):
            strItens = strItens +" "+ str(item)
            item = item - 1

    print(strItens)

print("sim")


