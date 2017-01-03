import random
import string
print "Random Int from 100 to 999: %d" % random.randint(100,999)
randNameX = string.join(random.sample(['0','1','2','3','4','5','6','7','8','9','a','b','c','d','e','f','g','h','i','j','k','l','m','n','@','#','%','^','*','-'], 8)).replace(" ","")
print "Random String: " + randNameX