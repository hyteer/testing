import json

file = open("d:/Res/MaishaReq2.txt","r")
content = file.read()
jsdata = json.loads(content)

print jsdata