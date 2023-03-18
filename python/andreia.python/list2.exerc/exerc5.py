nota_1 = float(input("Digite sua primeira nota: "))
nota_2 = float(input("Digite sua nota segunda nota: "))
nota_3 = float(input("Digite sua nota terceira nota: "))
media_exerc = float(input("Digite sua media de exercicios: "))
media_aprov = ((nota_1 + nota_2*2 + nota_3*3) + media_exerc)/7

print(f"A media de aproveitamento deste aluno e: {media_aprov:.1f}".format(media_aprov))

if (media_aprov>=9):
    print("Sua nota e A ")

elif (media_aprov>=7.5<9):
    print("Sua nota e B ")

elif (media_aprov>=6.0<7.5):
    print("Sua nota e C ")

elif (media_aprov<6.0):
    print("Sua nota e D ")
    



