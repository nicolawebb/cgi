#!C:\Users\niick\AppData\Local\Programs\Python\Python36\python.exe
import cgi
import cgitb      #use for error traces
cgitb.enable()    #use for error traces

#add html header here so no matter the condition we have a header
html = """
      <html>
      <head>
        <link rel="stylesheet" href="styles.css">
      </head>
      </html>
      """
print(html)

name = ''
module = ''


###============================ALL FIELDS FILLED OUT============================###

#check all fields have been filled out and if they are the correct type if necessary
def checkForm():
  check = 1
  if name == None:
    print("<p style='color:red'>Name is a required field!</p>")
    check = 0
  if module == None:
    print("<p style='color:red'>Module is a required field!</p>")
    check = 0
  elif not module.isnumeric():
    print("<p style='color:red'>Module is a number</p>")
    check = 0
  if check == 0:
    print("<p style='color:red'>Please complete the form!</p>")
  return check

###============================================================================####





###==================================UNIQUE DATA===============================###

#check if name user has entered is unique
fileContents=[]
def checkInput(file, name):
  unique = True
  with open(file) as user_file:
    for lines in user_file:
      lines = lines.rstrip()
      fileContents.append(lines)
  for x in fileContents:
    splitLine = x.split(",")
    userName = splitLine[0]
    #only checking name as serveral people can take the same module
    if name == userName:
      print("not unique")
      unique = False
  return unique

  ###=========================================================================####



###==================================REFRESH FORM===============================###

#shows a blank form to let the user enter data again 
def reloadForm():
  print("<p style='color:red'>Please fill out the entire form</p>")

  #this is the same html as 'helloWorldForm'html'
  html = """
    <form action="helloWorldForm.py" method="POST">
      Student Name: <input type="text" name="name">   
      <br>
      Course Module: <input type="text" name="module">
      <input type="submit" value="Submit" class="button">
    </form>
  """
  print(html)

  ###=============================================================####




# Create instance of FieldStorage 
form = cgi.FieldStorage()
#check if there is any data in the form 
keys = list(form.keys())

#if there is any data inputted in the form
if len(keys) > 0:
  # Get data from fields  
  name = form.getvalue('name')        # name of the field is same as in client form
  module  = form.getvalue('module')   # name of the field is same as in client form

  #if all fields have been filled out and are the correct type, add it to the text file
  if checkForm():
    path = 'users.txt'
    
    #if input is unique...
    if checkInput(path, name):
      #add input to the text file
      file = open(path, 'a')
      formFields = name + "," + module + "\n"
      file.write(formFields)
      file.close()

      #display the next page with the data from the form
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

    else:
      #if input not unique ask user to re-enter
      print("<p style='color:red'>Data already entered!</p>")
      reloadForm()

  else:
    #if all fields not filled out or are not the correct type, reload the form
    reloadForm()

else:
  #if not data entered at all, reload the form
  print("<p style='color:red'>Please fill out form!</p>")
  reloadForm()
