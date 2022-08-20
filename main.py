import tkinter as tk
from tkinter import CENTER, Button, Frame, Menu, ttk, messagebox, Label, StringVar
from tkcalendar import *
from tkcalendar import DateEntry
from view import *
import locale

# Cores
color0 = "#f0f3f5" # Preta
color1 = "#feffff" # Branca
color2 = "#4fa882" # Verde
color3 = "#38576b" # Valor
color4 = "#403d3d" # Letra
color5 = "#e06636" # - profit
color6 = "#038cfc" # Azul
color7 = "#ef5350" # Vermelha
color8 = "#263238" # Verde
color9 = "e9edf5" # Sky Blue

window = tk.Tk()
window.title("Sistema de Controle de Gastos")
window.geometry('600x400+380+180')
window.resizable(width=False ,height=False)

global tree

# Calendário do campo "Data da despesa", ciclando na alça do mesmo
def data_window():
    window_calendar = tk.Tk()
    window_calendar.title("CALENDÁRIO")
    window_calendar.geometry('300x265+680+220')
    window_calendar.resizable(width=False ,height=False)

    window_calendar.mainloop()

# Mostrar gastos adicionados na treeview principal
def mostrar():

    global tree

    lista = monstrar_info()

    lista_header = ['ID', 'Data', 'Tipo de Despesa', 'Valor da Despesa']

    tree = ttk.Treeview(frame_info, selectmode='extended', columns=lista_header, show='headings')

    # vertical scrollbar
    vsb = ttk.Scrollbar(frame_info, orient='vertical', command=tree.yview)

    # horizontal scrollbar
    hsb = ttk.Scrollbar(frame_info, orient='horizontal', command=tree.xview)

    tree.configure(yscrollcommand=vsb.set, xscrollcommand=hsb.set)

    tree.grid(column=0, row=0, sticky='nsew')
    vsb.grid(column=1, row=0, sticky='ns')
    hsb.grid(column=0, row=1, sticky='ew')

    frame_info.grid_rowconfigure(0, weight=8)

    hd=["nw","nw","nw","nw"]
    h=[30, 120, 100, 140]
    n=0

    for col in lista_header:
        tree.heading(col, text=col.title(), anchor=CENTER)
        # adjust the column's width to the header string
        tree.column(col, width=h[n],anchor=hd[n])    
        n+=1

    for item in lista:
        tree.insert('', 'end', values=item)

