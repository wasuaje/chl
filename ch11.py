import urllib,bz2
from PIL import Image
#data=urllib.urlopen("http://www.pythonchallenge.com/pc/return/cave.jpg")
#text=data.read()
#f=open("cave.jpg",'wb')
#f.write(text)
#f.close()


im = Image.open("cave.jpg")
pix = im.load()

width, height = im.size
print dir(im)
print dir(im.layers)
print im.layers
im.show()

all_pixels = []
for x in range(500,width):
	for y in range(height-200):
		print im.getpixel((x,y)),
#		if x%2 == 1 and y%2 == 0:
#			cpixel = pix[x , y]
#		        print chr(cpixel[0]),

#for x in range(width):
 #       cpixel = pix[x , 43]
  #      print chr(cpixel[0]),
        
#print chr(105),   chr(110) ,   chr(116) ,   chr(101) ,   chr(103) ,   chr(114) ,   chr(105) ,   chr(116) ,   chr(121) 

#respuesta 

