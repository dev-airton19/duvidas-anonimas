from flask import Flask, render_template, request, redirect
import sqlite3

app = Flask(__name__)

def salvar_mensagem(mensagem):
    conn = sqlite3.connect("duvidas.db")
    cursor = conn.cursor()
    cursor.execute("INSERT INTO mensagens (mensagem) VALUES (?)", (mensagem,))
    conn.commit()
    conn.close()

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        mensagem = request.form["mensagem"]
        salvar_mensagem(mensagem)
        return render_template("index.html", mensagem_sucesso="Sua dúvida foi enviada com sucesso!")
    return render_template("index.html", mensagem_sucesso=None)

if __name__ == "__main__":
    app.run(debug=True)
