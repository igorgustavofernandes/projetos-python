from funcoes import *
from funcoes_banco import *
from database import *


#livros = listar_livros()
#for livro in livros:
    #linha()
    #print(f"ID: {livro['id']}")
    #print(f"TÍTULO: {livro['titulo']}")
    #print(f"AUTOR: {livro['autor']}")
    #print(f"ANO DE LANÇAMENTO: {livro['ano_lancamento']}")
    #print(f"GÊNERO: {livro['genero']}")




#cliente = buscar_cliente(6)
#if cliente:
    #linha()
    #print(f'ID: {cliente["id"]}')
    #print(f'NOME: {cliente["nome"]}')
    #print(f'EMAIL: {cliente["email"]}')
    #linha()
#else:
    #print('Cliente não encontrado')

#nome = input('Digite o nome do cliente que deseja encontrar: ')
##linha()
#if clientes:
    #for cliente in clientes:
        #print(f'Nome: {cliente["nome"]}')
        #linha()
#else:
    #print('Nenhum cliente foi encontrado!')
    #linha()

while True:
    linha()
    print('SISTEMA DE BIBLIOTECA')
    linha()
    print(" 1 - Listar clientes")
    print(" 2 - Buscar cliente")
    print(" 3 - Cadastrar cliente")
    print(" 4 - Atualizar telefone")
    print(" 5 - Excluir cliente")
    print(" 0 - Sair")

    try:
        opc = int(input('Digite uma opção: '))
    except ValueError:
        print('Digite uma opção válida')

    
    if opc == 1:
        clientes = listar_clientes()
        for cliente in clientes:
            linha()
            print(f"ID: {cliente['id']}")
            print(f"Nome: {cliente['nome']}")
            print(f"Email: {cliente['email']}")

    elif opc == 2:
        id_cliente = pedir_id()
        cliente = buscar_cliente(id_cliente)
        if cliente:
            linha()
            print(f'ID: {cliente["id"]}')
            print(f'NOME: {cliente["nome"]}')
            print(f'EMAIL: {cliente["email"]}')
            linha()
        else:
            print('Cliente não encontrado')


    elif opc == 3:
        nome = input('Digite o nome: ')
        cpf = input('Digite o cpf: ')
        nacionalidade = input('Digite a nacionalidade: ')
        email = input('Digite o email: ')
        telefone = input('Digite o telefone: ')
        data_nascimento = input('Digite a data de nascimento [yyyy-mm-dd]: ')

        cadastrar_cliente (
        nome=nome,
        cpf=cpf,
        nacionalidade=nacionalidade,
        email=email,
        telefone=telefone,
        data_nascimento=data_nascimento
        )
        print('Cliente cadastrado com sucesso! ')

    elif opc == 4:
        telefone = input('Digite o novo número: ')
        id_cliente = pedir_id()

        atualizar_telefone(
        novo_telefone= telefone,
        id=id_cliente
    )
        print('Telefone atualizado com sucesso! ')

    elif opc == 5:
        id_cliente = pedir_id()
        excluir_cliente(
        id=id_cliente
    )

    elif opc == 0:
        print('Você desejou encerrar')
        break