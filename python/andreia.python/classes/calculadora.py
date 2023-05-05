from operacoes import soma, subtracao, multiplicacao, divisao

while(True):
    print("\t\t1. Soma")
    print("\t\2. Subtracao")
    print("\t\3. Divisao")
    print("\t\4. Multiplicacao")
    print("\t\0. Sair")
    
    op = int(input("\t\tEscolha a Operacao "))
    
    if (op==0):
        break
    
    if (op<0) or (op>4):
        Mensagem("\t\tOpcao Invalida ")
    