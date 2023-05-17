from tkinter import *

janela = Tk()
janela.title("Gird")
janela.geometry("250x250")

label_nome = Label(janela, width=10, height=2, text="Nome :", bg="black", fg="red")
label_nome.grid(row=0, column=0, padx=10, pady=10)

nome = Label(janela, width=10, height=2, text="Rafael", bg="black", fg="red")
nome.grid(row=0, column=1, padx=10, pady=10)

label_idade = Label(janela, width=10, height=2, text="idade :", bg="black", fg="green")
label_idade.grid(row=1, column=0, padx=10, pady=10)

idade = Label(janela, width=10, height=2, text="29", bg="black", fg="green")
idade.grid(row=1, column=1, padx=10, pady=10)

label_pais = Label(janela, width=10, height=2, text="país :", bg="black", fg="blue")
label_pais.grid(row=2, column=0, padx=10, pady=10)

pais = Label(janela, width=10, height=2, text="Brasil", bg="black", fg="blue")
pais.grid(row=2, column=1, padx=10, pady=10)

janela.mainloop()