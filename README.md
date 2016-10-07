# find-gender
####Aim : This function will find the Gender of a given name.<br>
<hr>
#####Function :(File Name : find-gender.py)<br>
import json <br>
 <font size="8px;"> #The json library can parse JSON from strings or files. The library parses JSON into a 	Python dictionary or list.It can also convert Python dictionaries or lists into JSON strings.</font><br>
import urllib2<br>
<font size="8px;"> #urllib2 — extensible library for opening URLs</font><br>
Key = "find-your-gender"<br>
<font size="8px;"> #your server key here</font><br>
name = raw_input("Enter name : ");<br>
<font size="8px;"> #It receives Input from user</font><br>
if name:<br>
    data = json.load(urllib2.urlopen("https://gender-api.com/get?key=" + Key + "&name="+name))<br>
    print "Gender: " + data["gender"];<br>
else:<br>
    print "Error!!"<br>
<hr>
Output - Gender: male<br>

<hr>
How To Works :<br>
1. Open Terminal<br>
2. Install Python 2.<br>
3. Put the file (find-gender.py ) in any folder<br>
4. From terminal access the file ie. PC:~$  cd FolderName/find-gender.py<br>
5. It will ask “Enter your name:”<br>
6. When you enter name it will show Gender (male/female)<br>
7. Otherwise It will show error!<br>


Thank you !!
