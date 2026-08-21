from database import *
import mysql.connector

def listar_clientes():
    conexao = conectar()
    cursor = conexao.cursor(dictionary=True)
    clientes = []
    try:
        cursor.execute("SELECT * FROM clientes")
        clientes = cursor.fetchall()
    except mysql.connector.Error:
        print('Não foi possível realizar operação no Banco de Dados')
    finally:
        cursor.close()
        conexao.close()
    return clientes

def listar_livros():
    conexao = conectar()
    cursor = conexao.cursor(dictionary=True)
    livros = []
    try:
        cursor.execute("""
        SELECT livros.id, livros.titulo, livros.ano_lancamento, livros.genero, autores.nome AS autor 
        FROM livros 
        JOIN autores ON livros.autor_id = autores.id
        """)
        livros = cursor.fetchall()
    except mysql.connector.Error:
        print('Não foi possível realizar operação no Banco de Dados')
    finally:
        cursor.close()
        conexao.close()
    return livros

def cadastrar_cliente(nome, cpf, nacionalidade, email, telefone, data_nascimento):
    conexao = conectar()
    cursor = conexao.cursor()
    sql = ("""
    INSERT INTO clientes
    (nome, cpf, nacionalidade, email, telefone, data_nascimento)
    VALUES
    (%s ,%s ,%s, %s, %s, %s)
    """)
    valores = (
        nome, 
        cpf, 
        nacionalidade, 
        email, 
        telefone, 
        data_nascimento
        )
    try:
        cursor.execute(sql, valores)
        conexao.commit()
    except mysql.connector.Error:
        print('Erro ao executar a operação no Banco de Dados')
    finally:
        cursor.close()
        conexao.close()

def atualizar_telefone(id, novo_telefone):
    conexao = conectar()
    cursor = conexao.cursor()
    sql = ("""
        UPDATE clientes
        SET telefone = %s
        WHERE id = %s 
    """)
    valores = (
        novo_telefone,
        id
    )
    try:
        cursor.execute(sql, valores)
        if cursor.rowcount > 0:
            conexao.commit()
            return True
        else:
            return False
    except mysql.connector.Error:
        print('Erro ao executar a operação no Banco de Dados')
    finally:
        cursor.close()
        conexao.close()

def excluir_cliente(id):
    conexao = conectar()
    cursor = conexao.cursor()
    sql = ('DELETE FROM clientes WHERE id = %s')
    valores = (id,)
    try:
        cursor.execute(sql, valores)
        if cursor.rowcount > 0:
            conexao.commit()
            return True
        else:
            return False
    except mysql.connector.Error:
            print('Erro ao executar a operação no Banco de Dados')
    finally:
        cursor.close()
        conexao.close()

def buscar_cliente(id):
    conexao = conectar()
    cursor = conexao.cursor(dictionary=True)
    sql = (
    "SELECT * FROM clientes WHERE id = %s"
    )
    valor = (id,)
    try:
        cursor.execute(sql, valor)
        cliente = cursor.fetchone()
    except mysql.connector.Error:
            print('Erro ao executar a operação no Banco de Dados')
    finally:
        cursor.close()
        conexao.close()
    return cliente

def buscar_clientes_por_nome(nome):
    conexao = conectar()
    cursor = conexao.cursor(dictionary=True)
    sql = (
        "SELECT nome FROM clientes WHERE nome like %s"
    )
    valor = (f'%{nome}%',)
    try:
        cursor.execute(sql, valor)
        clientes = cursor.fetchall()
    except mysql.connector.Error:
            print('Erro ao executar a operação no Banco de Dados')
    finally:
        cursor.close()
        conexao.close()
    return clientes

def pedir_id():
    while True:
        try:
            id = int(input('Digite o id: '))
            return id
        except ValueError:
            print('Tente novamente um id válido: ')
    