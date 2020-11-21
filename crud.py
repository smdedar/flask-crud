import sqlite3

def create_table():
    conn = sqlite3.connect('database.db')
    conn.execute('CREATE TABLE teachers (id INTEGER PRIMARY KEY AUTOINCREMENT,name TEXT, addr TEXT, city TEXT, pin TEXT)')
    conn.close()



def view_data():
    connection = sqlite3.connect('database.db')
    cursor = connection.cursor()
    try:
        sql = 'SELECT * from teachers'
        cursor.execute(sql)
        data = cursor.fetchall()
        connection.commit
    except:
        data = "null"
    return data



def delete_data(id):
    connection = sqlite3.connect('database.db')
    cursor = connection.cursor()
    try:
        sql = 'DELETE FROM teachers WHERE id=?'
        cursor.execute(sql,(id,))
        connection.commit()
        mcg = "Delete Successfully"
    except:
        mcg = "Delete Failed"
    return mcg



def edit_data(id):
    connection = sqlite3.connect('database.db')
    cursor = connection.cursor()
    try:
        sql = 'SELECT * FROM teachers WHERE id=?'
        cursor.execute(sql,(id,))
        data = cursor.fetchone()
        connection.commit()
    except:
        data = "None"
    return data




def update_data(task):
    connection = sqlite3.connect('database.db')
    cursor = connection.cursor()
    try:
        sql = 'UPDATE teachers SET name = ?, addr = ?, city = ?, pin = ?  WHERE id = ?'
        cursor.execute(sql,task)
        connection.commit()
        mcg = "Update Successfully"
    except:
        mcg = "Update Failed"
    return mcg



def add_data(data):
    connection = sqlite3.connect('database.db')
    cursor = connection.cursor()
    try:
        sql = 'INSERT INTO teachers (name,addr,city,pin) VALUES (?,?,?,?)'
        cursor.execute(sql,data)
        connection.commit()
        mcg = "Add Successfully"
    except:
        mcg = "Insert Failed"
    return mcg