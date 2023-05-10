from tkinter import *

janela = Tk()
janela.title("Pack")
janela.geometry("250x250")

label_nome = Label(janela, width=10, height=2, text="Nome :", bg="black", fg="red")
label_nome.pack()

nome = Label(janela, width=10, height=2, text="Rafael", bg="black", fg="red")
nome.pack()

label_idade = Label(janela, width=10, height=2, text="idade :", bg="black", fg="green")
label_idade.pack()

idade = Label(janela, width=10, height=2, text="29", bg="black", fg="green")
idade.pack()

label_pais = Label(janela, width=10, height=2, text="país :", bg="black", fg="blue")
label_pais.pack()

pais = Label(janela, width=10, height=2, text="Brasil", bg="black", fg="blue")
pais.pack()


janela.mainloop()