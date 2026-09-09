from datetime import date
from database import *
from funcoes import *
from funcoes_banco import *

while True:

    print("=" * 45)
    print("      SISTEMA DE GERENCIAMENTO DE BIBLIOTECA   ")
    print("=" * 45)
    print("""
    [ 1 ] Listar clientes
    [ 2 ] Buscar cliente
    [ 3 ] Cadastrar cliente
    [ 4 ] Atualizar telefone
    [ 5 ] Excluir cliente
    ---------------------------
    [ 6 ] Cadastrar autor
    [ 7 ] Cadastrar livro
    ---------------------------
    [ 8 ] Cadastrar empréstimo
    [ 9 ] Devolver livro
    [ 10 ] Listar emprestimos ativos
    ---------------------------
    [ 0 ] Sair do Sistema
    """)
    linha()

    opc = pedir_opc_valida()
    linha()

    # 1 - LISTAR CLIENTES
    if opc == 1:
        print("\n=== LISTA DE CLIENTES ===")
        clientes = listar_clientes()
        if clientes:
            for cliente in clientes:
                linha()
                print(f"ID:    {cliente['id']}")
                print(f"Nome:  {cliente['nome']}")
                print(f"Email: {cliente['email']}")
            linha()
        else:
            linha()
            print("Nenhum cliente cadastrado.")
            linha()

    # 2 - BUSCAR CLIENTE
    elif opc == 2:
        linha()
        print("=== BUSCAR CLIENTE ===")
        print("[ 1 ] Buscar por ID")
        print("[ 2 ] Buscar por Nome")
        linha()
        
        escolha = pedir_opc_valida()
        
        if escolha == 1:
            id_cliente = pedir_id()
            cliente = buscar_cliente(id_cliente)
            linha()
            if cliente:
                print(f"ID:    {cliente['id']}")
                print(f"NOME:  {cliente['nome']}")
                print(f"EMAIL: {cliente['email']}")
            else:
                print("Cliente não encontrado.")
            linha()

        elif escolha == 2:
            nome = input("Digite o nome do cliente: ")
            clientes = buscar_clientes_por_nome(nome)
            if clientes:
                for cliente in clientes:
                    linha()
                    print(f"ID:    {cliente['id']}")
                    print(f"NOME:  {cliente['nome']}")
                    print(f"EMAIL: {cliente['email']}")
                linha()
            else:
                linha()
                print("Cliente não encontrado.")
                linha()

    # 3 - CADASTRAR CLIENTE
    elif opc == 3:
        print("\n=== CADASTRO DE CLIENTE ===")
        nome = input("Digite o nome: ")
        cpf = pedir_cpf()
        nacionalidade = input("Digite a nacionalidade: ")
        email = pedir_email()
        telefone = pedir_telefone()
        data_nascimento = pedir_data_nascimento()

        cliente = buscar_cliente_por_cpf(cpf)
        linha()
        if cliente:
            print("Atenção: Esse CPF já está cadastrado!")
        else:
            sucesso = cadastrar_cliente(
                nome=nome,
                cpf=cpf,
                nacionalidade=nacionalidade,
                email=email,
                telefone=telefone,
                data_nascimento=data_nascimento,
            )
            if sucesso:
                print("Cliente cadastrado com sucesso!")
            else:
                print("Não foi possível cadastrar o cliente!")
        linha()

    # 4 - ATUALIZAR TELEFONE
    elif opc == 4:
        print("\n=== ATUALIZAÇÃO DE TELEFONE ===")
        id_cliente = pedir_id()
        telefone = input("Digite o novo número: ")

        sucesso = atualizar_telefone(novo_telefone=telefone, id=id_cliente)
        linha()
        if sucesso:
            print("Telefone atualizado com sucesso!")
        else:
            print("ID não encontrado.")
        linha()

    # 5 - EXCLUIR CLIENTE
    elif opc == 5:
        print("\n=== EXCLUSÃO DE CLIENTE ===")
        id_cliente = pedir_id()
        sucesso = excluir_cliente(id=id_cliente)
        
        linha()
        if sucesso:
            print("Cliente excluído com sucesso!")
        else:
            print("ID não encontrado.")
        linha()

    # 6 - CADASTRAR AUTOR
    elif opc == 6:
        print("\n=== CADASTRO DE AUTOR ===")
        nome = input("Digite o nome do autor: ")
        data_nascimento = pedir_data_nascimento()
        nacionalidade = input("Digite a nacionalidade: ")

        sucesso = cadastrar_autor(
            nome=nome,
            data_nascimento=data_nascimento,
            nacionalidade=nacionalidade,
        )

        linha()
        if sucesso:
            print("Autor cadastrado com sucesso!")
        else:
            print("Não foi possível cadastrar o autor!")
        linha()

    # 7 - CADASTRAR LIVRO
    elif opc == 7:
        print("\n=== CADASTRO DE LIVRO ===")
        titulo = input("Digite o título do livro: ")
        autor_id = pedir_id()
        ano_lancamento = int(input("Digite o ano de lançamento: "))
        genero = input("Digite o gênero: ")

        sucesso = cadastrar_livro(
            titulo=titulo,
            autor_id=autor_id,
            ano_lancamento=ano_lancamento,
            genero=genero,
        )

        linha()
        if sucesso:
            print("Livro cadastrado com sucesso!")
        else:
            print("Não foi possível cadastrar o livro!")
        linha()

    # 8 - CADASTRAR EMPRÉSTIMO
    elif opc == 8:
        print("\n=== REGISTRO DE EMPRÉSTIMO ===")
        livro_id = pedir_id()
        cliente_id = pedir_id()
        funcionario_id = pedir_id()
        data_emprestimo = input("Digite a data do empréstimo [yyyy-mm-dd]: ")

        sucesso = cadastrar_emprestimo(
            livro_id=livro_id,
            cliente_id=cliente_id,
            funcionario_id=funcionario_id,
            data_emprestimo=data_emprestimo,
        )

        linha()
        if sucesso:
            print("Empréstimo cadastrado com sucesso!")
        else:
            print("Não foi possível cadastrar o empréstimo!")
        linha()

    # 9 - DEVOLVER LIVRO
    elif opc == 9:
        print("\n=== DEVOLUÇÃO DE LIVRO ===")
        id_livro = int(input("Digite o ID do livro: "))
        
        linha()
        if devolver_livro(id_livro):
            print("Devolução confirmada com sucesso!")
        else:
            print("Devolução não efetivada.")
        linha()

    # 10 - Listar emprestimos ativos 
    elif opc == 10:
        print("\n=== LISTA DE EMPRESTIMOS ATIVOS ===")
        print()
        emprestimos = listar_emprestimos_ativos()
        if emprestimos:
            for emprestimo_ativo in emprestimos:
                print(f"ID Livro: {emprestimo_ativo['livro_id']}")
                print(f"ID CLIENTE: {emprestimo_ativo['cliente_id']}")
                print(f"DATA EMPRESTIMO: {emprestimo_ativo['data_emprestimo']}")
                print(f"TÍTULO: {emprestimo_ativo['titulo']}")
                print(f"CLIENTE: {emprestimo_ativo['cliente']}")
                print("-" * 40)
        else:
            print('Não há nenhum emprestimo ativo nesse momento')

    # 0 - SAIR
    elif opc == 0:
        linha()
        print("Encerrando o sistema... Até logo!")
        linha()
        break

    else:
        linha()
        print("Opção inválida! Tente novamente.")
        linha()