abc=[]
a="g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj"
alfabeto = 'abcdefghijklmnopqrstuvwxyz'
for i in alfabeto:
	abc.append(i)
#print abc
nt=''
for h in a:
	for p in range(0,len(alfabeto)):
		if  h==' ':
			nt+=' '
			break

		if h==alfabeto[p]:
			if  p==24:
				p=-2
			elif  p==25:
				p=-1		
			nt+=alfabeto[p+2]		
			
print nt
