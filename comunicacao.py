import tkinter as tk

def janela_comunicacao():

    janela = tk.Tk() #criar janela
    janela.title("Neoncore Systems")
    janela.geometry("400x500")
    janela.configure(bg="#fff2cc")

    titulo = tk.Label(janela, text="Comunicação Simulada", bg="#fff7e1",relief="solid", width=40, font=("Georgia", 12))
    titulo.pack(pady=5)

    #listas para armazenar mensagens
    mensagens_usuario1 = []
    mensagens_usuario2 = []

    #função para enviar mensagem do usuário 1
    def enviar_usuario1():
        msg = entrada1.get()
        if msg:
            mensagens_usuario2.append("Usuário 1: " + msg)
            caixa_texto.insert(tk.END, "Usuário 1: " + msg + "\n" ) # \n é quebrar linha
            entrada1.delete(0, tk.END)

    #função para enviar mensagem do usuário 2
    def enviar_usuario2():
        msg = entrada2.get()
        if msg:
            mensagens_usuario1.append("Usuário 2: " + msg)
            caixa_texto.insert(tk.END, "Usuário 2: " + msg + "\n") # \n é quebrar linha
            entrada2.delete(0, tk.END)

    # botão fechar
    def fechar(): 
        janela.destroy()


    # Campo e botão para Usuário 1

    titulo1= tk.Label(janela,text="Usuario 1",bg= "#faebc0",relief = "solid",width=10, font = ("Georgia",10))
    titulo1.pack(pady=5)

    entrada1 = tk.Entry(janela,relief = "solid",bg= "#fff7e1",width=30, font = ("Georgia",14))
    entrada1.pack(pady=5)

    botao1 = tk.Button(janela, text="Enviar", relief = "solid",command=enviar_usuario1, bg= "#fff7e1", width=20,  font= ("Georgia", 10))
    botao1.pack()

    #campo e botão para Usuário 2

    titulo1= tk.Label(janela,text="Usuario 2",bg= "#faebc0",relief = "solid",width=10, font = ("Georgia",10))
    titulo1.pack(pady=5)

    entrada2 = tk.Entry(janela,relief = "solid",bg= "#fff7e1",width=30, font = ("Georgia",14))
    entrada2.pack(pady=5)

    botao2 = tk.Button(janela, text="Enviar",command=enviar_usuario2, relief = "solid", bg= "#fff7e1", width=20,  font= ("Georgia", 10))
    botao2.pack()

    # Área de texto para mostrar a conversa
    caixa_texto = tk.Text(janela, height=10,relief = "solid", bg= "#fff7e1",width=45, font= ("Georgia", 10))
    caixa_texto.pack(pady=10)

    #botão fechar
    btn_fechar = tk.Button(janela, text= "Fechar", relief = "solid",command=fechar, bg= "#faebc0", width=10,  font= ("Georgia", 20)) # botâo 
    btn_fechar.pack(pady=10, padx ="10")

    janela.mainloop()
