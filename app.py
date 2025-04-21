from flask import Flask, render_template, request
import sqlite3
import os

app = Flask(__name__)

# Cria o banco se não existir
def criar_banco():
    if not os.path.exists("duvidas.db"):
        conn = sqlite3.connect("duvidas.db")
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS duvidas (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                mensagem TEXT NOT NULL
            )
        ''')
        conn.commit()
        conn.close()

criar_banco()

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        mensagem = request.form['mensagem']
        if mensagem.strip():
            conn = sqlite3.connect('duvidas.db')
            cursor = conn.cursor()
            cursor.execute("INSERT INTO duvidas (mensagem) VALUES (?)", (mensagem,))
            conn.commit()
            conn.close()
            return render_template('sucesso.html')
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
