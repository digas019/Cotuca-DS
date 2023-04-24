def mensagem(msg):
    print(msg);
    input("Pressione <ENTER> para continuar ")
def mostraMenu():
    print("_________-Cadastro dos Clientes-_______");
    print("1. Novo Registro");
    print("2. Alterar um Registro Existente");
    print("3. Deletar um Registro Existente");
    print("4. Pesquisar um registro/n");
    print("0. Sair/n");
    

def trataOpcao(opcao):
    match opcao: #match case feito para escolher a entrada para ser executada
        case 1:
            mensagem("Inlcuir");
        case 2:
            mensagem("Alterar");
        case 3:
            mensagem("Deletar");
        case 4:
            mensagem("Pesquisa");
        case _: #qualquer coisa diferente das opcoes, ele resulta em opcao invalida
            mensagem("Opcao Invalida");
    
    print(f"Sua opcao foi {opcao}");
    mensagem("");


mostraMenu();
op = int(input("Digite sua opcao: "))
trataOpcao(op)