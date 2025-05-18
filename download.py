from booker import Zlibrary
import random
# Create Zlibrary object and login
messages = [str(i) for i in range(20)]
for i in range(20):
	Z = Zlibrary(remix_userid="3984740", remix_userkey="93dcdba3eb9d81824205be4ec2c2bb54")
	user_profile = Z.getProfile()["user"]

	print("Remix User ID:", user_profile["id"])
	print("Remix User Key:", user_profile["remix_userkey"])
	# Get most popular books
	most_popular = Z.search(message=messages[i])
	# Downloading a book
	choose = 0
	for i in range(len(most_popular["books"])):
		if most_popular["books"][i]["extension"] == "epub":
			print('epub found')
			choose = i
			break
	filename, filecontent = Z.downloadBook(most_popular["books"][choose])

	# Writting file content to a file
	with open(filename, "wb") as bookfile:
	   bookfile.write(filecontent)
	print("DOWNLOaDED WOOOOO")
