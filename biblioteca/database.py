import mysql.connector

def conectar():
    conexao = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Igthnv23.",
        database="biblioteca"
    )
    return conexao

