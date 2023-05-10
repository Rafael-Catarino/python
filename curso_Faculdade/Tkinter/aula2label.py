from tkinter import *

janela = Tk()
janela.title("Label")
janela.geometry("1200x500")
janela.config(bg = "red")

janela.resizable(width=False,height=True)

label_nome = Label(janela, width=10, height=2, text="nome :", font=("Arial 15 bold"), fg="yellow", bg="black")
label_nome.grid(row=0, column=0, padx=10)

label_pais = Label(janela, width=10, height=2, text="pais :", font=("Arial 15"), fg="green", bg="black")
label_pais.grid(row=1, column=0, padx=10)

label_idade = Label(janela, width=10, height=2, text="idade :", font=("Arial 15 bold"), fg="blue", bg="black")
label_idade.grid(row=2, column=0,padx=10)

janela.mainloop()