# Menu relatório: "Gerar relatório"
def janela_relatorio():
    window_report = tk.Tk()
    window_report.title("Gerar relatório")
    window_report.geometry('600x400+400+200')
    window_report.resizable(width=False ,height=False)

    l_report = Label(window_report, text='Despesas de')
    l_report.grid(row=0, column=0, padx=10, pady=10, sticky='nswe', columnspan=2)

    b_report = DateEntry(window_report, date_pattern="dd/mm/y")
    b_report.grid(row=0, column=2, padx=10, pady=10, sticky='nswe', columnspan=2)
    
    l_report_2 = Label(window_report, text='até')
    l_report_2.grid(row=0, column=4, padx=10, pady=10, sticky='nswe', columnspan=2)

    b_report_2 = DateEntry(window_report, date_pattern="dd/mm/y")
    b_report_2.grid(row=0, column=6, padx=10, pady=10, sticky='nswe', columnspan=2)

    # FRAME para colocar info do relatório
    frame_relatorio = Frame(window_report, borderwidth=1.5, relief='sunken')
    frame_relatorio.place(x=20, y=50, width=415, height=280)

    def mostrar_relatorio():
        primeira_data_relatorio = b_report.get()
        segunda_data_relatorio = b_report_2.get()

        lista = despesas_por_datas(primeira_data_relatorio, segunda_data_relatorio)
        print(lista)

        lista_header = ['ID', 'Data', 'Tipo de Despesa', 'Valor da Despesa']
        tree_relatorio = ttk.Treeview(frame_relatorio, selectmode='extended', columns=lista_header, show='headings')

        # vertical scrollbar
        vsb = ttk.Scrollbar(frame_relatorio, orient='vertical', command=tree_relatorio.yview)

        # horizontal scrollbar
        hsb = ttk.Scrollbar(frame_relatorio, orient='horizontal', command=tree_relatorio.xview)

        tree_relatorio.configure(yscrollcommand=vsb.set, xscrollcommand=hsb.set)

        tree_relatorio.grid(column=0, row=0, sticky='nsew')
        vsb.grid(column=1, row=0, sticky='ns')
        hsb.grid(column=0, row=1, sticky='ew')

        frame_relatorio.grid_rowconfigure(0, weight=8)

        hd=["nw","nw","nw","nw"]
        h=[30, 120, 100, 140]
        n=0

        for col in lista_header:
            tree_relatorio.heading(col, text=col.title(), anchor=CENTER)
            # adjust the column's width to the header string
            tree_relatorio.column(col, width=h[n],anchor=hd[n])    
            n+=1

        for item in lista:
            tree_relatorio.insert('', 'end', values=item)

        # somando gastos que foram filtrados
        lista_valor = [] 
        for valor in lista:
            lista_valor.append(float(valor[3].replace(',','.')))

        locale.setlocale(locale.LC_MONETARY, 'pt_BR.UTF-8')
        soma_valores = locale.currency(sum(lista_valor))

        label_soma = Label(frame_valor_total, text='TOTAL  =')
        label_soma.grid(row=0, column=0, columnspan=2)        
        label_dinamica = StringVar(frame_valor_total, soma_valores)

        label3 = Label(frame_valor_total, textvariable=label_dinamica)        
        label3.grid(row=0, column=2, columnspan=2)

    b_generate_report = Button(window_report, text='Gerar relatório', bg=color6, command=mostrar_relatorio)
    b_generate_report.grid(row=0, column=8, padx=10, pady=10, sticky='nswe', columnspan=2)

    frame_valor_total = Frame(window_report, borderwidth=1.5, relief='sunken')
    frame_valor_total.place(x=20, y=350, width=415, height=30)

    window_report.mainloop()

# Função pra "Inserir", "Atualizar" e "Deletar" infos
def inserir():
    data = reference_date.get()
    despesa = str(type_of_expense.get()).strip()
    valor = str(text_real.get()).strip()

    lista = [data, despesa, valor]

    if data == '':
        messagebox.showerror('Erro', 'Preencha a Data')
    elif despesa == '':
        messagebox.showerror('Erro', 'Preencha o campo "Tipo de Depesa"')
    elif valor == '':
        messagebox.showerror('Erro', 'Preencha o campo "Valor da Despesa"')
    else:
        inserir_info(lista)
        messagebox.showinfo('Sucesso', 'Os dados foram inseridos com sucesso')

        type_of_expense.delete(0, 'end')
        text_real.delete(0, 'end')

    for widget in frame_info.winfo_children():
        widget.destroy()

    mostrar()

def atualizar():
    try:
        treev_dados = tree.focus()
        treev_dicionario = tree.item(treev_dados)
        tree_lista = treev_dicionario['values']

        valor_id = tree_lista[0] # vai pegar o id

        reference_date.delete(0, 'end')
        type_of_expense.delete(0, 'end')
        text_real.delete(0, 'end')

        reference_date.insert(0, tree_lista[1])
        type_of_expense.insert(0, tree_lista[2])
        text_real.insert(0, tree_lista[3])

        def reatualizar():
            data = reference_date.get()
            despesa = str(type_of_expense.get()).strip()
            valor = str(text_real.get()).strip()

            lista = [data, despesa, valor, valor_id]

            if data == '':
                messagebox.showerror('Erro', 'Preencha a Data')
            elif despesa == '':
                messagebox.showerror('Erro', 'Preencha o campo "Tipo de Depesa"')
            elif valor == '':
                messagebox.showerror('Erro', 'Preencha o campo "Valor da Despesa"')
            else:
                atualizar_info(lista)
                messagebox.showinfo('Sucesso', 'Os dados foram atualizados com sucesso')

                type_of_expense.delete(0, 'end')
                text_real.delete(0, 'end')

            for widget in frame_info.winfo_children():
                widget.destroy()

            mostrar()
        
        confirm_button = tk.Button(window, text='Confirmar', bg=color2, command=reatualizar)
        confirm_button.place(x=440, y=250)
    
    except IndexError:
        messagebox.showerror('Erro', 'Selecione um dos dados da tabela')

