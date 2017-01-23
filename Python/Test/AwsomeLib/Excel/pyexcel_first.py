# coding: utf-8
import pyexcel as pe

file = "testfile.xlsx"
records = pe.iget_records(file_name=file)
list = pe.get_array(file_name=file)

def print_dict():
    for record in records:
        print("%s is aged at %s" % (record[u'名称'], record['Age']))
        #print("Use list way:")
        #print("%s is aged at %s" % (list[0], list[1]))


print_dict()

num = len(list)
print("-----------Total: %d-------------") % num

def print_list1():
    for i in range(1,num):
        if i == 1:
            print("Name, Age")
        else:
            print("%s, %s") % (list[i][0],list[i][1])

def print_list2():
    for i in range(0,num):
        print("%s, %s") % (list[i][0],list[i][1])

print_list2()