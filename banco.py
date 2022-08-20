import sqlite3 as lite

# Criando conexão
con = lite.connect('db.db')

# Criando tabela
with con:
    cur = con.cursor()
    cur.execute("CREATE TABLE formulario(id INTEGER PRIMARY KEY AUTOINCREMENT, Data DATE NOT NULL, Despesa TEXT NOT NULL, Valor TEXT NOT NULL)")