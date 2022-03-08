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
<body>
<h1>Hello {name}. You're enrolled to study {module}. Enjoy!</h1>
</body>
</html>
""".format(
        name=name,
        module=module
        )
print(html)