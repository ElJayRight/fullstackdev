import sqlite3
import os


def is_in_db(method, language=None):
    conn = sqlite3.connect('data.db')
    cursor = conn.cursor()
   
    if language:
        cursor.execute("select * from methods where method_name = ? and language = ?", (method,language))
    else:
        cursor.execute("select * from methods where method_name = ?", (method, ))

    result = cursor.fetchone()
    cursor.close()
    if result:
        return True
    else:
        return False

def add_record(method, language, data):
    conn = sqlite3.connect('data.db')
    if is_in_db(method, language):
        return False
    code_file = f'{method}/{language}.{language}'
    cursor = conn.cursor()
    cursor.execute('''INSERT INTO methods (method_name, language, file_name)
                   VALUES (?, ?, ?)''', (method, language, code_file))
    conn.commit()
    cursor.close()

    if not os.path.exists(method):
        os.makedirs(method)

    with open(code_file,'w') as file:
        file.write(data)
    return True

def get_data(method=None, language=None):
    conn = sqlite3.connect('data.db')
    cursor = conn.cursor()
        
    if method:
        if language:
            cursor.execute("select file_name from methods where method_name = ? and language = ?", (method, language))
            result = cursor.fetchone()
            if result:
                result = result[0]
    
        else:
            cursor.execute("select language from methods where method_name = ?", (method, ))
            result = cursor.fetchall()
            if result:
                result = [i[0] for i in result]
    else:
        cursor.execute("select method_name from methods")
        result = cursor.fetchall()
        result = [i[0] for i in result]

    if result:
        return result
    return None 

def build():
    conn = sqlite3.connect('data.db')
    cursor = conn.cursor()

    cursor.execute('''CREATE TABLE IF NOT EXISTS methods (
                   id INTEGER PRIMARY KEY,
                   method_name TEXT NOT NULL,
                   language TEXT NOT NULL,
                   file_name TEXT NOT NULL
                )''')

    conn.commit()

if __name__ == "__main__":
    build()