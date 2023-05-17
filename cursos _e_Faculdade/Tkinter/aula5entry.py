from tkinter import *

janela = Tk()
janela.title("Entry")
janela.geometry("250x250")
janela.config(bg = "black")

label_nome = Label(janela, width=10, height=2, text="nome : ", bg="black", fg="#FFFFFF")
label_nome.grid(row=0, column=0)

entry_nome = Entry(janela, width=15)
entry_nome.grid(row=0, column=1)

label_idade = Label(janela, width=10, height=2, text="idade : ", bg="black", fg="#FFFFFF")
label_idade.grid(row=1, column=0)

entry_idade = Entry(janela, width=15)
entry_idade.grid(row=1, column=1)

label_pais = Label(janela, width=10, height=2, text="pais : ", bg="black", fg="#FFFFFF")
label_pais.grid(row=2, column=0)

entry_pais = Entry(janela, width=15)
entry_pais.grid(row=2, column=1)

button_enviar = Button(janela, width=10, height=0, text="Enviar")
button_enviar.place(x="65", y="120")


janela.mainloop()