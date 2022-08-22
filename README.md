# 💻 Sistema de Controle de Despesas

Sistema de Controle de Gastos com uma interface gráfica, onde o usuário poderá inserir, alterar, deletar e gerar na tela um relatório de controle de despesas.

---

## ✔️ Requisitos

Um editor de código como o [VSCode](https://code.visualstudio.com/)

Use o gerenciador de pacotes [pip](https://pip.pypa.io/en/stable/) para instalar o tkcalendar

```bash
pip install tkcalendar
```
ou utilizar o arquivo "requirements.txt" para instalar as dependências
```bash
Babel==2.10.3
pytz==2022.1
tkcalendar==1.6.1

```

---

## ⚙️ Funcionalidades 

Um Sistema de Controle de Gastos simples, onde o usuário poderá adicionar a descrição do tipo de gasto, a data e o valor do mesmo. Também podendo atualizar e deletar uma requerida despesa já incluída. Por fim, no menu superior, denominado "Relatório", poderá gerar um relatório com o gasto total através do intervalo de tempo escolhido.

---

## 🚀 Como executar o projeto

1. Antes de rodar o programa em si, execute o arquivo "banco.bd" para criar uma base de dados onde serão armazenadas as informações

```python
import sqlite3 as lite

# Criando conexão
con = lite.connect('db.db')

# Criando tabela
with con:
    cur = con.cursor()
    cur.execute("CREATE TABLE formulario(id INTEGER PRIMARY KEY AUTOINCREMENT,
                Data DATE NOT NULL, Despesa TEXT NOT NULL, Valor TEXT NOT NULL)")
```

2. Execute o arquivo "main.py" para de fato rodar o programa
3. Uma janela com uma interface gráfica se abrirá, logo, insira, atualize e delete os dados que assim desejar
4. No canto superior esquerdo, tem um menu chamado "Relatório" onde poderá gerar um relatório com o valor total das despesas através do intervalo de tempo escolhido
---
## 🛠 Tecnologias Usadas
* Python
* Sqlite 
* Tkinter
* Tkcalendar

---

## 🧛‍♂️ Autor

[![Twitter Badge](https://img.shields.io/badge/-@paulowilli-1ca0f1?style=flat-square&labelColor=1ca0f1&logo=twitter&logoColor=white&link=https://twitter.com/paulowilli)](https://twitter.com/paulowilli) 

[![Linkedin Badge](https://img.shields.io/badge/-PauloWilliam-blue?style=flat-square&logo=Linkedin&logoColor=white&link=https://www.linkedin.com/in/paulo-william-de-souza-b926101a5/)](https://www.linkedin.com/in/paulo-william-de-souza-b926101a5/) 

[![Gmail Badge](https://img.shields.io/badge/-ziunewill@gmail.com-c14438?style=flat-square&logo=Gmail&logoColor=white&link=mailto:ziunewill@gmail.com)](mailto:ziunewill@gmail.com)

[![Dev.to blog](https://img.shields.io/badge/Myblog-0A0A0A?style=for-the-badge&logo=dev.to&logoColor=white)](https://about-mee.herokuapp.com/blog/)

---

## 📝 Licença

Este projeto está sob a licença [MIT](https://choosealicense.com/licenses/mit/).

Feito por Paulo William
