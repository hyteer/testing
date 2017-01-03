# encoding: utf-8
# demo for showing type dict duplication
import json

js = {"br":"Opera", "pf": "Unix"}

#ddata = json.loads(js)
print js["br"]
print type(js)  # Get type
print str(js)





