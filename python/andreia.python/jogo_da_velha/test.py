import os

#def mapa 
def mostraJogo(jogadas):
    print(f"{cores}")
    print()
    for i in range(9):
        match i:
            case 0:
                print(' 0', end='')
            case 1:
                print(' 1', end='')
            case 2:
                print(' 2', end='')
            case 3:
                print(' 3', end='')
            case 4:
                print(' 4', end='')
            case 5:
                print(' 5', end='')
            case 6:
                print(' 6', end='')
            case 7:
                print(' 7', end='')
            case 8:
                print(' 8', end='')
                
        if (i in [2,5,8]): 
            print(f"{jogadas[i]}")
            if (i!=8): print("---+---+---")
        else:
            print(f"{jogadas[i]}", end='|')

    print()

jogadas = [' '] * 9 

#def para posicao 

def funcionalidades_jogo()
    caract = [x,o]



#def para verificar posicao

jogador1 = '' #variavel global jogador
jogador2 = '' #variavel global jogador
def jogadores():
    jogador1 = input("Digite seu nickname (Jogador 1): ")
    print()
    jogador2 = input("Digite seu nickname (Jogador 2): ")

jogadores()
mostraJogo(jogadas)



#def jogadas

#def jogador


#cor 

cores = {
    'branco''\033[30',
    'vermelho''\033[31',
    'verde''\033[32',
    'amarelo''\033[33',
    'azul''\033[34',
    'magenta''\033[35',
    'cyano''\033[36 ',
    'branco''\033[37'
    'limpa' '\n\033[m'

}