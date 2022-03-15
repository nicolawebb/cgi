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
            cursor = conn.cursor()
            query = "INSERT INTO Student (Name, Age) VALUES (%s, %s)"
            (Name, Age) = ("Nicola Webb", 26)
            args = (Name, Age)

            cursor.execute(query, args)
            conn.commit()
            cursor.close()
        

    except Error as e:
        print(e)
    
    finally:
        conn.close()

if __name__ == '__main__':
    connect()