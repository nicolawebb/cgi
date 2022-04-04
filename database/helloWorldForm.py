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

          if "Submit" in form:
            print('We are connected!')
            cursor = conn.cursor()
            query = "INSERT INTO Student (Name, CourseModule) VALUES (%s, %s)"
            args = (name, module)
            cursor.execute(query, args)

            html = """
            <body>
            <h1>Hello {name}. You're enrolled to study {module}. Enjoy!</h1>
            </body>
            """.format(
                    name=name,
                    module=module
                    )
            print(html)
            

          elif "Display" in form:
            cursor = conn.cursor() 
            #select all data from the Student table
            query = "SELECT * FROM Student"
            cursor.execute(query)
            #results contains the output of the query 
            results = cursor.fetchall()
            for row in results:
                  name = row[0] #name is the first column in the table so we select the first part of the query
                  module = row[1] #module is the second column so we select the second part of the query
                  #display the name and module column data
                  html = """
                  <body>
                  <p> {name} {module} </p>
                  </body>
                  """.format(
                          name=name,
                          module=module
                          )
                  print(html)
          else:
              print("Huh?")
  
          conn.commit()
          cursor.close()
        

    except Error as e:
        print(e)
    
    finally:
        conn.close()

if __name__ == '__main__':
    connect()