from funcoes import *
from funcoes_banco import *
from database import *


nome = input('Digite o nome: ')
data_nascimento = pedir_data_nascimento()
nacionalidade = input('Digite a nacionalidade: ')

autor = buscar_autor(nome)

if autor:
    print('Esse autor já está cadastrado!')
else:
    sucesso = cadastrar_autor(
        nome=nome,
        data_nascimento=data_nascimento,
        nacionalidade=nacionalidade
    )

    if sucesso:
        print('Autor cadastrado com sucesso!')
    else:
        print('Não foi possível cadastrar o autor!')