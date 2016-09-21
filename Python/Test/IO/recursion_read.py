#!/usr/bin/python  
#coding:utf8  
  
import os

robot_path = "D:\Testing\Robot\WSH\Web\Beta"
print robot_path

def dirlist(path, allfile):  
    filelist =  os.listdir(path)  
  
    for filename in filelist:  
        filepath = os.path.join(path, filename)
        #print "coding:",isinstance(str(filepath), unicode)

        if type(filepath).__name__!="unicode":
            filepath=filepath.decode("gbk").encode("utf-8")
        else:
            pass

        if os.path.isdir(filepath):
            dirlist(filepath, allfile)
        else:  
            allfile.append(filepath)
    return allfile  

allfiles = dirlist(robot_path, [])

print allfiles



for file in allfiles:
    #ufile = file.encode("utf-8")
    #ufile = file.decode(encoding="utf-8", errors="strict")
    print file
