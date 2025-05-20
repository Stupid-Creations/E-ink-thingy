import zipfile
import os 
try: 
	a = open("book.zip")
	a.close()
except:
	book = open('Percy Jackson and the Light_ (Z-Library) (Rick Riordan).epub','rb')
	archive = open("neeeew.zip",'wb')
	archive.write(book.read())
	archive.close()
	book.close()

zip_file = zipfile.ZipFile('book2.zip', 'r') 
a = zip_file.namelist() # Open in read mode ('r')
css = [i for i in a if 'css' in i] 
html = [i for i in a if 'html' in i and 'xhtml' not in i]

class css_reader:
	def __init__(self):
		self.keywords = []
		self.keywordcons = []
	def add_keyword(self,keyword,cons):
		if keyword in self.keywords:
			return
		self.keywords.append(keyword)
		self.keywordcons.append(cons)
	def get_cons(self,keyword):
		return self.keywordcons[self.keywords.index(keyword)]
	def add_from_file(self,filepath,zipped = True):
		if not zipped:
			csspool = open(filepath).read().decode('utf-8')
		else:
			print(filepath)
			file = zipfile.ZipFile(filepath,'r')
			a = file.namelist() # Open in read mode ('r')
			css = [i for i in a if 'css' in i] 
			csspool = ""
			for i in css:
				csspool+=file.read(i).decode('utf-8')
				csspool+='\n'

		tags = ''.join(''.join(csspool.split('.')).split('{')).split('}')
		tags = [i.replace('\n','') for i in tags if i != '']
		for i in tags:
			props = i.split('    ')
			if i != '':
				if len(props) <= 1:
					props = props[0].split('	')
				props = [i.replace(' ','') for i in props if i!='']
				self.add_keyword(props[0],[props[i] for i in range(1,len(props))])

print(css)
cssfile = zip_file.read(css[1]) #(either add checking the html thingies for css or check filesize)
tags = ''.join(''.join(cssfile.decode('utf-8').split('.')).split('{')).split('}')
tags = [i.replace('\n','') for i in tags]
print([i.replace(' ','') for i in tags[0].split('    ')])  
#ADD SPACES VERSUS TABS CHECK!!
new = css_reader()
new.add_from_file("book2.zip")
print(new.keywordcons)


