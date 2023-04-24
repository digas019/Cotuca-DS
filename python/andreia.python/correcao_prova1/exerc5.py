def qtosDivisores(n):
    divisores = 1
    metade = n/2
    aux = 1
    while(aux<=metade):
        if(n%aux) == 0:
            divisores += 1
        aux += 1

    return divisores; 

qtos = 0

while(True):
    num = int(input("Digite um numero: "))
    if (num==0): break
    if (qtosDivisores(num)==5):
        qtos += 1

print(f"Foram digitados {qtos} numeros com 5 divisores")