from funcoes import *
from funcoes_banco import *
from database import *
from datetime import date

historico = listar_historico_emprestimos()

for emprestimo in historico:
    print(emprestimo)