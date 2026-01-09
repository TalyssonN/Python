import sqlite3
from pathlib import Path

ROOT_PATH = Path(__file__).parent

# Função para criar conexão com o banco de dados SQLite
# PATH usado para criar o db no diretório atual do script


def create_connection(db_file):
    """Criando conexão com DB SQLite"""
    conn = None
    try:
        conn = sqlite3.connect(ROOT_PATH / db_file)
        print("Conexão estabelecida com sucesso.")
    except sqlite3.Error as e:
        print(f"Erro ao conectar ao banco de dados: {e}")
    return conn

create_connection("CLIENTES.db")

# Função para criar uma tabela no banco de dados
def create_table(conn):
    """Criando tabela no DB SQLite"""
    try:
        sql_create_table = """
        CREATE TABLE clientes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            idade INTEGER,
            email TEXT UNIQUE
        );
        """
        cursor = conn.cursor()
        cursor.execute(sql_create_table)
        print("Tabela criada com sucesso.")
    except sqlite3.Error as e:
        print(f"Erro ao criar tabela: {e}")

create_table(create_connection("CLIENTES.db"))

def insert_client(conn, client):
    """Inserindo um novo cliente na tabela"""
    try:
        sql_insert_client = """
        INSERT INTO clientes (nome, idade, email)
        VALUES (?, ?, ?);
        """
        cursor = conn.cursor()
        cursor.execute(sql_insert_client, client)
        conn.commit()
        print("Cliente inserido com sucesso.")
        
    except sqlite3.Error as e:
        print(f"Erro ao inserir cliente: {e}")
    conn.close()

insert_client(create_connection("CLIENTES.db"), ("João Silva", 30, "joao.silva@example.com"))

# def inserir_muitos_clientes(conn, dados):
#     cursor = conn.cursor()
#     sql_insert_multi = """
#         INSERT INTO clientes (nome, idade, email)
#         VALUES (?, ?, ?);
#     """
#     cursor.executemany(sql_insert_multi, dados)
#     conn.commit()
#     print("Muitos clientes inseridos com sucesso.")
#     conn.close()

# dados = [
#         ("Maria Oliveira", 25, "maria.oliveira@example.com"),
#         ("Carlos Souza", 28, "carlos.souza@example.com"),
#         ("Lucas Pereira", 35, "lucas.pereira@example.com")
# ]
# inserir_muitos_clientes(create_connection("CLIENTES.db"), dados)

def pesquisar(conn, id):
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM clientes WHERE id=?", (id,))
    return cursor.fetchone()

cliente = pesquisar(create_connection("CLIENTES.db"), 1)
print(cliente)