fr = input("Escreva sua frase: ")
lt = input("Escreva uma letra: ")
contador = 0

for c in fr:
    if(c == lt):
        contador = contador + 1 
print(f"O numero de vezes que a letra escolhida aparece nessa frase e {contador}")