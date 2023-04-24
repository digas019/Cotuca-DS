import pyodbc as bd
import os
import getpass as gp

global conexao
def conectar():
    os.system('cls') or None
    # conectar este programa ao servidor de banco de dados
    senha = gp.getpass("Digite a senha do seu banco de dados:")  # pede a senha
    conexao = bd.connect(driver="{SQL Server}",
                            server="regulus.cotuca.unicamp.br",
                            database="BD23513",
                            uid="BD23513",
                            pwd=f"{senha}")  # substitui variável senha 
                                            # pela senha digitada
    print("Conexão bem sucedida!")

def alterar():
    # cursor é um objeto que permite que nosso programa execute comandos
    # de SQL lá no servidor remoto:
    meuCursor = conexao.cursor()  # objeto de manipulação de dados
    numDepto = 1
    while numDepto != 0:
        # pedimos que o usuário digite o numero do departamento a ser alterado
        numDepto = int(input("Número do departamento (0 para terminar): "))
        if numDepto != 0:    # usuário não quer terminar o cadastro
            # verifica no BD se existe um departamento com esse numero digitado
            result = meuCursor.execute(
                    'SELECT NOMEDEPTO, GERENTE_NUMSEGSOCIAL, GERENTE_DATAINICIAL '+\
                    'FROM EMPRESA.DEPARTAMENTO '+\
                    'WHERE NUMDEPTO = ? ', numDepto)

            registros = result.fetchall()
            if len(registros) == 0:
                print("Departamento nao encontrado.")
            else:
                print("Registro encontrado:")
                print(registros)
                nomeDepto = registros[0][0]
                gerente = registros[0][1]
                dataInicial = registros[0][2]
                print("Nome do departamento: " +nomeDepto)
                print("Gerente:"+gerente)
                print("Data inicial:"+dataInicial)



            nomeDepto = input("Nome do departamento: ")
            gerente = input("Novo gerente do departamento: ")
            dataInicial = input("Data de início do gerente (dd/mm/aaaa): ")

            if nomeDepto == "": # usuario digitou [enter]
                    nomeDepto = registros [0][0] # nome original do BD

            if gerente == "": # usuario digitou [enter]
                gerente = registros[0][1] # gerente original do BD
            if dataInicial == "": # usuario digitou [enter]
                    dataInicial = registros[0][2] #data original do BD
            
            # criamos uma string com o comando Insert para inserir os novos dados
            sComando = "Update empresa.departamento " +\
                "       set nomeDepto = ?, gerente_numSegSocial = ?,"+\
                "           gerente_dataInicial = ? " +\
                " VALUES "+\
            f"({numDepto}, '{nomeDepto}', Convert(date,'{dataInicial}', 103))"
            
            # fazemos o cursor executar a string com o comando Insert que criamos
            try:        # tente executar o comando abaixo:
                meuCursor.execute(sComando,nomeDepto, gerente, dataInicial)
            except:     # em caso de erro
                print("Não foi possível incluir. Pode haver depto repetido.")
        
        # após digitar numDepto = 0, paramos o cadastramento
        # e enviamos os registros inseridos para serem definitivamente
        # gravados no servidor de banco de dados remoto
        meuCursor.commit() # enviar as mudanças para o BD        


def incluir():
        # cursor é um objeto que permite que nosso programa execute comandos
        # de SQL lá no servidor remoto:
        meuCursor = conexao.cursor()  # objeto de manipulação de dados
        numDepto = 1
        while numDepto != 0:
            # pedimos que o usuário digite os dados do novo departamento
            numDepto = int(input("Número do departamento (0 para terminar): "))
            if numDepto != 0:    # usuário não quer terminar o cadastro
                nomeDepto = input("Nome do departamento: ")
                dataInicial = input("Data de início do gerente (dd/mm/aaaa): ")
                
                # criamos uma string com o comando Insert para inserir os novos dados
                sComando = "insert into emp.departamento " +\
                    "       (numDepto, nomeDepto, gerente_dataInicial)"+\
                    " VALUES "+\
                f"({numDepto}, '{nomeDepto}', Convert(date,'{dataInicial}', 103))"
                
                # fazemos o cursor executar a string com o comando Insert que criamos
                try:        # tente executar o comando abaixo:
                    meuCursor.execute(sComando)
                except:     # em caso de erro
                    print("Não foi possível incluir. Pode haver depto repetido.")
        
        # após digitar numDepto = 0, paramos o cadastramento
        # e enviamos os registros inseridos para serem definitivamente
        # gravados no servidor de banco de dados remoto
        meuCursor.commit() # enviar as mudanças para o BD


def seletor():
    opcao = 1
    while opcao != 0:
        os.system('cls') or None
        print("Operacoes Disponiveis")
        print("======== =============\n")
        print("0 - Terminar este programa")
        print("1 - Incluir departamentos")
        print("2- Alterar Departamentos")
        print("3 - Excluir Departamentos")
        print("4 - Listar departamentos")
        opcao = int(input("\nDigite o numero da opcao desejada:"))
        match opcao:
            case 1: incluir()
            case 2: alterar()
            case 3: excluir()
            case 4: listar()

conectar()
seletor()
conexao.close()
