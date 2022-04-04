#!C:\Users\niick\AppData\Local\Programs\Python\Python36\python.exe
import cgi
import cgitb      #use for error traces
cgitb.enable()    #use for error traces

# Create instance of FieldStorage 
form = cgi.FieldStorage() 

# Get data from fields  
name = form.getvalue('name')        # name of the field is same as in client form
module  = form.getvalue('module')   # name of the field is same as in client form

html = """
  <html>
  <head>
    <link rel="stylesheet" href="styles.css">
  </head>
  </html>
  """
print(html)


if "Submit" in form:
  html = """
  <html>
  <head>
    <link rel="stylesheet" href="styles.css">
  </head>
  <body>
  <h1>Hello {name}. You're enrolled to study {module}. Enjoy!</h1>
  </body>
  </html>
  """.format(
          name=name,
          module=module
          )
  print(html)

elif "Display" in form:
  html = """
  <html>
  <head>
    <link rel="stylesheet" href="styles.css">
  </head>
  <body>
  <h1>Display!</h1>
  </body>
  </html>
  """
  print(html)
else:
    print("Huh?")
  





#-----------------------DATABASE------------------#
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
            query = "INSERT INTO Student (Name, CourseModule) VALUES (%s, %s)"
            args = (name, module)

            cursor.execute(query, args)
            conn.commit()
            cursor.close()
        

    except Error as e:
        print(e)
    
    finally:
        conn.close()

if __name__ == '__main__':
    connect()