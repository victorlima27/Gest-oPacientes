import os
from env.credenciais import SECRET_KEY_cred,SGBD_cred,usuario_cred,senha_cred,servidor_cred,database_cred
from sqlalchemy_utils import database_exists, create_database

SECRET_KEY = SECRET_KEY_cred

SQLALCHEMY_DATABASE_URI = \
    '{SGBD}://{usuario}:{senha}@{servidor}/{database}'.format(
        SGBD = SGBD_cred,
        usuario = usuario_cred,
        senha = senha_cred,
        servidor = servidor_cred,
        database = database_cred
    )

SQLALCHEMY_TRACK_MODIFICATIONS = False

# Verifica se o banco de dados existe; se não, cria-o
if not database_exists(SQLALCHEMY_DATABASE_URI):
    create_database(SQLALCHEMY_DATABASE_URI)
    print("Banco de dados criado com sucesso!")
