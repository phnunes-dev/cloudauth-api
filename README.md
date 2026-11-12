# CloudAuth API

API REST de gerenciamento de usuários com autenticação JWT, desenvolvida com **Python e FastAPI**, utilizando **MySQL** como sistema de gerenciamento de banco de dados.

O projeto começou como uma aplicação CRUD com SQLite e evoluiu para uma arquitetura com MySQL, configuração segura de credenciais e organização das operações de banco de dados.

## Funcionalidades

- Cadastro e autenticação de usuários.
- Armazenamento de senhas utilizando hash bcrypt.
- Geração e validação de tokens JWT.
- Proteção de rotas por autenticação.
- Operações CRUD de usuários.
- Integração com banco de dados MySQL.
- Gerenciamento de configurações por variáveis de ambiente.
- Controle de dependências e versionamento com Git.

## Tecnologias

- Python 3.12
- FastAPI
- MySQL 8.0
- MySQL Connector/Python
- SQLite (versão anterior)
- PyJWT
- Passlib / bcrypt
- Pydantic
- Uvicorn
- python-dotenv
- Git e GitHub

## Estrutura do projeto

```text
cloudauth-api/
│
├── main.py
├── auth.py
├── crud.py
├── database.py
├── requirements.txt
├── .gitignore
├── .env
└── README.md
```

## Banco de dados

A aplicação utiliza MySQL como banco de dados principal.

A conexão é configurada por variáveis de ambiente, evitando armazenar credenciais diretamente no código.

Variáveis utilizadas:

```env
DB_HOST=localhost
DB_PORT=3306
DB_NAME=cloudauth
DB_USER=cloudauth_app
DB_PASSWORD=sua_senha
SECRET_KEY=sua_chave_secreta
```

O arquivo `.env` não deve ser publicado no GitHub.

## Rotas da API

| Método | Rota | Descrição | Autenticação |
|---|---|---|---|
| POST | `/auth/registro` | Cadastro de usuário | Não |
| POST | `/auth/login` | Autenticação e geração de JWT | Não |
| GET | `/usuarios` | Listagem de usuários | Sim |
| PUT | `/usuarios/{id}` | Atualização de usuário | Sim |
| DELETE | `/usuarios/{id}` | Exclusão de usuário | Sim |

## Executando o projeto

Com Python instalado e o MySQL configurado:

Instale as dependências:

```powershell
python -m pip install -r requirements.txt
```

Configure o arquivo `.env` com as credenciais do banco de dados e a chave JWT.

Inicie a aplicação:

```powershell
python -m uvicorn main:app --reload
```

A documentação interativa da API estará disponível em:

`http://127.0.0.1:8000/docs`

## Segurança e configuração

- Credenciais armazenadas em variáveis de ambiente.
- Arquivos sensíveis excluídos do versionamento pelo `.gitignore`.
- Senhas armazenadas em formato hash.
- Autenticação baseada em tokens JWT.
- Usuário específico do MySQL com permissões delimitadas ao banco da aplicação.

## Objetivo do projeto

Desenvolver uma aplicação que permita praticar integração entre serviços, gerenciamento de banco de dados, autenticação, segurança de credenciais e organização de aplicações Python.

O projeto também servirá como base para estudos de conteinerização com Docker e implantação de infraestrutura na AWS, incluindo EC2, RDS, IAM, VPC e CloudWatch.

**Status:** em desenvolvimento.
