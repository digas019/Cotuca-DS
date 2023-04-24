def substituirletra ():
    palavra = str(input("Digite sua frase: "))
    letrapadrao = str(input("Qual a letra a ser substituida?"))
    letranova = str(input("Qual a letra que quer substituir no lugar?"))

    for l in palavra:
        letraantiga = letranova
