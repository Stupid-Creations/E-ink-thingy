file = open("Redemption of Time/OEBPS/Text/008.html",encoding='utf8')
opened = True
string = ''
tag = ''
tags = []
strings = []
temps = []
for i in file.read().split("</head>")[-1]:
	if i == "<":
		opened = True
		print('oepned')
	if not opened:
		if i == '\n' and string!='' and string!=' ':
			tags.append(temps)
			temps = []
			strings.append(string)
			string = ''
		else:
			if i!= '\n':
				string+=i
	if opened:
		tag+=i
	if i == ">":
		opened = False
		temps.append(tag)
		tag = ""

tags.pop()
types = []
print(len(tags),len(strings))
for (i,j) in zip(tags,strings):
	types.append([k for k in ''.join(i).split('"') if '<' not in k and ">" not in k])

flat_list = [
    x
    for xs in types
    for x in xs
]

print("All modifiers")
print(list(set(flat_list)))
final = []
for i in types:
	temp = []
	for j in range(len(i)):
		if i[j] == "bolditalic":
			temp.append("bi")
		if i[j] == "indent":
			temp.append('t')
		if i[j] == "section-break":
			temp.append("n")
		if i[j] == "header21":
			temp.append("h")
		if i[j] == "center-text":
			temp.append("c")
		if i[j] == "italic":
			temp.append("i")
	final.append(temp)

compacted = open("book.bk",'w',encoding='utf8')
for i in range(len(final)):
	compacted.write(''.join(final[i])+"<>"+strings[i])
	compacted.write('\n')

compacted.close()
print("Wrote!")