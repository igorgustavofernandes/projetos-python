from database import *
import mysql.connector
from datetime import datetime, date

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
# OPERAÇÕES DE LIVROS (LISTAR, BUSCAR, CADASTRAR)
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

def cadastrar_livro(titulo, autor_id, ano_lancamento, genero):

    if buscar_autor(autor_id) is None:
        print('Autor não encontrado em nosso sistema')
        return False

    conexao = conectar()
    cursor = conexao.cursor()

    sql = ("""
        INSERT INTO livros
        (titulo, autor_id, ano_lancamento, genero)
        VALUES
        (%s, %s, %s, %s)
    """)

    valores = (
        titulo,
        autor_id,
        ano_lancamento,
        genero
    )

    try:
        cursor.execute(sql, valores)
        conexao.commit()
        return True

    except mysql.connector.Error:
        print('Erro ao executar a operação no Banco de Dados')
        return False

    finally:
        cursor.close()
        conexao.close()


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


# ==============================================================================
# OPERAÇÕES DE FUNCIONÁRIOS (LISTAR, BUSCAR)
# ==============================================================================

def buscar_funcionario(id):
    conexao = conectar()
    cursor = conexao.cursor(dictionary=True)
    funcionario = None

    sql = ("""
        SELECT *
        FROM funcionarios
        WHERE id = %s
    """)

    valor = (id,)

    try:
        cursor.execute(sql, valor)
        funcionario = cursor.fetchone()
    except mysql.connector.Error:
        print('Erro ao executar a operação no Banco de Dados')
    finally:
        cursor.close()
        conexao.close()

    return funcionario

# ==============================================================================
# OPERAÇÕES DE EMPRESTIMOS (LISTAR, BUSCAR)
# ==============================================================================

def cadastrar_emprestimo(livro_id, cliente_id, funcionario_id, data_emprestimo):

    if buscar_livro(livro_id) is None:
        print('Livro não encontrado em nosso sistema')
        return False

    if livro_esta_emprestado(livro_id) is not None:
        print('Esse livro está emprestado atualmente')
        return False
    
    if buscar_cliente(cliente_id) is None:
        print('Esse cliente não está cadastrado em nosso sistema')
        return False

    if buscar_funcionario(funcionario_id) is None:
        print('Funcionário inexistente')
        return False
    conexao = conectar()
    cursor = conexao.cursor()
    sql = ("""
    INSERT INTO emprestimos (livro_id, cliente_id, funcionario_id, data_emprestimo)
    VALUES (%s, %s, %s, %s)
    """)
    valores = (livro_id, cliente_id,funcionario_id,data_emprestimo)
    try:
        cursor.execute(sql,valores)
        conexao.commit()
        return True
    except mysql.connector.Error:
        print('Erro ao executar a operação no Banco de Dados')
        return False
    finally:
        cursor.close()
        conexao.close()

import mysql.connector

def devolver_livro(id_livro):
    data = date.today()
    if buscar_livro(id_livro) is None:
        print('O livro não está cadastrado em nosso sistema.')
        return False
    if not livro_esta_emprestado(id_livro):
        print('O livro não está emprestado atualmente.')
        return False
    conexao = conectar()
    cursor = conexao.cursor()
    sql = """
    UPDATE emprestimos
    SET data_devolutiva = %s
    WHERE livro_id = %s AND data_devolutiva IS NULL
    """
    valores = (data, id_livro)
    try:
        cursor.execute(sql, valores)
        conexao.commit()
        if cursor.rowcount == 1:
            return True
        return False
    except mysql.connector.Error:
        print(f'Erro ao executar a operação no Banco de Dados')
        return False
    finally:
        cursor.close()
        conexao.close()


                        
# ==============================================================================
# OPERAÇÕES DE AUTOR (LISTAR, BUSCAR, CADASTRAR)
# ==============================================================================

def buscar_autor(id):
    conexao = conectar()
    cursor = conexao.cursor(dictionary=True)
    autor = None

    sql = ("""
        SELECT *
        FROM autores
        WHERE id = %s
    """)

    valor = (id,)

    try:
        cursor.execute(sql, valor)
        autor = cursor.fetchone()
    except mysql.connector.Error:
        print('Erro ao executar a operação no Banco de Dados')
    finally:
        cursor.close()
        conexao.close()

    return autor
 
def cadastrar_autor(nome, data_nascimento, nacionalidade):
    conexao = conectar()
    cursor = conexao.cursor()
    sql = ("""
    INSERT INTO autores
    (nome, data_nascimento, nacionalidade)
    VALUES
    (%s ,%s ,%s)
    """)
    valores = (
        nome, 
        data_nascimento,
        nacionalidade
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

def listar_emprestimos_ativos():
    conexao = conectar()
    cursor = conexao.cursor(dictionary=True)
    emprestimos_ativos = []
    try:
        cursor.execute ("""
        SELECT emprestimos.livro_id,
        emprestimos.cliente_id,
        emprestimos.data_emprestimo,
        livros.titulo,
        clientes.nome AS cliente
        FROM emprestimos
        JOIN livros ON emprestimos.livro_id = livros.id
        JOIN clientes ON emprestimos.cliente_id = clientes.id
        WHERE emprestimos.data_devolutiva IS NULL;
        """)
        emprestimos_ativos = cursor.fetchall()
    except mysql.connector.Error:
        print("Erro ao executar a operação no Banco de Dados")
    finally:
        cursor.close()
        conexao.close()
    return emprestimos_ativos

        
def listar_historico_emprestimos():
    conexao = conectar()
    cursor = conexao.cursor(dictionary=True)
    historico = []
    try:
        cursor.execute("""
        select 
	        emprestimos.id, 
	        emprestimos.livro_id, 
            emprestimos.cliente_id,
            livros.titulo, 
            clientes.nome as cliente, 
            emprestimos.data_emprestimo,
            emprestimos.data_devolutiva 
        from emprestimos
        Join livros on emprestimos.livro_id = livros.id
        Join clientes on emprestimos.cliente_id = clientes.id
        order by emprestimos.data_emprestimo DESC; 
    """)
        historico = cursor.fetchall()
    except mysql.connector.Error:
        print('Erro ao executar a operação no Banco de Dados')
    finally:
        cursor.close()
        conexao.close()
    return historico