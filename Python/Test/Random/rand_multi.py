#coding:utf8
import random
import string
#随机整数：
print random.randint(1,50)
#随机选取0到100间的偶数：
print random.randrange(0, 101, 2)
#随机浮点数：
print random.random()
print random.uniform(1, 10)
#随机字符：
print random.choice('abcdefghijklmnopqrstuvwxyz!@#$%^&*()')
#多个字符中选取特定数量的字符：
print random.sample('zyxwvutsrqponmlkjihgfedcba',5)
#多个字符中选取特定数量的字符组成新字符串：
print string.join(random.sample(['z','y','x','w','v','u','t','s','r','q','p','o','n','m','l','k','j','i','h','g','f','e','d','c','b','a'], 5)).replace(' ','')
#随机选取字符串：
print random.choice(['剪刀', '石头', '布'])
#打乱排序
items = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
print random.shuffle(items)