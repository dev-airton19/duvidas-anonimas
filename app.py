from flask import Flask, render_template, request, redirect, flash, url_for
import sqlite3

app = Flask(__name__)
app.secret_key = 'segredo123'

def criar_tabela():
    conn = sqlite3.connect('duvidas.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS duvidas (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            mensagem TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

criar_tabela()

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        mensagem = request.form['mensagem']
        conn = sqlite3.connect('duvidas.db')
        cursor = conn.cursor()
        cursor.execute('INSERT INTO duvidas (mensagem) VALUES (?)', (mensagem,))
        conn.commit()
        conn.close()
        flash('Dúvida enviada com sucesso!')
        return redirect(url_for('index'))
    return render_template('index.html')

@app.route('/ver')
def ver_duvidas():
    conn = sqlite3.connect('duvidas.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM duvidas')
    dados = cursor.fetchall()
    conn.close()
    return '<br>'.join([f"{linha[0]} - {linha[1]}" for linha in dados])

if __name__ == '__main__':
    app.run(debug=True)
