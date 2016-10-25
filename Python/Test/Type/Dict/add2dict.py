#coding:utf-8
def addWord(theIndex,word,pagenumber):
  theIndex.setdefault(word, [ ]).append(pagenumber) #存在就在基础上加入列表，不存在就新建个key

d = {"hello":[3]}
#d = {}
addWord(d,"hello",3)
addWord(d,"hello",56)
addWord(d,"nihao",24) 
print d

d.setdefault('test','value')
d['test2'].append(11)
print d