def deletar():
    try:
        treev_dados = tree.focus()
        treev_dicionario = tree.item(treev_dados)
        tree_lista = treev_dicionario['values']

        valor_id = [tree_lista[0]] # vai pegar o id

        res = messagebox.askokcancel('Deletar?', 'Tem certeza que deseja apagar?')
        if res == True:
            deletar_info(valor_id)
            messagebox.showinfo('Sucesso', 'Dados apagados com sucesso!')
        else:
            pass        

        for widget in frame_info.winfo_children():
            widget.destroy()

        mostrar()

    except IndexError:
        messagebox.showerror('Erro', 'Selecione um dos dados da tabela')

my_menu = Menu(window)
window.config(menu=my_menu)

# Menu item
generate_report = Menu(my_menu, tearoff=0)
my_menu.add_cascade(label='Relatório', menu=generate_report)
generate_report.add_command(label='Gerar', command=janela_relatorio)
generate_report.add_separator()
generate_report.add_command(label='Fechar', command=window.quit)

standard_expense = ['', 'Água', 'Luz', 'Gás', 'Internet', 'Padaria', 'Remédio', 'Combustível', 'Roupa', 'Supermercado', 'Feira', 'Dízimo', 'Médico',
 'Eletrodoméstico', 'Móveis', 'Avon', 'Uber']

label_reference_day = ttk.Label(text = 'Data de Referência: ')
label_reference_day.grid(row=0, column=0, padx=10, pady=10, sticky='nswe', columnspan=2)

label_type_expense = ttk.Label(text="Tipo de Despesa: ")
label_type_expense.grid(row=1, column=0, padx=10, pady=10, sticky='nswe', columnspan=2)

type_of_expense = ttk.Combobox(values=standard_expense)
type_of_expense.grid(row=1, column=2, padx=10, pady=10, sticky='nswe', columnspan=2)

button_voice_expense = ttk.Button(window, text='Voz', command="def voz")
button_voice_expense.grid(row=1, column=4, padx=10, pady=10, sticky='nswe', columnspan=2)

label_expense_amount = ttk.Label(text='Valor da Despesa R$: ')
label_expense_amount.grid(row=2, column=0, padx=10, pady=10, sticky='nswe', columnspan=2)

text_real = ttk.Entry(window)
text_real.grid(row=2, column=2, padx=10, pady=10, sticky='nswe', columnspan=2)

insert_button = tk.Button(window, text='Inserir', bg=color2,command=inserir)
insert_button.grid(row=3, column=0, padx=10, pady=10, sticky='nswe', columnspan=2)

update_button = tk.Button(window, text='Atualizar', bg=color6, command=atualizar)
update_button.grid(row=3, column=2, padx=10, pady=10, sticky='nswe', columnspan=2)

delete_button = tk.Button(window, text='Deletar', bg=color7, command=deletar)
delete_button.grid(row=3, column=4, padx=10, pady=10, sticky='nswe', columnspan=2)

reference_date = DateEntry(window, width=10, postcommand=data_window, date_pattern="dd/mm/y")
reference_date.grid(row=0, column=2, padx=10, pady=10, sticky='nswe', columnspan=2)

# FRAME para colocar info de despesas já adicionadas
frame_info = Frame(window, borderwidth=1.5, relief='sunken')
frame_info.place(x=20, y=180, width=415, height=200)

mostrar()

window.mainloop()