import sqlite3
from tkinter import *
from tkinter import messagebox

# Função para criar a tabela de hospedes no banco de dados
def criar_tabela():
    conn = sqlite3.connect("sistema_reservas.db")
    cursor = conn.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS hospedes (nome TEXT, idade INTEGER, email TEXT, documento TEXT, dia TEXT, hora TEXT)")
    conn.commit()
    conn.close()

# Função para adicionar um hospede ao banco de dados
def adicionar_hospede():
    conn = sqlite3.connect("sistema_reservas.db")
    cursor = conn.cursor()
    cursor.execute("SELECT COUNT(*) FROM hospedes")
    total_hospedes = cursor.fetchone()[0]
    
    if total_hospedes >= 50:
        messagebox.showinfo("Limite de Hospedes", "Não é possível hospedar mais pessoas. Limite máximo atingido.")
        return
    
    nome = entry_nome.get()
    idade = entry_idade.get()
    email = entry_email.get()
    documento = entry_documento.get()
    dia = entry_dia.get()
    hora = entry_hora.get()
    
    cursor.execute("INSERT INTO hospedes VALUES (?, ?, ?, ?, ?, ?)", (nome, idade, email, documento, dia, hora))
    conn.commit()
    conn.close()
    
    messagebox.showinfo("Reserva Concluída", "Reserva realizada com sucesso!")
    
    # Limpar os campos após a reserva
    entry_nome.delete(0, END)
    entry_idade.delete(0, END)
    entry_email.delete(0, END)
    entry_documento.delete(0, END)
    entry_dia.delete(0, END)
    entry_hora.delete(0, END)

# Função para listar todos os hospedes hospedados
def listar_hospedes():
    conn = sqlite3.connect("sistema_reservas.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM hospedes")
    hospedes = cursor.fetchall()
    conn.close()
    
    for hospede in hospedes:
        print(f"Nome: {hospede[0]}, Idade: {hospede[1]}, Email: {hospede[2]}, Documento: {hospede[3]}, Dia: {hospede[4]}, Hora: {hospede[5]}")

# Criar a tabela no banco de dados
criar_tabela()

# Interface gráfica utilizando Tkinter
window = Tk()
window.title("Sistema de Reservas de Hotel")
window.geometry("400x300")

label_boas_vindas = Label(window, text="Bem-vindo ao Sistema de Reservas do Douglas!", font=("Arial Bold", 12))
label_boas_vindas.pack()

label_nome = Label(window, text="Nome:")
label_nome.pack()
entry_nome = Entry(window)
entry_nome.pack()

label_idade = Label(window, text="Idade:")
label_idade.pack()
entry_idade = Entry(window)
entry_idade.pack()

label_email = Label(window, text="Email:")
label_email.pack()
entry_email = Entry(window)
entry_email.pack()

label_documento = Label(window, text="Documento:")
label_documento.pack()
entry_documento = Entry(window)
entry_documento.pack()

label_dia = Label(window, text="Dia da Reserva:")
label_dia.pack()
entry_dia = Entry(window)
entry_dia.pack()

label_hora = Label(window, text="Hora da Reserva:")
label_hora.pack()
entry_hora = Entry(window)
entry_hora.pack()

button_reservar = Button(window, text="Reservar", command=adicionar_hospede)
button_reservar.pack()

button_listar = Button(window, text="Listar Hospedes", command=listar_hospedes)
button_listar.pack()

label_rodape = Label(window, text="Obrigado pela visita e agradecemos a preferência!", font=("Arial Bold", 12))
label_rodape.pack()

window.mainloop()
