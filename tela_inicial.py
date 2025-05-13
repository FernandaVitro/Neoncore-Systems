import tkinter as tk
import cadastro
import editorTexto
import comunicacao
import sobre

def abrir_cadastro():
    cadastro.janela_cadastro()

def abrir_editor():
    editorTexto.janela_editor()

def abrir_comunicacao():
    comunicacao.janela_comunicacao()

def abrir_sobre():
    sobre.janela_sobre()


janela = tk.Tk() # criar janela
janela.title("Neoncore Systems") # nome da janela
janela.geometry("400x400") # tamanho da janela
janela.configure(bg="#fff2cc") # cor de fundo

titulo= tk.Label(janela,text="Tela Inicial",bg= "#fff7e1",relief = "solid",width=40, font = ("Georgia",30))
titulo.pack(pady=5)

btn_cadastro = tk.Button(janela, text= "Login", command=abrir_cadastro, relief = "solid",bg= "#fff7e1", width=10,  font= ("Georgia", 20)) # botâo 
btn_cadastro.pack(pady=10, padx ="10")

btn_editorTexto = tk.Button(janela, text= "Editor de Texto", command = abrir_editor, relief = "solid",bg= "#fff7e1", width=15,  font= ("Georgia", 20)) # botâo 
btn_editorTexto.pack(pady=10, padx ="10")

btn_comunicacao = tk.Button(janela, text= "Chat", command = abrir_comunicacao, relief = "solid",bg= "#fff7e1", width=15,  font= ("Georgia", 20)) # botâo 
btn_comunicacao.pack(pady=10, padx ="10")

btn_sobre = tk.Button(janela, text= "Sobre o Sistema", command = abrir_sobre, relief = "solid",bg= "#fff7e1", width=15,  font= ("Georgia", 20)) # botâo 
btn_sobre.pack(pady=10, padx ="10")

janela.mainloop()