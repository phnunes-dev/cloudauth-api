 CRUD com Autenticação JWT

API simples de CRUD de usuários com autenticação via JWT, feita em FastAPI + SQLite. Projeto de estudo, parte de uma trilha de aprendizado de backend/APIs.

 O que tem aqui

- Registro e login de usuário, com senha armazenada como hash (bcrypt via passlib)
- Geração e validação de token JWT
- Rotas protegidas por token (listar, atualizar e excluir usuário exigem autenticação)
- Banco SQLite, sem ORM — SQL direto, pra fixar os fundamentos antes de partir pra abstrações

 Tecnologias

- Python 3
- FastAPI
- SQLite
- PyJWT
- Passlib (bcrypt)

 Rotas

| Método | Rota              | Descrição                  | Requer token |
|--------|-------------------|-----------------------------|--------------|
| POST   | /auth/registro    | Cria um novo usuário        | Não          |
| POST   | /auth/login        | Autentica e retorna o token | Não          |
| GET    | /usuarios          | Lista todos os usuários     | Sim          |
| PUT    | /usuarios/{id}     | Atualiza nome/email         | Sim          |
| DELETE | /usuarios/{id}     | Remove um usuário           | Sim          |

 Como rodar

```bash
pip install fastapi uvicorn passlib[bcrypt] pyjwt "pydantic[email]"
python -m uvicorn main:app --reload
```

Depois é só acessar `http://127.0.0.1:8000/docs` — o FastAPI gera uma interface (Swagger) pra testar as rotas direto do navegador, sem precisar de Postman.

## Observações

O `SECRET_KEY` do JWT está com um valor padrão no código só pra facilitar rodar localmente. Em qualquer ambiente real, isso deveria vir de variável de ambiente, nunca hardcoded.
