import sqlite3


banco = sqlite3.connect('banco.bd')
cursor = banco.cursor()
    
    
def CriarBanco():
    #Cria o banco.O cursor é responsavel pelos comandos sql
    
    
    #cursor.execute("CREATE TABLE contas (usuario text, senha integer)")
    
    cursor.execute("INSERT INTO contas VALUES('adm',12345)")
    banco.commit()


if __name__ == "__main__":
    CriarBanco()
