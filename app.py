from flask import Flask, render_template, request
import sqlite3
import os
from datetime import datetime

app = Flask(__name__)

# Cria e salva no banco com data e hora
def salvar_duvida(mensagem):
    criar_banco = not os.path.exists("duvidas.db")
    conn = sqlite3.connect("duvidas.db")
    cursor = conn.cursor()
    
    if criar_banco:
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS duvidas (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                mensagem TEXT NOT NULL,
                data_envio TEXT
            )
        ''')

    data_envio = datetime.now().strftime('%d/%m/%Y %H:%M:%S')
    cursor.execute("INSERT INTO duvidas (mensagem, data_envio) VALUES (?, ?)", (mensagem, data_envio))
    conn.commit()
    conn.close()

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        mensagem = request.form['mensagem']
        if mensagem.strip():
            salvar_duvida(mensagem)
            return render_template('sucesso.html')
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
