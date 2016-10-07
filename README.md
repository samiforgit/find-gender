# find-gender

##Aim : This function will find the Gender of a given name.

Function :  File Name : find-gender.py
import json 
	#The json library can parse JSON from strings or files. The library parses JSON into a 	Python dictionary or list.It can also convert Python dictionaries or lists into JSON strings.

import urllib2
	#urllib2 — extensible library for opening URLs

Key = "find-your-gender"
	#your server key here

name = raw_input("Enter name : ");
	# It receives Input from user

if name:
    data = json.load(urllib2.urlopen("https://gender-api.com/get?key=" + Key + "&name="+name))
    print "Gender: " + data["gender"];
else:
    print "Error!!"

Output - Gender: male

How To Works :
1. Open Terminal
2. Install Python 2.
3. Put the file (find-gender.py ) in any folder
4. From terminal access the file ie. PC:~$  cd FolderName/find-gender.py
5. It will ask “Enter your name:”
6. When you enter name it will show Gender (male/female)
7. Otherwise It will show error!


Thank you !!
