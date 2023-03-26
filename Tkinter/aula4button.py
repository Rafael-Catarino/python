from tkinter import *

janela = Tk()
janela.title("Botão")
janela.geometry("500x250")

global contador

contador = 0

def executar():

    global contador

    texto_1 = "numero impar"
    texto_2 = "numero par"

    if (contador%2) == 0 :
        label_nome["text"] = texto_2
        label_nome["bg"] = "green"
    else:
        label_nome["text"] = texto_1
        label_nome["bg"] = "blue"

    contador += 1

label_nome = Label(janela, width=20, height=2, text="nome : ", relief="flat", fg="white", bg="black")
label_nome.grid(row=0, column=0, padx=10, pady=10)

# Estilos do button - sunken, ridge, flat(padrão), groove, solid, raised, 
botao = Button(janela, command=executar, width=10, height=0, text= "Enviar", relief="sunken", fg="yellow", bg="black")
botao.grid(row=0, column=1, padx=10, pady=10)

janela.mainloop()