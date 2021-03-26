import urllib
from PIL import Image
#data=urllib.urlopen("http://www.pythonchallenge.com/pc/def/oxygen.png")
#text=data.read()
#f=open("oxygen.png",'wb')
#f.write(text)
#f.close()
im = Image.open("oxygen.png")
pix = im.load()

width, height = im.size

all_pixels = []
for x in range(width):
        cpixel = pix[x*7 , 43]
        print chr(cpixel[0]),

print chr(105),   chr(110) ,   chr(116) ,   chr(101) ,   chr(103) ,   chr(114) ,   chr(105) ,   chr(116) ,   chr(121) 

#respuesta s m a r t   g u y ,   y o u   m a d e   i t .   t h e   n e x t   l e v e l   i s   [ 1 0 5 ,   1 1 0 ,   1 1 6 ,   1 0 1 ,   1 0 3 ,   1 1 4 ,   1 0 5 ,   1 1 6 ,   1 2 1 ]	
# luego print char every number in list and
# i n t e g r i t y

