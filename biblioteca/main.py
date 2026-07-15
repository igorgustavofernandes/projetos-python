from funcoes import *

biblioteca = carregar_dados()

while True:
    menu()

    opc = leia_opcao('Digite uma opção: ', 1, 7)

    if opc == 1:
        cadastro(biblioteca)
        salvar_dados(biblioteca)

    elif opc == 2:
        listagem(biblioteca)

    elif opc == 3:
        pesquisa(biblioteca)

    elif opc == 4:
        emprestimo(biblioteca)
        salvar_dados(biblioteca)

    elif opc == 5:
        devolucao(biblioteca)
        salvar_dados(biblioteca)

    elif opc == 6:
        remocao(biblioteca)
        salvar_dados(biblioteca)

    elif opc == 7:
        break

