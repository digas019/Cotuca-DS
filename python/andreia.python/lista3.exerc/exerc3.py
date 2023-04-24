frase = input("Digite sua frase: ")
fraseInv = str()

for l in frase[::-1]:
    fraseInv += l

print(fraseInv)

