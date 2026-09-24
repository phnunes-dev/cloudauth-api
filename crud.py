from database import db
from auth import gerar_hash_senha, verificar_senha


def criar_usuario(nome: str, email: str, senha: str):
    with db() as conn:
        conn.execute(
            "INSERT INTO usuarios (nome, email, senha_hash) VALUES (?, ?, ?)",
            (nome, email, gerar_hash_senha(senha))
        )


def autenticar_usuario(email: str, senha: str):
    with db() as conn:
        usuario = conn.execute(
            "SELECT id, nome, email, senha_hash FROM usuarios WHERE email = ?", (email,)
        ).fetchone()

    if not usuario or not verificar_senha(senha, usuario["senha_hash"]):
        return None
    return {"id": usuario["id"], "nome": usuario["nome"], "email": usuario["email"]}


def listar_usuarios():
    with db() as conn:
        usuarios = conn.execute("SELECT id, nome, email FROM usuarios").fetchall()
    return [dict(u) for u in usuarios]


def atualizar_usuario(id: int, nome: str, email: str):
    with db() as conn:
        return conn.execute(
            "UPDATE usuarios SET nome = ?, email = ? WHERE id = ?", (nome, email, id)
        ).rowcount > 0


def excluir_usuario(id: int):
    with db() as conn:
        return conn.execute("DELETE FROM usuarios WHERE id = ?", (id,)).rowcount > 0