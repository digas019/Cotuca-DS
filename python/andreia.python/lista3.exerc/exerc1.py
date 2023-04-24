palavra = str(input("Digite uma palavra: "))
letra = "a"
cont = 0

for c in palavra:
    if(c == "a") or (c == "A"):
        cont = cont + 1

print(cont)

