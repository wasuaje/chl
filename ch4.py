import urllib

start="12345"
divi="Yes. Divide by two and keep going."
nothing="and the next nothing is "

for i in range(0,401):
	data=urllib.urlopen("http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing="+start)
	print "url= "+"http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing="+start
	text=data.read()
	print text
	if nothing in text:
		start=text[text.find(nothing)+24:len(text)]
	else:
		if divi in text:
			start=str(int(start)/2)
#
#respuesta peak.html
#



