import pyodbc as bd
import os
import getpass as gp

def acessar():
    os.system('cls') or None
    # conectar este programa ao servidor de banco de dados
    senha = gp.getpass("Digite a senha do seu banco de dados:")
    conexao = bd.connect(driver = "{SQL Server})",
                        server = "regulus.cotuca.unicamp.br",
                        database = "BD23513",
                        uid = "BD23513",
                        pwd = f"{senha}")
    print("Conexao bem sucedida!")