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
            print("Email inválido.")
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
    conexao = sqlite3.connect('banco_de_usuarios.bd')
    cursor = conexao.cursor()
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS usuarios (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        email TEXT NOT NULL,
        senha TEXT UNIQUE NOT NULL
    )
    ''')
    conexao.commit()

    cursor.execute(f"INSERT INTO usuarios (email, senha) VALUES ({email}, {senha})", ("Maria", "maria@email.com"))
    conexao.commit()
    conexao.close()