""" Utilizando a biblioteca gráfica Tkinter, o aluno deve construir uma interface que simule uma tela de login de usuário contendo o campo de login, senha e um botão de autenticação."""

from tkinter import *


class Application(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.titulo = Label(self, text="Preencha os campos:")
        self.titulo.grid(column=1, columnspan=2, row=0)
        self.msg = Label(self, text="Login:*")
        self.msg.grid(column=1, row=1)
        self.entrada = Entry(self, bd=3, font=(
            "Arial", 13), width=25, justify=(CENTER))
        self.entrada.grid(column=2, row=1)
        self.msg = Label(self, text="Senha:*", anchor=W)
        self.msg.grid(column=1, row=2)
        self.entrada = Entry(self, bd=3, font=(
            "Arial", 13), width=25, justify=(CENTER))
        self.entrada.grid(column=2, row=2)
        self.enviar = Button(self, text="ENVIAR", command=quit)
        self.enviar.grid(column=1, columnspan=2, row=3)
        self.grid()


app = Application()
mainloop()
