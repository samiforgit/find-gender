# find-gender

####Aim : This function will find the Gender of a given name.<br>

######Function :  File Name : find-gender.py<br>

import json <br>
	&nbsp;&nbsp;####The json library can parse JSON from strings or files. The library parses JSON into a 	Python dictionary or list.It can also convert Python dictionaries or lists into JSON strings.<br>
import urllib2<br>
	&nbsp;&nbsp;####urllib2 — extensible library for opening URLs<br>
Key = "find-your-gender"<br>
	#your server key here<br>
name = raw_input("Enter name : ");<br>
	&nbsp;&nbsp;####It receives Input from user<br>
if name:<br>
    data = json.load(urllib2.urlopen("https://gender-api.com/get?key=" + Key + "&name="+name))<br>
    print "Gender: " + data["gender"];<br>
else:<br>
    print "Error!!"<br>
Output - Gender: male<br>


How To Works :<br>
1. Open Terminal<br>
2. Install Python 2.<br>
3. Put the file (find-gender.py ) in any folder<br>
4. From terminal access the file ie. PC:~$  cd FolderName/find-gender.py<br>
5. It will ask “Enter your name:”<br>
6. When you enter name it will show Gender (male/female)<br>
7. Otherwise It will show error!<br>


Thank you !!
