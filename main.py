import sqlite3
from contextlib import asynccontextmanager
from fastapi import FastAPI, Depends, HTTPException, status
from pydantic import BaseModel, EmailStr
from database import create_table
from auth import criar_access_token, obter_usuario_atual
import crud


@asynccontextmanager
async def lifespan(app: FastAPI):
    create_table()
    yield


app = FastAPI(title="CRUD com Autenticação JWT", lifespan=lifespan)


class UsuarioBase(BaseModel):
    nome: str
    email: EmailStr


class UsuarioCreate(UsuarioBase):
    senha: str


class UsuarioLogin(BaseModel):
    email: EmailStr
    senha: str


class UsuarioUpdate(UsuarioBase):
    pass


# --- ROTAS PÚBLICAS ---

@app.post("/auth/registro", status_code=status.HTTP_201_CREATED)
def registrar(usuario: UsuarioCreate):
    try:
        crud.criar_usuario(usuario.nome, usuario.email, usuario.senha)
        return {"mensagem": "Usuário registrado com sucesso!"}
    except sqlite3.IntegrityError:
        raise HTTPException(status.HTTP_409_CONFLICT, "E-mail já cadastrado.")


@app.post("/auth/login")
def login(dados: UsuarioLogin):
    usuario = crud.autenticar_usuario(dados.email, dados.senha)
    if not usuario:
        raise HTTPException(status.HTTP_401_UNAUTHORIZED, "E-mail ou senha incorretos.")
    token = criar_access_token({"sub": str(usuario["id"]), "email": usuario["email"]})
    return {"access_token": token, "token_type": "bearer"}


# --- ROTAS PROTEGIDAS ---

@app.get("/usuarios")
def listar(usuario_atual: dict = Depends(obter_usuario_atual)):
    return crud.listar_usuarios()


@app.put("/usuarios/{id}")
def atualizar(id: int, dados: UsuarioUpdate, usuario_atual: dict = Depends(obter_usuario_atual)):
    if not crud.atualizar_usuario(id, dados.nome, dados.email):
        raise HTTPException(status.HTTP_404_NOT_FOUND, "Usuário não encontrado.")
    return {"mensagem": "Usuário atualizado com sucesso!"}


@app.delete("/usuarios/{id}")
def excluir(id: int, usuario_atual: dict = Depends(obter_usuario_atual)):
    if not crud.excluir_usuario(id):
        raise HTTPException(status.HTTP_404_NOT_FOUND, "Usuário não encontrado.")
    return {"mensagem": "Usuário excluído com sucesso!"}