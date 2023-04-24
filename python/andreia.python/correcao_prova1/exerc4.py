soma = 0
media = 0.0
cont = 1
while(cont<21):
    print(f"Digite os dados da {cont}a. pessoa")
    nome = input("Digite seu nome: ")
    idade = int(input("Digite sua idade: "))
    soma = soma + idade
    cont += 1

media = soma / (cont-1)

print(f"A media de idades é {media}")