import sys

def utf8_filter(str):
    if sys.stdout.encoding == 'cp936':
        #sys.stdout = UnicodeStreamFilter(sys.stdout)
        return str
    else:
        return str.encode('utf-8')



