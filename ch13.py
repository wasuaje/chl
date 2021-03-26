import xmlrpclib

s = xmlrpclib.ServerProxy('http://www.pythonchallenge.com/pc/phonebook.php')
print s.system.listMethods()
print s.phone('Bert')  


#Respuesta devuelce un 555-ITALY, la clave: italy