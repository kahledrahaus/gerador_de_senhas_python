#!/usr/bin/python3
import random
import string
import customtkinter as ctk
import pyperclip

# criar a janela principal
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("dark-blue")

janela = ctk.CTk()
janela.title("Gerador de senhas")
janela.geometry("330x210")

# função para gerar a senha aleatória
def gerar_senha():
    # escolher caracteres a partir dos quais a senha será gerada
    caracteres = string.ascii_letters + string.digits + string.punctuation

    # gerar senha aleatória
    senha = ''.join(random.choice(caracteres) for i in range(12))

    # limpando a label copiado
    label_copiar.configure(text="")

    return senha

# função para exibir a senha gerada na tela
def exibir_senha():
    senha = gerar_senha()
    output_box.set(senha)

# função para copiar a senha para a área de transferência
def copiar_senha():
    senha = output_box.get()
    pyperclip.copy(senha)
    label_copiar.configure(text="Copiado!")

# texto de tela
texto = ctk.CTkLabel(janela, text="Bem vindo!")
texto.pack(padx=10)

# criar um botão para gerar a senha
gerar_botao = ctk.CTkButton(janela, text='Gerar senha', command=exibir_senha)
gerar_botao.pack(padx=10, pady=10)

# criar uma caixa de saída para exibir a senha gerada
output_box = ctk.StringVar()
output_label = ctk.CTkLabel(janela, textvariable=output_box)
output_label.pack(padx=10, pady=10)

# criar um botão para copiar a senha
copiar_botao = ctk.CTkButton(janela, text='Copiar senha', command=copiar_senha)
copiar_botao.pack(padx=10, pady=10)
label_copiar = ctk.CTkLabel(master=janela, text="")
label_copiar.pack()

# iniciar o loop de eventos da interface gráfica
janela.mainloop()
