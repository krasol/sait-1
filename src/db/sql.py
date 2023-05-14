import sqlite3
import re

async def add(item):
    connect = sqlite3.connect("database.db")
    cursor = connect.cursor()
    m = []
    m.append(item)
    cursor.execute('INSERT INTO user (users) VALUES(?)', m)
    connect.commit()
    cursor.close()

async def delete(item):
    sqlite_connection = sqlite3.connect('database.db')
    cursor = sqlite_connection.cursor()

    sql_delete_query = """DELETE from user where id = ?"""
    cursor.execute(sql_delete_query, (item, ))
    sqlite_connection.commit()
    print("Запись успешно удалена")
    cursor.close()

async def buy():
    connect = sqlite3.connect('database.db')
    cursor = connect.cursor()
    query = 'SELECT * FROM user'
    cursor.execute(query)
    data = cursor.fetchall()
    m = []

    for i in data:
        m.append(i)

    l = len(data)
    g = []

    for i in range(l):
        a = re.sub('|\(|\'|\,|\)','',str(m[i]))
        g.append(a)

    c = []
    k = 0
    for i in g:
        k += 1
        q = i + '\n'
        c.append(q)
    v = '\n'.join(c)
    return v
    print(v)
