
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from app import app


def test_pagina_inicial():
    app.config["TESTING"] = True

    cliente = app.test_client()

    resposta = cliente.get("/")

    assert resposta.status_code == 200
    assert b"DebTec Task Manager" in resposta.data

def test_cadastrar_tarefa():
    app.config["TESTING"] = True

    cliente = app.test_client()

    resposta = cliente.post(
        "/adicionar",
        data={
            "titulo": "Tarefa de teste",
            "descricao": "Testando o cadastro",
            "prioridade": "Alta"
        },
        follow_redirects=True
    )

    assert resposta.status_code == 200
    assert b"Tarefa de teste" in resposta.data

def test_excluir_tarefa():
    app.config["TESTING"] = True

    cliente = app.test_client()

    resposta = cliente.post(
        "/adicionar",
        data={
            "titulo": "Tarefa para excluir",
            "descricao": "Teste de exclusão",
            "prioridade": "Baixa"
        },
        follow_redirects=True
    )

    assert b"Tarefa para excluir" in resposta.data

    from app import conectar

    conexao = conectar()
    tarefa = conexao.execute(
        "SELECT id FROM tarefas WHERE titulo = ?",
        ("Tarefa para excluir",)
    ).fetchone()
    conexao.close()

    assert tarefa is not None

    resposta = cliente.post(
        f"/excluir/{tarefa['id']}",
        follow_redirects=True
    )

    assert resposta.status_code == 200
    assert b"Tarefa para excluir" not in resposta.data
def test_editar_tarefa():
    app.config["TESTING"] = True

    cliente = app.test_client()

    cliente.post(
        "/adicionar",
        data={
            "titulo": "Tarefa original",
            "descricao": "Descrição original",
            "prioridade": "Baixa"
        }
    )

    from app import conectar

    conexao = conectar()
    tarefa = conexao.execute(
        "SELECT id FROM tarefas WHERE titulo = ?",
        ("Tarefa original",)
    ).fetchone()
    conexao.close()

    assert tarefa is not None

    resposta = cliente.post(
        f"/editar/{tarefa['id']}",
        data={
            "titulo": "Tarefa editada",
            "descricao": "Nova descrição",
            "prioridade": "Alta",
            "status": "Em andamento"
        },
        follow_redirects=True
    )

    assert resposta.status_code == 200
    assert b"Tarefa editada" in resposta.data