idade = int(input("Digite sua idade: "))

sem_class = range(0,5)
infanto_A = range(5,8)
infanto_B = range(8,11)
infanto_Juv = range(11,14)
juvenil = range(14,17)
junior = range(17,21)


if idade in sem_class:
    print("Voce se encontra na categoria Sem Classificacao")

elif idade in infanto_A :
    print("Voce se encontra na categoria Infantil A ")

elif idade in infanto_B:
    print("Voce se encontra na categoria Infantil B ")

elif idade in infanto_Juv:
    print("Voce se encontra na categoria Infanto Juvenil ")

elif idade in juvenil:
    print("Voce se encontra na categoria Juvenil ")

elif idade in junior:
    print("Voce se encontra na categoria Junior ")

elif(idade>20):
    print("Voce se encontra na categoria Adulto ")

