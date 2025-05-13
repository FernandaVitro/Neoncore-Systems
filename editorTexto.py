import tkinter as tk


def janela_editor():

    def fechar(): 
        janela.destroy()

    janela = tk.Tk() # criar janela
    janela.title("Neoncore Systems") # nome da janela
    janela.geometry("400x400") # tamanho da janela
    janela.configure(bg="#fff2cc") # cor de fundo

    titulo= tk.Label(janela,text="Editor de texto",bg= "#fff7e1",relief = "solid",width=40, font = ("Georgia",30))
    titulo.pack(pady=5)

    caixa_texto = tk.Text(janela, height=10,bg= "#fff7e1",width=45, font= ("Georgia", 10))
    caixa_texto.pack(pady=10)


    tk.Checkbutton(janela,text="Salvar",bg="#fff7e1" ).pack(pady=5) #caixanha do aceito termo
    btn_fechar = tk.Button(janela, text= "Fechar", relief = "solid",command=fechar, bg= "#fff7e1", width=10,  font= ("Georgia", 20)) # botâo 
    btn_fechar.pack(pady=10, padx ="10")



    janela.mainloop()