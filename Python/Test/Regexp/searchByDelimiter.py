# encoding: utf-8
#!/bin/python
#
#site: www.ahlinux.com
def tsplit(string, delimiters):
    """Behaves str.split but supports multiple delimiters."""

    delimiters = tuple(delimiters)
    stack = [string,]

    for delimiter in delimiters:
        for i, substring in enumerate(stack):
            substack = substring.split(delimiter)
            stack.pop(i)
            for j, _substring in enumerate(substack):
                stack.insert(i+j, _substring)

    return stack

s = 'thing1,thing2/thing3-thing4'
s2 = tsplit(s,(',','/','-'))
print s2

str = '﻿{"errcode":"0","errmsg":"\u767b\u9646\u6210\u529f"}'
print "Original str:", str
str2 = str.replace('﻿','')
print "The new str2:", str2