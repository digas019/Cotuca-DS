peso = float(input("Digite seu peso em kg: "))
altura = float(input("Digite sua altura em metros: "))
imc = peso/altura**2

if (imc<=18.5):
    print("Voce esta abaixo do peso normal")

elif(18.5<imc<=25):
    print("Voce esta no peso normal")

elif(25<imc<=30):
    print("Voce esta acima do peso normal")

elif(imc>30):
    print("Voce esta na categoria obesidade")
