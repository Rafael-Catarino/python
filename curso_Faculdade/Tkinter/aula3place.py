from tkinter import *

janela = Tk()
janela.title("Place")
janela.geometry("250x250")

label_nome = Label(janela, width=10, height=2, text="Nome :", bg="black", fg="red")
label_nome.place(x=10, y=10)
nome = Label(janela, width=10, height=2, text="Rafael", bg="black", fg="red")
nome.place(x=100, y=10)

label_idade = Label(janela, width=10, height=2, text="idade :", bg="black", fg="green")
label_idade.place(x=10, y=60)
idade = Label(janela, width=10, height=2, text="29", bg="black", fg="green")
idade.place(x=100, y=60)

label_pais = Label(janela, width=10, height=2, text="país :", bg="black", fg="blue")
label_pais.place(x=10, y=110)
pais = Label(janela, width=10, height=2, text="Brasil", bg="black", fg="blue")
pais.place(x=100, y=110)

janela.mainloop()