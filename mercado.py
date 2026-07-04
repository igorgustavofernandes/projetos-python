def linha(tam=42):
    print('-'*tam)

def titulo(txt):
    linha()
    print(txt.center(tam := 42) if len(txt) < 42 else txt)
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

# -- Funcões do Sistema -- #

def cadastro():
    aluno = []
    aluno.append(leia_nome('Digite o nome do aluno: '))
    aluno.append(leia_int(f'Digite a idade de {aluno[0]}: '))
    print(f'O aluno foi cadastrado com sucesso!')
    alunos.append(aluno[:])
    aluno.clear()

def pesquisa():
    titulo('Alunos')
    if len(alunos) == 0:
        print('Não existe alunos cadastrados ainda.')
        return
    nome = leia_nome('Digite o nome do aluno que deseja pesquisar: ')
    linha()
   
    achou = False
    for i, n in enumerate(alunos):
        if n[0].lower() == nome.lower(): 
            print(f'O aluno {n[0]} está cadastrado. Tem {n[1]} anos e é o nº {i+1} na lista.')
            linha(50)
            achou = True
            
    if not achou:
        print(f'Aluno "{nome}" não foi encontrado no sistema.')
        
                

def lista():
    if len(alunos) == 0:
        print('(NÃO EXISTEM ALUNOS CADASTRADOS)')
    else:
        for i, a in enumerate(alunos):
            print(f'{i+1} - {a[0]}')

def remover():
    if len(alunos) == 0:
        print('Não existe alunos cadastrados ainda.')
        return
    lista()
    linha()
    while True:
        opc = leia_int('Digite o número do aluno que você deseja remover: ')
        if 1 <= opc <= len(alunos):
            aluno_removido = alunos.pop(opc - 1)
            print(f'Aluno {aluno_removido[0]} removido com sucesso!')
            break
        else:
            print(f'\033[31mERRO: Não existe aluno com o número {opc}.\033[m')

        while True:
            opc2 = str(input('Deseja tentar novamente? (S/N): ')).strip().upper()
            if opc2 in ('S', 'N'):
                break
            print('Opção inválida, use S para SIM e N para NÃO')
            if opc2 == 'N':
                print('Operação de remoção cancelada.')
                break

alunos = []
while True:
    titulo('Escola genérica')
    print('\33[1;34m(1) - CADASTRAR UM NOVO ALUNO.\033[m')
    print('\33[1;34m(2) - PESQUISAR UM ALUNO\033[m ')
    print('\33[1;34m(3) - LISTAR ALUNOs\033[m ')
    print('\33[1;34m(4) - REMOVER UM ALUNO\033[m ')
    print('\33[1;34m(5) - ENCERRAR PROGRAMA\033[m')
    opc = leia_int('Digite uma opção: ')
    if opc == 1:
        titulo('CADASTRO DE ALUNOS')
        cadastro()
    elif opc == 2:
        pesquisa()
    elif opc == 3:
        titulo('ALUNOS')
        lista()
    elif opc == 4:
        titulo('ALUNOS')
        remover()
    elif opc == 5:
        print('Encerrando...')
        break
    else:
        print('\033[31mDigite uma opção válida entre 1 e 5!\033[m')
