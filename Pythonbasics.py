#assigning variables
zip_code=20854
print(zip_code)


#Other variables
a=5
b=3
c=a+b
print (c)

#assigning a string of text ""
firstname="Arlette"
print(firstname)

#assigning a string of text ' '
lastname='geller'
fullname=firstname+lastname
print(fullname)

fullname1=firstname+""+lastname
print(fullname1)

possessive="Arlette's"
print(possessive)
quote='He said. "Go home."'
print(quote)

#adding zipcode to name
#cannot add integer and string
#namezip=fullname+zip_code

#to do that we use the str function
namezip=fullname+str(zip_code)
print(namezip)

#Function directory of variables to list all variables used in session
dir()

#to terminate program and return to main
#quit() 
