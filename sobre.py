import tkinter as tk

def janela_sobre():

    def fechar(): #clicar para fechar
        janela.destroy()

    janela = tk.Tk() # criar janela
    janela.title("Neoncore Systems") # nome da janela
    janela.geometry("700x400") # tamanho da janela
    janela.configure(bg="#fff2cc") # cor de fundo

    titulo= tk.Label(janela,text="Sobre o Sistema",bg= "#fff7e1",relief = "solid",width=40, font = ("Georgia",16))
    titulo.pack(pady=5)

    texto = tk.Label(janela,text=("Este sistema foi desenvolvido pela Neoncore Systems com o objetivo de simular uma plataforma multifuncional"
            "voltada para fins educacionais e de treinamento.\n\n"
            "A proposta é tornar os computadores mais fáceis de usar e seguros para todos, por meio de uma interface gráfica "
            "simples e eficiente, combinada com recursos que reforçam a usabilidade e a segurança.\n\n"
            "Principais funcionalidades:\n"
            "- Cadastro e Login: Criação de contas com nome de usuário e senha, protegidas por criptografia.\n"
            "- Editor de Texto: Ferramenta semelhante a um bloco de notas.\n"
            "- Comunicação Simulada: Envio e recebimento de mensagens entre usuários.\n"
            "- Recursos de Segurança: Criptografia e antivírus integrados.\n\n"
            "Versão: 1.0\n"
            "Desenvolvimento: Equipe Neoncore Systems"),bg="#fff2cc",font=("Georgia", 10),justify="left", anchor="w")
    texto.pack(padx=20, pady=10)

    #justify="left"= Alinha o texto para a esquerda dentro da label
    # anchor="w"  =  Gruda o texto no lado esquerdo da label
    # wraplength=360= Largura máxima antes de quebrar a linha


    #botão fechar
    btn_fechar = tk.Button(janela, text= "Fechar", relief = "solid",command=fechar, bg= "#fff7e1", width=10,  font= ("Georgia", 20)) # botâo 
    btn_fechar.pack(pady=10, padx ="10")

    janela.mainloop()