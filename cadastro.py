import tkinter as tk

def janela_cadastro():
    def fechar(): #clicar para fechar
        janela.destroy()

    janela = tk.Tk() # criar janela
    janela.title("Neoncore Systems") # nome da janela
    janela.geometry("400x400") # tamanho da janela
    janela.configure(bg="#fff2cc") # cor de fundo

    titulo= tk.Label(janela,text="Cadastro",bg= "#fff7e1",relief = "solid",width=40, font = ("Georgia",30))
    titulo.pack(pady=5)

    Tlogin= tk.Label(janela,text="Usuario ",relief = "solid",bg= "#fff7e1",width=20, font = ("Georgia",14))
    Tlogin.pack(pady=10)
    Login= tk.Entry (janela,width = 20,relief = "solid", font = ("Georgia", 14))
    Login.pack(pady= 10)

    Tsenha= tk.Label(janela,text="Senha",relief = "solid",bg= "#fff7e1",width=20, font = ("Georgia",14))
    Tsenha.pack(pady=10)
    senha= tk.Entry (janela,width = 20,relief = "solid", font = ("Georgia", 14))
    senha.pack(pady= 10)

    tk.Checkbutton(janela,text="Ativar antivirus",bg="#fff7e1" ).pack(pady=5) #caixanha do "aceito termo"

    btn_proximo = tk.Button(janela, text= "Proximo", relief = "solid",command=fechar, bg= "#fff7e1", width=10,  font= ("Georgia", 20)) # botâo 
    btn_proximo.pack(pady=10, padx ="10")



    janela.mainloop()