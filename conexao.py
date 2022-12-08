import sqlite3

def CriarBanco():
    #Cria o banco.O cursor é responsavel pelos comandos sql
    banco = sqlite3.connect('banco.bd')
    cursor = banco.cursor()
    
    #cursor.execute("CREATE TABLE contas (usuario text, senha integer)")
    
    cursor.execute("INSERT INTO contas VALUES('adm',12345)")
    banco.commit()



CriarBanco()
