import os,re

dir1 = os.path.dirname(__file__)
dir2 = os.path.dirname(dir1)
dir3 = os.path.dirname(dir2)
BASE_DIR = os.path.dirname(os.path.dirname(__file__))
filedir = os.path.abspath(os.path.dirname(__file__))
print "dir1:",dir1
print "dir2:",dir2
print "dir3:",dir3
print "basedir:",BASE_DIR
print "filedir:",filedir

filepath = os.path.join(BASE_DIR,'Res/testfile.txt')

file = open(filepath,'r')
content = file.read()

print "file content:",content
