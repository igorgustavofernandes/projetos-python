# Sistema de Gerenciamento de Biblioteca

Sistema de gerenciamento de biblioteca desenvolvido em **Python**, com integração ao **MySQL**.

O projeto foi desenvolvido para praticar desenvolvimento de software, programação em Python, SQL, operações CRUD, relacionamentos entre entidades e integração entre uma aplicação e um banco de dados relacional.

## Funcionalidades

### Clientes

* Cadastrar clientes
* Listar clientes
* Buscar cliente por ID
* Buscar clientes por nome
* Buscar cliente por CPF
* Atualizar telefone
* Excluir cliente

### Autores

* Cadastrar autores
* Buscar autores por ID
* Associar autores aos livros

### Livros

* Cadastrar livros
* Listar livros
* Buscar livros por ID
* Associar livros aos autores
* Verificar disponibilidade de livros para empréstimo

### Empréstimos

* Registrar empréstimos
* Registrar devoluções
* Listar empréstimos ativos
* Consultar histórico de empréstimos
* Relacionar livros, clientes e funcionários aos empréstimos

## Tecnologias

* **Python**
* **MySQL**
* **SQL**
* **mysql-connector-python**
* **python-dotenv**
* **Git**
* **GitHub**

## Banco de dados

A aplicação utiliza **MySQL** como banco de dados relacional.

O sistema trabalha com entidades como:

* Clientes
* Livros
* Autores
* Funcionários
* Empréstimos

As consultas utilizam operações SQL como `SELECT`, `INSERT`, `UPDATE` e `DELETE`, além de `JOIN` para relacionar informações entre diferentes tabelas.

### Variáveis de ambiente

As credenciais do banco de dados são armazenadas em um arquivo `.env`, evitando que informações sensíveis sejam diretamente inseridas no código-fonte.

Exemplo:

```env
DB_HOST=localhost
DB_USER=root
DB_PASSWORD=sua_senha
DB_NAME=biblioteca
```

> O arquivo `.env` não é versionado pelo Git e está incluído no `.gitignore`.

## Estrutura do projeto

```text
biblioteca/
├── database.py
├── funcoes.py
├── funcoes_banco.py
├── main.py
├── testes.py
├── requirements.txt
└── biblioteca.json
```

### Principais arquivos

**`main.py`**
Contém o fluxo principal da aplicação e o menu de interação com o usuário.

**`funcoes.py`**
Contém funções relacionadas à lógica e à interface do sistema.

**`funcoes_banco.py`**
Concentra as operações de acesso e manipulação dos dados no MySQL.

**`database.py`**
Responsável pela conexão com o banco de dados e pelo carregamento das variáveis de ambiente.

**`testes.py`**
Utilizado durante o desenvolvimento para realizar testes das funções do sistema.

## Como executar

### 1. Clone o repositório

```bash
git clone https://github.com/igorgustavofernandes/projetos-python.git
```

### 2. Acesse o projeto

```bash
cd projetos-python/biblioteca
```

### 3. Crie um ambiente virtual

```bash
python -m venv .venv
```

### 4. Ative o ambiente virtual

No Windows:

```bash
.venv\Scripts\activate
```

### 5. Instale as dependências

```bash
python -m pip install -r requirements.txt
```

### 6. Configure o banco de dados

Crie um banco de dados MySQL chamado `biblioteca` e configure as tabelas utilizadas pela aplicação.

### 7. Configure o arquivo `.env`

Crie um arquivo `.env` na pasta do projeto:

```env
DB_HOST=localhost
DB_USER=root
DB_PASSWORD=sua_senha
DB_NAME=biblioteca
```

### 8. Execute a aplicação

```bash
python main.py
```

## Evolução do projeto

O projeto começou utilizando um arquivo **JSON** para armazenar os dados.

Durante o desenvolvimento, a aplicação foi migrada para **MySQL**, permitindo trabalhar com um banco de dados relacional e aprofundar conhecimentos em:

* SQL
* CRUD
* Relacionamentos entre tabelas
* `JOIN`
* Integração entre Python e MySQL
* Organização de código
* Variáveis de ambiente

Essa evolução também permitiu separar melhor a lógica da aplicação das operações relacionadas ao banco de dados.

## Objetivo

O projeto tem como objetivo consolidar conhecimentos em **Python, bancos de dados e desenvolvimento de software**, aplicando esses conceitos na construção de uma aplicação funcional de gerenciamento de biblioteca.

> Projeto desenvolvido para fins de estudo e portfólio.
