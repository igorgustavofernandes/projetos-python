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
    print('''
    1 - Listar clientes
    2 - Buscar cliente
    3 - Cadastrar cliente
    4 - Atualizar telefone
    5 - Excluir cliente
    6 - Cadastrar autor
    7 - Cadastrar livro
    8 - Cadastrar empréstimo
    0 - Sair
    ''')
    
    opc = pedir_opc_valida()
    
    if opc == 1:
        clientes = listar_clientes()
        for cliente in clientes:
            linha()
            print(f"ID: {cliente['id']}")
            print(f"Nome: {cliente['nome']}")
            print(f"Email: {cliente['email']}")

    elif opc == 2:
        linha()
        print("1 - Buscar por id")
        print("2 - Buscar por nome")
        linha()
        escolha = pedir_opc_valida()
        if escolha == 1:
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
        elif escolha == 2:
            nome = input("Digite o nome do cliente: ")
            clientes = buscar_clientes_por_nome(nome)
            if clientes:
                for cliente in clientes:
                    linha()
                    print(f'ID: {cliente["id"]}')
                    print(f'NOME: {cliente["nome"]}')
                    print(f'EMAIL: {cliente["email"]}')
                    linha()
            else:
                linha()
                print("Cliente não encontrado")
                linha()
        
    elif opc == 3:
        nome = input('Digite o nome: ')
        cpf = pedir_cpf()
        nacionalidade = input('Digite a nacionalidade: ')
        email = pedir_email()
        telefone = pedir_telefone()
        data_nascimento = pedir_data_nascimento()
        cliente = buscar_cliente_por_cpf(cpf)
        if cliente:
            linha()
            print("Esse CPF já está cadastrado!")
            linha()
        else:
            sucesso = cadastrar_cliente (
                nome=nome,
                cpf=cpf,
                nacionalidade=nacionalidade,
                email=email,
                telefone=telefone,
                data_nascimento=data_nascimento
                )
            linha()
            if sucesso:
                print("Cliente cadastrado com sucesso!")
            else:
                print('Não foi possível cadastrar o cliente!')
            linha()

    elif opc == 4:
        telefone = input('Digite o novo número: ')
        id_cliente = pedir_id()

        sucesso = atualizar_telefone(
            novo_telefone= telefone,
            id=id_cliente
        )
        if sucesso:
            print('Telefone atualizado com sucesso! ')
        else:
            print('ID não encontrado')
    

    elif opc == 5:
        id_cliente = pedir_id()
        sucesso = excluir_cliente(
        id=id_cliente
    )
        if sucesso:
            print('Cliente excluido com sucesso! ')
        else:
            print('ID não encontrado. ')

        titulo = input('Digite o título do livro: ')
        autor_id = pedir_id()
        ano_lancamento = int(input('Digite o ano de lançamento: '))
        genero = input('Digite o gênero: ')

        sucesso = cadastrar_livro(
            titulo=titulo,
            autor_id=autor_id,
            ano_lancamento=ano_lancamento,
            genero=genero
        )

        if sucesso:
            print('Livro cadastrado com sucesso!')
        else:
            print('Não foi possível cadastrar o livro!')

    elif opc == 6:
        nome = input('Digite o nome do autor: ')
        data_nascimento = pedir_data_nascimento()
        nacionalidade = input('Digite a nacionalidade: ')

        sucesso = cadastrar_autor(
            nome=nome,
            data_nascimento=data_nascimento,
            nacionalidade=nacionalidade
        )

        if sucesso:
            print('Autor cadastrado com sucesso!')
        else:
            print('Não foi possível cadastrar o autor!')

    elif opc == 7:
        titulo = input('Digite o título do livro: ')
        autor_id = pedir_id()
        ano_lancamento = int(input('Digite o ano de lançamento: '))
        genero = input('Digite o gênero: ')

        sucesso = cadastrar_livro(
            titulo=titulo,
            autor_id=autor_id,
            ano_lancamento=ano_lancamento,
            genero=genero
        )

        if sucesso:
            print('Livro cadastrado com sucesso!')
        else:
            print('Não foi possível cadastrar o livro!')

    elif opc == 8:
        livro_id = pedir_id()
        cliente_id = pedir_id()
        funcionario_id = pedir_id()
        data_emprestimo = input('Digite a data do empréstimo [yyyy-mm-dd]: ')

        sucesso = cadastrar_emprestimo(
            livro_id=livro_id,
            cliente_id=cliente_id,
            funcionario_id=funcionario_id,
            data_emprestimo=data_emprestimo
        )

        if sucesso:
            print('Empréstimo cadastrado com sucesso!')
        else:
            print('Não foi possível cadastrar o empréstimo!')

    elif opc == 0:
        print('Encerrando o sistema...')
        break

    else:
        print('Opção inválida!')