import itertools, strings

a = [1, 11, 21, 1211, 111221, ]
#len(a[30]) = ?
#a = [1,]
                   
def lookandsay(oldtext):  	
      newtext = ""                                 #initialise
      repdigit = oldtext[0]		            #look at first digit
      numrep = 1                                   #and set counter to 1
      for  i in range(1, len(oldtext)):          #loop through old text         
          if repdigit == oldtext[i:i+1]:     #if new digit same as previous.. 
             
              numrep+=1                                 #...add one to counter
              
          else:                                          #but if different
             
              newtext = newtext + str(numrep) + str(repdigit)    #develop new text 
              repdigit = oldtext[i:i+1]      #remember new digit for next loop
              numrep = 1                               #and reset counter to 1             
         
      newtext = newtext + str(numrep) + str(repdigit)            #deal with ending of old text 

      return newtext                                   #end function
     
h=lookandsay('1')
for z in  range(0,29):
	print lookandsay(h)
	h=lookandsay(h)

print len(h)



#sacada de internet
#http:#www.btinternet.com/~se16/js/looknsay.htm
#respuesta 5808
#portada a python por wuelfhis asuaje
