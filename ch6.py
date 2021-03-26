import os,glob,zipfile

start="90052"
divi="Yes. Divide by two and keep going."
nothing="Next nothing is "
path = 'chl/'
#
infile = glob.glob( os.path.join(path, '*.txt') )
while True:
	if path+start+".txt" in infile:
		fil=open(path+start+".txt",'r')
		data=fil.read()
#		print data
		if nothing in data:
			start=data[data.find(nothing)+16:len(data)]
		else:
			if divi in data:
				start=str(int(start)/2)
		fil=zipfile.ZipFile("channel.zip","r")		
		for file in  fil.filelist:
			if start+".txt" in file.filename:			
				print file.comment,
# this will print the word hockey in banner form
# but each word in hockey is made of a letter
# finally it is oxygen
