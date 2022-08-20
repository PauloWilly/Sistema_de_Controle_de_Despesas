import sqlite3 as lite

con = lite.connect('db.db')

# Inserir infrmações
def inserir_info(i):
    with con:
        cur = con.cursor()
        query = "INSERT INTO formulario (data, despesa, valor) VALUES (?, ?, ?)"
        cur.execute(query, i)

# Acessar informações
def monstrar_info():
    lista = []
    with con:
        cur = con.cursor()
        query = "SELECT * FROM formulario"
        cur.execute(query)
        informacao = cur.fetchall()

        for i in informacao:
            lista.append(i)
    return lista

# Atualizar informações
def atualizar_info(i):    
    with con:
        cur = con.cursor()
        query = "UPDATE formulario SET Data=?, Despesa=?, Valor=? WHERE id=?"
        cur.execute(query, i)

# Deletar informações
def deletar_info(i):
    with con:
        cur = con.cursor()
        query = "DELETE FROM formulario WHERE id=?"
        cur.execute(query, i)

def despesas_por_datas(a, b):
    lista = []
    with con:
        cur = con.cursor()
        query = f"SELECT * FROM formulario WHERE Data BETWEEN '{a}' AND '{b}' "
        cur.execute(query)
        informacao = cur.fetchall()

        for i in informacao:
            lista.append(i)
    return lista