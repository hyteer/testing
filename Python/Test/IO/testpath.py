import os

ospath = os.path
mydir = os.path.dirname(__file__)
pardir = os.pardir
joinpath = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir, 'res'))
strpath = os.path.abspath(os.path.join('D:\\Testing\\', os.pardir, 'Python'))

print 'ospath:',ospath
print mydir
print 'pardir:',pardir
print 'joinpath:', joinpath
print os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir, os.pardir))
print 'strpath:',strpath
