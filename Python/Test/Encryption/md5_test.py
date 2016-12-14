import md5

# 1. Use MD5 lib
src = 'this is a md5 test.'   
m1 = md5.new()   
m1.update(src)   
print m1.hexdigest()  


# 2. Use hashlib

import hashlib   

m2 = hashlib.md5()   
m2.update(src)   
print m2.hexdigest()  
