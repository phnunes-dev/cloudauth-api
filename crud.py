
from database import db
from auth import gerar_hash_senha, verificar_senha


def criar_usuario(nome: str, email: str, senha: str):
    with db() as conn:
        cursor = conn.cursor()
        try:
            cursor.execute(
                "INSERT INTO usuarios (nome, email, senha_hash) VALUES (%s, %s, %s)",
                (nome, email, gerar_hash_senha(senha))
            )
        finally:
            cursor.close()


def autenticar_usuario(email: str, senha: str):
    with db() as conn:
        cursor = conn.cursor(dictionary=True)
        try:
            cursor.execute(
                "SELECT id, nome, email, senha_hash FROM usuarios WHERE email = %s",
                (email,)
            )
            usuario = cursor.fetchone()
        finally:
            cursor.close()

    if not usuario or not verificar_senha(senha, usuario["senha_hash"]):
        return None

    return {
        "id": usuario["id"],
        "nome": usuario["nome"],
        "email": usuario["email"]
    }


def listar_usuarios():
    with db() as conn:
        cursor = conn.cursor(dictionary=True)
        try:
            cursor.execute("SELECT id, nome, email FROM usuarios")
            usuarios = cursor.fetchall()
        finally:
            cursor.close()

    return usuarios


def atualizar_usuario(id: int, nome: str, email: str):
    with db() as conn:
        cursor = conn.cursor()
        try:
            cursor.execute(
                "UPDATE usuarios SET nome = %s, email = %s WHERE id = %s",
                (nome, email, id)
            )
            return cursor.rowcount > 0
        finally:
            cursor.close()


def excluir_usuario(id: int):
    with db() as conn:
        cursor = conn.cursor()
        try:
            cursor.execute(
                "DELETE FROM usuarios WHERE id = %s",
                (id,)
            )
            return cursor.rowcount > 0
        finally:
            cursor.close()
