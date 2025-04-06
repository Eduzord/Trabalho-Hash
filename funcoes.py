import re
import sqlite3
import hashlib



def valida_senha(senha):
    regex = r'^(?=.*[A-Z])(?=.*[\W_])(?=.{8,}).*$'
    return bool(re.match(regex, senha))


def loop_email():
    controle_cadastro_email = True
    while controle_cadastro_email:
        email = input("Insira seu email:\n")
        if valida_email(email):
            controle_cadastro_email = False  # Se o email possuir "@", sai do loop
            return email
        else:
            print("Email inválido.\n")
def valida_email(email):
    if email.find("@") == -1:
        return False
    else:
        return True

def gerador_de_hash(senha):
    senha_bytes = senha.encode('utf-8')

    hash_sha1 = hashlib.sha1(senha_bytes)

    return hash_sha1.hexdigest()

def cadastra_usuario_BD(email,senha):
    conexao = sqlite3.connect('banco_de_usuarios.db')
    cursor = conexao.cursor()
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS usuarios (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        email TEXT NOT NULL,
        senha TEXT UNIQUE NOT NULL
    )
    ''')
    conexao.commit()

    try:
        # Inserção segura com placeholders
        cursor.execute("INSERT INTO usuarios (email, senha) VALUES (?, ?)", (email, senha))
        conexao.commit()
        print("Usuário cadastrado com sucesso!\n")
    except sqlite3.IntegrityError as e:
        print("Erro ao cadastrar usuário\n", e)
    conexao.close()

def verifica_cadastro_BD(email,senha):
    conexao = sqlite3.connect('banco_de_usuarios.db')
    cursor = conexao.cursor()

    # Consulta SQL para verificar se existe uma linha com esse email e senha
    cursor.execute("SELECT senha FROM usuarios WHERE email = ?", (email,))
    resultado = cursor.fetchone()

    if resultado is None:
        print("E-mail inexistente.\n")
    else:
        senha_hash_banco = resultado[0]

        if senha_hash_banco == senha:
            print("Senha correta.\n")
        else:
            print("Senha incorreta.\n")

    # Fecha a conexão
    conexao.close()

def retorna_hash_com_email(email):
    conexao = sqlite3.connect('banco_de_usuarios.db')
    cursor = conexao.cursor()

    # Consulta SQL para verificar se existe uma linha com esse email e senha
    cursor.execute("SELECT senha FROM usuarios WHERE email = ?", (email,))
    resultado = cursor.fetchone()
    if resultado == None:
        print("Email inexistente.\n")
    else:
        print(f"O Hash é {resultado[0]} ")
