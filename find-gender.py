import json
    #The json library can parse JSON from strings or files.
    #The library parses JSON into a Python dictionary or list.It can also convert Python dictionaries or lists into JSON strings.
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

#Output- Gender: male
