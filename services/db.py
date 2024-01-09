import sqlite3

class DB:
    def __init__(self):
        self.connection = None
        self.cursor = None

    def connect(self):
        self.connection = sqlite3.connect("Cadastro.db")
        self.cursor = self.connection.cursor()
        return self.cursor

def start_server():
    db = DB()
    return db.connect()


      