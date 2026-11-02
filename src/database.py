
import sqlite3
from pathlib import Path

CAMINHO_BANCO = Path(__file__).resolve().parent.parent / "tarefas.db"


def conectar():
    conexao = sqlite3.connect(CAMINHO_BANCO)
    conexao.row_factory = sqlite3.Row
    return conexao


def criar_tabela():
    conexao = conectar()

    conexao.execute("""
        CREATE TABLE IF NOT EXISTS tarefas (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            titulo TEXT NOT NULL,
            descricao TEXT,
            prioridade TEXT NOT NULL,
            status TEXT NOT NULL DEFAULT 'Pendente'
        )
    """)

    conexao.commit()
    conexao.close()
