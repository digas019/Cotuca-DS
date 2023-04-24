vet = [0] * 5
for i in range(len(vet)):
    vet[i] = int(input("Numero: "));

print(vet);
menor = vet[0];
posicaoMenor = 0;
maior = vet[0];
posicaoMaior = 0;
j=1 
while j<len(vet):
    if(vet[j] < menor):
        menor = vet[j];
    j = j + 1
print("menor elemento é " + str(menor))

print("Vetor na ordem  inversa a que foi digitado");
j = len(vet) -1;
while j > 1:
                           print(vet[j]);
    j = j-1;

print("O menor elemento é " + str(menor));                                                                                                                                                          