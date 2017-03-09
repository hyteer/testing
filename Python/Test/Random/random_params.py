import random,string


param1 = string.join(random.sample(['1','2','3','4','5','6','7','8','9'], 5)).replace(" ","")
param2 = string.join(random.sample(['1','2','3','4','5','6','7','8','9'], 2)).replace(" ","")
param3 = str(random.randrange(1,3))
params = param1 + ',' + param2 + ',' + param3

print "Params:", params
