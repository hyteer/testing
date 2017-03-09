

def trav_val(d,key):
  global tempval
  for k,v in d.items():
    if type(v) == dict:
      print("found a dict...")
      trav_val(v,key)
    elif k == key:
      print("Found:",v)
      tempval = v
      break
  print("tempval:",tempval)
  return tempval

def get_val(d,key):
	tempval = "default..."
	x = trav_val(d,key)
	print("Outval:",tempval)
	print("OutX:",x)
	tempval == "default..."
	return x

d1 =  {'age': 33, 'issue': {'hobit': 'Singing', 'lv': 'dyci'}, 'name': 'YT'}
d2 =  {'age': 33, 'issue': {'hobit': 'Singing', 'deep':{'fav':'python'},'lv': 'dyci'}, 'name': 'YT'}
x = get_val(d2,'fav')
print("X:",x)


