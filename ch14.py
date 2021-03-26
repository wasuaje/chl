import urllib
from PIL import Image
#data=urllib.urlopen("http://www.pythonchallenge.com/pc/def/oxygen.png")
#text=data.read()
#f=open("oxygen.png",'wb')
#f.write(text)
#f.close()

#wire.png
#walk around
#<!-- remember: 100*100 = (100+99+99+98) + (...  -->

im = Image.open("wire.png")
pix = im.load()

newim = Image.new("RGB", (250, 4),"white")

width, height = im.size
#print width, height
all_pixels = []
newh=0  #hasta250
neww=0  #hasta4
for x in range(width-1,0,-1):
        print x
        cpixel=pix[x,0]
        print neww,newh
        newim.putpixel((neww,newh),cpixel[2])
        neww+=1
        if neww==250:
            neww=0  
            newh+=1
            if newh==4:
                newh=0
newim.show()
newim.save("prueba2.jpg")

#respuesta

