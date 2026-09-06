from funcoes import *
from funcoes_banco import *
from database import *

emprestimo = livro_esta_emprestado(5)

if emprestimo:
    print("🔴 Livro está emprestado")
else:
    print("🟢 Livro está disponível")