import zipfile
book = open('book.epub','rb')
archive = open("book.zip",'wb')
archive.write(book.read())
archive.close()
book.close()
zip_file = zipfile.ZipFile('book.zip', 'r') 
zip_file.printdir() # Open in read mode ('r')
print('zipfile exists :, stuff written!')