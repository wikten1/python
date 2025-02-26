import pymysql.cursors

con = pymysql.connect(
    host="localhost",
    user="root",
    passwd="",
    port=3306,
    db="aulapythonfull",
    charset="utf8mb4",
    cursorclass=pymysql.cursors.DictCursor
)

def criaTabela(nomeTabela):
    try:
        with con.cursor() as cursor:
            cursor.execute(f"create table {nomeTabela} (nome varchar(50))")
        print("tabela criada com sucesso")
    except Exception as e:
        print(f'Ocorreu um erro {e}')

def removeTabela(nomeTabela):
    try:
        with con.cursor() as cursor:
            cursor.execute(f"drop table {nomeTabela}")
        print("tabela removida com sucesso")
    except Exception as e:
        print(f'Ocorreu um erro {e}')

def insereTabela(nome):
    try:
        with con.cursor() as cursor:
            cursor.execute(f"insert into teste values('{nome}')")
        con.commit()
        print("Valor inserido com sucesso")
    except Exception as e:
        print(f'Ocorreu um erro {e}')

def selectTabela():
    try:
        with con.cursor() as cursor:
            cursor.execute("SELECT * FROM teste")
            resultado = cursor.fetchall()
            for i in resultado:
                print(i)
    except Exception as e:
        print(f'Ocorreu um erro {e}')

def updateTabela():
    try:
        with con.cursor() as cursor:
            cursor.execute("UPDATE teste SET nome = 'joana' WHERE nome = 'Joana'")
        con.commit()
        print("tabela atualizada com sucesso")
    except Exception as e:
        print(f'Ocorreu um erro {e}')

def deleteTabela():
    try:
        with con.cursor() as cursor:
            cursor.execute("DELETE FROM teste WHERE nome = 'joana'")
        con.commit
        print("Remoção efetuada com sucesso")
    except Exception as e:
        print(f'Ocorreu um erro {e}')



deleteTabela()
con.close()