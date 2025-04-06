from funcoes import *

#Utilizando o SimpleSQLiteBrowser para visualizar o banco de dados;

controle_menu = True

while controle_menu:
    opcao = input("Selecione uma opção \n1 - Cadastro\n2 - Login\n3 - Pesquisa no BD\n4 - Encerrar programa\n")

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

    elif opcao == '2':
        email = loop_email()
        senha = gerador_de_hash(input("Insira sua senha: "))
        verifica_cadastro_BD(email,senha)

    elif opcao == '3':
        email = loop_email()
        retorna_hash_com_email(email)

    elif opcao == '4':
        print('Encerrando programa...')
        controle_menu = False

    else:
        print("Opção inválida.")








# See PyCharm help at https://www.jetbrains.com/help/pycharm/
