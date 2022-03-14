import mysql.connector
from mysql.connector import Error

def connect():
    try:
        conn = mysql.connector.connect(host='localhost',
                                        database='test',
                                        user='root',
                                        password='password')

        if conn.is_connected():
            print('We are connected!')
    except Error as e:
        print(e)
    
    finally:
        conn.close()

if __name__ == '__main__':
    connect()