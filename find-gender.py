import json
import urllib2

Key = "find-your-gender"
name = raw_input("Enter name : ");
if name:
    data = json.load(urllib2.urlopen("https://gender-api.com/get?key=" + Key + "&name="+name))
    print "Gender: " + data["gender"];
else:
    print "Error!!"

#Output- Gender: male
