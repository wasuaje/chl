import urllib

f=open("evil5.gfx",'r')
data=f.read()
f.close()

tupla=['','','','','']
cont=0

for char in range(len(data)):
    tupla[cont]+=data[char]
    cont+=1
    if cont==5:
        cont=0

for i in range(len(tupla)):
    f = open("file"+str(i)+".jpg",'w')
    f.write(tupla[i])
    f.close()
    
#respuesta: esto bota 5 imagenes .jpg con la palabra porportionality con el lity tachado, osea proportional    