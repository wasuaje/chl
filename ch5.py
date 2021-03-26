
import pickle,sys
pkl_file = open('banner.p', 'rb')
data1 = pickle.load(pkl_file)

cont=0
txt='\n'
for a in data1:	
	for b in a:		
		sys.stdout.write(b[0]*b[1])
	print "\r"
	
				
print txt
pkl_file.close()

#respuesta channel




