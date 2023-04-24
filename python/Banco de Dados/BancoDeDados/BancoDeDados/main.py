import pyodbc as bd
import os
import getpass as gp

def conectar():
    global conexao
    os.system('cls') or None
    # conectar este programa ao servidor de banco de dados
    senha = gp.getpass("Digite a senha do seu banco de dados:")  # pede a senha
    conexao = bd.connect(driver="{SQL Server}",
                         server="regulus.cotuca.unicamp.br",
                         database="chico",
                         uid="chico",
                         pwd=f"{senha}")  # substitui variável senha 
                                          # pela senha digitada
    print("Conexão bem sucedida!")
    
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
    
def alterar():
    # cursor é um objeto que permite que nosso programa execute comandos
    # de SQL lá no servidor remoto:
    meuCursor = conexao.cursor()  # objeto de manipulação de dados
    numDepto = 1
    while numDepto != 0:
        # pedimos que o usuário digite o número do departamento a ser alterado
        numDepto = int(input("Número do departamento (0 para terminar): "))
        if numDepto != 0:    # usuário não quer terminar o cadastro
            # verifica no BD se existe um departamento com esse número digitado
            result = meuCursor.execute(
                    'SELECT NOMEDEPTO, GERENTE_NUMSEGSOCIAL, GERENTE_DATAINICIAL '+\
                    ' FROM EMPRESA.DEPARTAMENTO '+\
                    ' WHERE NUMDEPTO = ?', numDepto)
            registros = result.fetchall()
            if len(registros) == 0:
                print("Departamento não encontrado.")
            else:
                print("Registro encontrado:")
                print(registros)
                nomeDepto = registros[0][0]
                gerente = registros[0][1]
                data = registros[0][2]
                print("Nome do departamento: "+nomeDepto)
                print("Gerente:"+gerente)
                print("Data inicial:"+data)
                
                nomeDepto = input("Novo nome do departamento: ")
                gerente = input("Novo gerente do departamento:")
                data = input("Nova data de início do gerente (dd/mm/aaaa): ")
                
                if nomeDepto == "":  # usuário digitou [Enter]
                     nomeDepto = registros[0][0]    # nome original do BD
                     
                if gerente == "":   # usuário digitou [Enter]
                    gerente = registros[0][1]   # gerente original do BD
                    
                if data == "":   # usuário digitou [Enter]
                    data = registros[0][2]  # data original do BD
                        
            # criamos uma string com o comando Update para atualizar os novos dados
            sComando = "Update emp.departamento " +\
                       "       set nomeDepto = ?, gerente_numSegSocial = ?,"+\
                       "           gerente_dataInicial = ? "+\
                       " where numDepto = ? "
               
            # fazemos o cursor executar a string com o comando Update que criamos
            try:        # tente executar o comando abaixo:
                meuCursor.execute(sComando, nomeDepto, gerente, data, numDepto)
            except:     # em caso de erro
                print("Não foi possível incluir. Pode haver depto repetido.")
    
    # após digitar numDepto = 0, paramos o cadastramento
    # e enviamos os registros inseridos para serem definitivamente
    # gravados no servidor de banco de dados remoto
    meuCursor.commit() # enviar as mudanças para o BD   
    
def excluir():
    # cursor é um objeto que permite que nosso programa execute comandos
    # de SQL lá no servidor remoto:
    meuCursor = conexao.cursor()  # objeto de manipulação de dados
    numDepto = 1
    while numDepto != 0:
        # pedimos que o usuário digite o número do departamento a ser excluído
        numDepto = int(input("Número do departamento (0 para terminar): "))
        if numDepto != 0:    # usuário não quer terminar o cadastro
            # verifica no BD se existe um departamento com esse número digitado
            result = meuCursor.execute(
                    'SELECT NOMEDEPTO, GERENTE_NUMSEGSOCIAL, GERENTE_DATAINICIAL '+\
                    ' FROM EMPRESA.DEPARTAMENTO '+\
                    ' WHERE NUMDEPTO = ?', numDepto)
            registros = result.fetchall()
            if len(registros) == 0:
                print("Departamento não encontrado.")
            else:
                print("Registro encontrado:")
                nomeDepto = registros[0][0]
                gerente = registros[0][1]
                data = registros[0][2]
                print("Nome do departamento: "+nomeDepto)
                print("Gerente:"+gerente)
                print("Data inicial:"+data)
                
                resposta = input("Deseja realmente excluir (s/n)?")
                if resposta == "s":
                    # criamos uma string com o comando Delete para excluir o registro lido
                    sComando = "Delete from emp.departamento " +\
                            " where numDepto = ? "
                    
                    # fazemos o cursor executar a string com o comando Update que criamos
                    try:        # tente executar o comando abaixo:
                        meuCursor.execute(sComando, numDepto)
                    except:     # em caso de erro
                        print("Não foi possível excluir. Deve ser um departamento em uso.")
    
    # após digitar numDepto = 0, paramos o cadastramento
    # e enviamos os registros inseridos para serem definitivamente
    # gravados no servidor de banco de dados remoto
    meuCursor.commit() # enviar as mudanças para o BD   

def listar():
    # cursor é um objeto que permite que nosso programa execute comandos
    # de SQL lá no servidor remoto:
    meuCursor = conexao.cursor()  # objeto de manipulação de dados
    # busca no BD os registros de departamentos 
    result = meuCursor.execute(
                'SELECT numdepto, NOMEDEPTO, GERENTE_NUMSEGSOCIAL, GERENTE_DATAINICIAL '+\
                ' FROM EMPRESA.DEPARTAMENTO ')   
    registros = result.fetchall()
    print("Num. Nome       Gerente    Data Inicial")
    for depto in registros:
        print(f"{depto[0]}   {depto[1]}    {depto[2]}    {depto[3]}")
        
    input("Tecle [enter] para terminar:")
    
def seletor():
    opcao = 1
    while opcao != 0:
        os.system('cls') or None
        print("Operações disponíveis")
        print("========= ===========\n")
        print("0 - Terminar este programa")
        print("1 - Incluir departamentos")
        print("2 - Alterar departamentos")     
        print("3 - Excluir departamentos")
        print("4 - Listar departamentos")
        opcao = int(input("\nDigite o número da opção desejada:"))
        match opcao:
            case 1: incluir()
            case 2: alterar()
            case 3: excluir()
            case 4: listar()

conectar()
seletor()
conexao.close()  