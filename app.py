from flask import Flask, render_template, request, redirect
import sqlite3

app = Flask(__name__)

# Criação do banco de dados se não existir
def init_db():
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS duvidas (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            texto TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

init_db()

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        duvida = request.form['duvida']
        if duvida.strip():
            conn = sqlite3.connect('database.db')
            cursor = conn.cursor()
            cursor.execute('INSERT INTO duvidas (texto) VALUES (?)', (duvida,))
            conn.commit()
            conn.close()
        return redirect('/')
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
