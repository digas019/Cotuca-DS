import random


sorteio = random.sample(range(1,10),1)
res = sorteio 
chance = 0
chute = int(input("Digite um numero de 1 a 10: "))

while(chance < 5):
    if (chute == res):
        print("Parabens!!!Voce acertou")

    elif(chute != res):
        chute = int(input("Digite um numero de 1 a 10: "))
        chance = chance + 1
        print(res)



