from services.db import start_server
from helpers.handleSQL import stringsSQL
import re

db = start_server()

def execute_commit(position, values):
    db.execute(stringsSQL[position], values)
    db.connection.commit()
    
def incluir(values):
    execute_commit(1, values)
    
def alterar(values):
    execute_commit(2, values)

def excluir(id):
    execute_commit(3, id)

def listagem_geral():
    db.execute(stringsSQL[4])
    clientlist = db.fetchall()
    for client in clientlist:
        print(client)
    db.connection.commit()

def listagem_saldo(id):
    execute_commit(5, id)
    print(f"R$: {db.fetchone()[0]}")
    