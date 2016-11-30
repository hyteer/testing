
#str = bytes().fromhex('010210')

#print bytes().fromhex('010210')

print bytes(map(ord, '\x01\x02\x31\x32'))
print bytes(map(ord, '\x00'))

