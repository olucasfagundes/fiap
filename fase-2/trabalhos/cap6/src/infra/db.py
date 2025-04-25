import psycopg2

def conectar():
    # Ajuste as credenciais conforme seu ambiente PostgreSQL
    conn = psycopg2.connect(
        host="localhost",
        port=5432,
        dbname="sysagro",
        user="postgres",
        password="teste"
    )
    return conn

def fechar_conexao(conn):
    if conn:
        conn.close()
