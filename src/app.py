


from flask import Flask, render_template, request, redirect
from database import criar_tabela, conectar

app = Flask(
    __name__,
    template_folder="templates",
    static_folder="../static"
)

criar_tabela()


@app.route("/")
def inicio():
    conexao = conectar()

    tarefas = conexao.execute(
        "SELECT * FROM tarefas ORDER BY id DESC"
    ).fetchall()

    total = conexao.execute(
        "SELECT COUNT(*) FROM tarefas"
    ).fetchone()[0]

    pendentes = conexao.execute(
        "SELECT COUNT(*) FROM tarefas WHERE status = 'Pendente'"
    ).fetchone()[0]

    andamento = conexao.execute(
        "SELECT COUNT(*) FROM tarefas WHERE status = 'Em andamento'"
    ).fetchone()[0]

    concluidas = conexao.execute(
        "SELECT COUNT(*) FROM tarefas WHERE status = 'Concluída'"
    ).fetchone()[0]

    conexao.close()

    return render_template(
        "index.html",
        tarefas=tarefas,
        total=total,
        pendentes=pendentes,
        andamento=andamento,
        concluidas=concluidas
    )


@app.route("/adicionar", methods=["POST"])
def adicionar():
    titulo = request.form["titulo"]
    descricao = request.form["descricao"]
    prioridade = request.form["prioridade"]

    conexao = conectar()

    conexao.execute(
        """
        INSERT INTO tarefas (titulo, descricao, prioridade)
        VALUES (?, ?, ?)
        """,
        (titulo, descricao, prioridade)
    )

    conexao.commit()
    conexao.close()

    return redirect("/")


@app.route("/excluir/<int:id>", methods=["POST"])
def excluir(id):
    conexao = conectar()

    conexao.execute(
        "DELETE FROM tarefas WHERE id = ?",
        (id,)
    )

    conexao.commit()
    conexao.close()

    return redirect("/")


@app.route("/editar/<int:id>", methods=["GET", "POST"])
def editar(id):
    conexao = conectar()

    if request.method == "POST":
        titulo = request.form["titulo"]
        descricao = request.form["descricao"]
        prioridade = request.form["prioridade"]
        status = request.form["status"]

        conexao.execute(
            """
            UPDATE tarefas
            SET titulo = ?, descricao = ?, prioridade = ?, status = ?
            WHERE id = ?
            """,
            (titulo, descricao, prioridade, status, id)
        )

        conexao.commit()
        conexao.close()

        return redirect("/")

    tarefa = conexao.execute(
        "SELECT * FROM tarefas WHERE id = ?",
        (id,)
    ).fetchone()

    conexao.close()

    if tarefa is None:
        return "Tarefa não encontrada", 404

    return render_template("editar.html", tarefa=tarefa)


if __name__ == "__main__":
    app.run(debug=True)

