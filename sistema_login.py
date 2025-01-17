# Começar instalando o pip install customtkinter
import customtkinter as ctk 

# Configuração aparência - aqui colocamos em modo dark, mas pode ser
#light
#system
#dark
ctk.set_appearance_mode('dark')


# Criação das funções de funcionalidades
# Função para validar o login do User
def validar_login():
    usuario = input_usuario.get()  # Armazenar o usuario
    senha = input_senha.get()   # Armazenar a senha

    if usuario == 'Eduardo' and senha == '12345':
        validacao_login.configure(text='Login correto!', text_color="green")
    else:
        validacao_login.configure(text='Login incorreto!', text_color='red')



# Criação da janela princial
menu = ctk.CTk()  #inicializar o sistema
menu.title('Sistema de Login')  #colocar um titulo na interface
menu.geometry('300x300')  #definir uma tamanho em px para a interface



# Criação dos campos
# Label - Campo para adcionar um texto na aplicação
texto_usuario = ctk.CTkLabel(menu, text='Usuário') 
# Posicionamento do texto
texto_usuario.pack(pady=10)  

# Entry - input usuario
input_usuario = ctk.CTkEntry(menu, placeholder_text='Digite o seu usuário') #placeholder_text - para colocar texto dentro do input
input_usuario.pack()

# Label - Texto senha
texto_senha = ctk.CTkLabel(menu, text=('Senha'))
texto_senha.pack(pady=10)

# Entrey - input senha
input_senha = ctk.CTkEntry(menu, placeholder_text=('Digite sua senha'), show='*') #show é para aparecer * no lugar da senha
input_senha.pack()

# Button - botão
botao = ctk.CTkButton(menu, text='Login', command=validar_login)
botao.pack(pady=20)

#Label - texto de confirmação de login
validacao_login = ctk.CTkLabel(menu, text="")
validacao_login.pack(pady=10)


# Inicial a aplicação
menu.mainloop()