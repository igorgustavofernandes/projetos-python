def linha(tam=40):
    print('='*tam)

def titulo(txt):
    linha()
    print(txt)
    linha()

def leia_int(msg):
    while True:
        try:
            return int(input(msg))
        except (ValueError, TypeError):
            print('\033[31mERRO: Digite um número inteiro válido.\033[m')

def leia_nome(msg):
    while True:
        nome = str(input(msg)).strip()
        if nome.replace(' ', '').isalpha():
            return nome
        print('\033[31mERRO: Nomes não devem conter números ou símbolos.\033[m')

def mostrar():
        for indice, livro in enumerate(biblioteca):
            if len(biblioteca) == 0:
                print('Não existem livros cadastrados nesse sistema! ')
            else:
                linha()
                print(f'Livro #{indice + 1} ')
                print(f'Titulo: {livro["título"]}')
                print(f'Autor: {livro["autor"]}')
                print(f'Ano: {livro["ano"]}')
                print(f'disponível? {livro["disponibilidade"]}')
                linha()


def menu():
    titulo('Biblioteca')
    print('(1) - Cadastrar Livro')
    print('(2) - Listar Livro ')
    print('(3) - Pesquisar Livro')
    print('(4) - Emprestar Livro')
    print('(5) - Devolver livro')
    print('(6) - Remover livro')
    print('(7) - Sair')

def cadastro():
    livro = {}
    livro['título'] = str(input('Digite o título do livro: '))
    livro['autor'] = leia_nome('Digite o autor do livro: ')
    livro['ano'] = leia_int('Digite o ano de lançamento do livro: ')
    livro['disponibilidade'] = True
    biblioteca.append(livro.copy())

def listagem():
    mostrar()


def pesquisa():
    nome = str(input('Digite o título do livro que você deseja pesquisar: ')).strip().lower()
    listagem(nome)

def emprestimo():
    nome = str(input('Digite o título do livro que deseja emprestar: ')).strip().lower()
    for livro in biblioteca:
        if livro["título"].strip().lower() == nome:
            if livro["disponibilidade"]:
                print('Livro Emprestado! ')
                livro["disponibilidade"] = False
            else:
                print("Livro não dísponivel para emprestimo.")

def devolucao():
    nome = str(input('Digite o nome do livro que você deseja devolver: ')).strip().lower()
    achou = False
    for livro in biblioteca:
        if livro["título"].strip().lower() == nome:
            if not livro["disponibilidade"]:
                print('Livro devolvido com sucesso! ')
                livro["disponibilidade"] = True
                achou = True
            else:
                print('O livro encontrado já está disponível.')
        else:
            print('Não existe esse livro em nossa biblioteca.')

def remocao():
    nome = str(input('Digite o título do livro que você deseja remover: ')).strip().upper()
    achou = False
    for livro in biblioteca:
        if livro["título"].strip().upper() == nome:
            biblioteca.remove(livro)
            print('Livro removido com sucesso! ')
            achou = True
            break
    if not achou:
        print('Livro não encontrado')

biblioteca = []
while True:
    menu()
    opc = leia_int('Digite uma opção: ')
    if opc == 1:
        cadastro()
    elif opc == 2:
        listagem()
    elif opc == 3:
        pesquisa()
    elif opc == 4:
        emprestimo()
    elif opc == 5:
        devolucao()
    elif opc == 6:
        remocao()
    elif opc == 7:
        break
