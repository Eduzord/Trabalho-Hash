from funcoes import *


controle_menu = True

while controle_menu:
    opcao = input("Selecione uma opção \n1 - Cadastro\n2 - Login\n3 - Pesquisa no BD")

    if opcao == '1':

        email = loop_email() #Faz a validação de email
        controle_cadastro_senha = True
        while controle_cadastro_senha:
            senha = input("Insira sua senha\n(Ao menos 8 caracteres, 1 caractere maiúsculo e um caractere especial:\n")
            if valida_senha(senha):
                senha = gerador_de_hash(senha)  # Cria um hash a partir da senha inserida
                controle_cadastro_senha = False #Se a senha corresponder a todos os requisitos, sai do loop.
            else:
                print("Sua senha não atende os requisitos. Tente novamente.")

        cadastra_usuario_BD(email,senha)

    if opcao == '2':
        controle_opcao_validacao = True
        email = loop_email()
        senha = input("Insira sua senha: ")
        senha = gerador_de_hash(senha)









# See PyCharm help at https://www.jetbrains.com/help/pycharm/
