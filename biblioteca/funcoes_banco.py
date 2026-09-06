from database import *
import mysql.connector
from datetime import datetime

# ==============================================================================
# FUNÇÕES AUXILIARES / ENTRADAS DO USUÁRIO (PEDIR)
# ==============================================================================

def pedir_id():
    while True:
        try:
            id = int(input('Digite o id: '))
            return id
        except ValueError:
            print('Tente novamente um id válido: ')

def pedir_opc_valida():
    while True:
        try:
            opc = int(input('Digite sua opção: '))
            return opc
        except ValueError:
            print('Tente novamente uma opção válida: ')

def pedir_cpf():
    while True:
        cpf = input('Digite o CPF: ')

        if len(cpf) != 11:
            print('O CPF precisa conter 11 dígitos.')
        elif not cpf.isnumeric():
            print('O CPF deve conter apenas números.')
        else:
            return cpf

def pedir_telefone():
    while True:
        telefone = input('Digite o telefone: ')

        if len(telefone) != 11:
            print('O telefone precisa conter 11 dígitos.')
        elif not telefone.isnumeric():
            print('O telefone deve conter apenas números.')
        else:
            return telefone

def pedir_email():
    while True:
        email = input('Digite o email: ')

        if ' ' not in email and '@' in email and '.' in email:
            return email
        else:
            print('Email inválido')
            
def pedir_data_nascimento():
    while True:
        data = input("Digite uma data [yyyy-mm-dd]: ")

        try:
            datetime.strptime(data, "%Y-%m-%d")
            return data
        except ValueError:
            print("Data inválida. Tente novamente.")


# ==============================================================================
# OPERAÇÕES DE CLIENTES (CADASTRAR, LISTAR, BUSCAR, ATUALIZAR, EXCLUIR)
# ==============================================================================

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
        return True
    except mysql.connector.Error:
        print("Erro ao executar a operação no Banco de Dados")
        return False
    finally:
        cursor.close()
        conexao.close()

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

def buscar_cliente(id):
    conexao = conectar()
    cursor = conexao.cursor(dictionary=True)
    cliente = None
    sql = "SELECT * FROM clientes WHERE id = %s"
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
    sql = "SELECT * FROM clientes WHERE nome LIKE %s"
    valor = (f'%{nome}%',)
    clientes = []
    try:
        cursor.execute(sql, valor)
        clientes = cursor.fetchall()
    except mysql.connector.Error:
        print('Erro ao executar a operação no Banco de Dados')
    finally:
        cursor.close()
        conexao.close()
    return clientes

def buscar_cliente_por_cpf(cpf):
    conexao = conectar()
    cursor = conexao.cursor(dictionary=True)
    cliente = None
    sql = "SELECT * FROM clientes WHERE cpf = %s"
    valor = (cpf,)
    try:
        cursor.execute(sql, valor)
        cliente = cursor.fetchone()
    except mysql.connector.Error:
        print('Erro ao executar a operação no Banco de Dados')
    finally:
        cursor.close()
        conexao.close()
    return cliente

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
        return False
    finally:
        cursor.close()
        conexao.close()

def excluir_cliente(id):
    conexao = conectar()
    cursor = conexao.cursor()
    sql = 'DELETE FROM clientes WHERE id = %s'
    valores = (id,)
    try:
        cursor.execute(sql, valores)
        if cursor.rowcount > 0:
            conexao.commit()
            return True
        else:
            return False
    except mysql.connector.Error:
        print("Erro ao executar a operação no Banco de Dados")
        return False
    finally:
        cursor.close()
        conexao.close()


# ==============================================================================
# OPERAÇÕES DE LIVROS (LISTAR, BUSCAR)
# ==============================================================================

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

def buscar_livro(id):
    conexao = conectar()
    cursor = conexao.cursor(dictionary=True)
    livro = None
    sql = ("""
        SELECT livros.id, livros.titulo, livros.ano_lancamento, livros.genero, autores.nome AS autor 
        FROM livros 
        JOIN autores ON livros.autor_id = autores.id
        WHERE livros.id = %s
    """)
    valor = (id,)
    try:
        cursor.execute(sql, valor)
        livro = cursor.fetchone()
    except mysql.connector.Error:
        print('Erro ao executar a operação no Banco de Dados')
    finally:
        cursor.close()
        conexao.close()
    return livro

def livro_esta_emprestado(id):
    conexao = conectar()
    cursor = conexao.cursor(dictionary=True)
    emprestimo = None
    sql = ("""
        SELECT *
        FROM emprestimos
        WHERE livro_id = %s
        AND data_devolutiva IS NULL
        """)
    valor = (id,)
    try:
        cursor.execute(sql,valor)
        emprestimo = cursor.fetchone()
    except mysql.connector.Error:
            print('Erro ao executar a operação no Banco de Dados')
    finally:
        cursor.close()
        conexao.close()
    return emprestimo