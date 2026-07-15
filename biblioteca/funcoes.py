import json


def salvar_dados(biblioteca: list):
    with open('biblioteca.json', 'w', encoding='utf-8') as arquivo:
        json.dump(biblioteca, arquivo, indent=4, ensure_ascii=False)


def carregar_dados() -> list: 
    try:
        with open('biblioteca.json', 'r', encoding='utf-8') as arquivo:
            return json.load(arquivo)
    except FileNotFoundError:
        return []

def linha(tam=40):
    print('=' * tam)


def titulo(txt):
    linha()
    print(txt)
    linha()


def leia_int(msg):
    while True:
        try:
            return int(input(msg))
        except (ValueError, TypeError):
            print('ERRO: Digite um número inteiro válido.')


def leia_opcao(msg, minimo, maximo):
    while True:
        opc = leia_int(msg)
        if minimo <= opc <= maximo:
            return opc
        print('\033[31mDigite uma opção válida entre 1 e 7!\033[m')


def leia_ano(mensagem):
    while True:
        try:
            entrada = input(mensagem).strip()
            ano = int(entrada)
            if ano <= 0:
                print("Erro: O ano precisa ser maior que zero (D.C.). Tente novamente.")
                continue
            if ano > 3000:
                print("Erro: Esse ano está muito longe no futuro! Digite um ano até 3000.")
                continue
            return ano
        except ValueError:
            print("Erro: Digite um ano inteiro válido (apenas números).")
        except (KeyboardInterrupt, EOFError):
            print("\nEntrada interrompida pelo usuário.")
            return None


def menu():
    titulo('Biblioteca')
    print('(1) - Cadastrar Livro')
    print('(2) - Listar Livro ')
    print('(3) - Pesquisar Livro')
    print('(4) - Emprestar Livro')
    print('(5) - Devolver livro')
    print('(6) - Remover livro')
    print('(7) - Sair')


def leia_txt(msg):
    while True:
        try:
            entrada = input(msg).strip()
            if entrada == "":
                print('\033[31mERRO: O campo não pode ficar vazio.\033[m')
                continue
            return entrada
        except (KeyboardInterrupt, EOFError):
            print('\nEntrada interrompida pelo usuário.')
            return None


def mostrar(livro):
    print(f'Título: {livro["título"]}')
    print(f'Autor: {livro["autor"]}')
    print(f'Ano: {livro["ano"]}')
    print(f'Disponível? {"Sim" if livro["disponibilidade"] else "Não"}')
    linha()


def cadastro(biblioteca):
    livro = {}
    livro['título'] = leia_txt('Digite o título do livro: ')
    livro['autor'] = leia_txt('Digite o autor do livro: ')
    livro['ano'] = leia_ano('Digite o ano de lançamento do livro: ')
    livro['disponibilidade'] = True
    biblioteca.append(livro.copy())
    salvar_dados(biblioteca)
    print('Livro cadastrado com sucesso!')


def listagem(biblioteca):
    if len(biblioteca) == 0:
        print('Não existem livros cadastrados nesse sistema!')
        return
    for indice, livro in enumerate(biblioteca):
        linha()
        print(f'Livro #{indice + 1}')
        mostrar(livro)


def pesquisa(biblioteca):
    if len(biblioteca) == 0:
        print('Não existem livros cadastrados para pesquisa.')
        return
    nome = leia_txt('Digite o título do livro que deseja pesquisar: ').lower()
    achou = False
    for indice, livro in enumerate(biblioteca):
        if livro['título'].strip().lower() == nome:
            linha()
            print('Livro encontrado com sucesso!')
            print(f'Livro #{indice + 1}')
            mostrar(livro)
            achou = True
    if not achou:
        print('Livro não encontrado.')
        linha()


def emprestimo(biblioteca):
    nome = leia_txt('Digite o título do livro que deseja emprestar: ').lower()
    achou = False
    for livro in biblioteca:
        if livro['título'].strip().lower() == nome:
            achou = True
            if livro['disponibilidade']:
                livro['disponibilidade'] = False
                salvar_dados(biblioteca)
                print('Livro emprestado com sucesso!')
            else:
                print('Livro já está emprestado.')
            break
    if not achou:
        print('Livro não encontrado.')


def devolucao(biblioteca):
    nome = leia_txt('Digite o título do livro que deseja devolver: ').lower()
    achou = False
    for livro in biblioteca:
        if livro['título'].strip().lower() == nome:
            achou = True
            if not livro['disponibilidade']:
                livro['disponibilidade'] = True
                salvar_dados(biblioteca)
                print('Livro devolvido com sucesso!')
            else:
                print('O livro já está disponível.')
            break
    if not achou:
        print('Livro não encontrado.')


def remocao(biblioteca):
    nome = leia_txt('Digite o título do livro que deseja remover: ').lower()
    achou = False
    for livro in biblioteca:
        if livro['título'].strip().lower() == nome:
            biblioteca.remove(livro)
            salvar_dados(biblioteca)
            print('Livro removido com sucesso!')
            achou = True
            break
    if not achou:
        print('Livro não encontrado.')