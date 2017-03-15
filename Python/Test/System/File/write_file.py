# coding: utf-8

def log_to_file(self):
    # 打开一个文件
    fo = open("F:\\Log\\foo.txt", "wb")
    fo.write( "Just a test!\nit's over!\n");
     
    # 关闭打开的文件
    fo.close()

def log_to_file_2(mylog):
	fo = open("F:\\Log\\log_test.txt", "w")
	print "文件名为: ", fo.name
	#seq = ["Ytest string 1.\n", "Ytest string2..."]
	fo.writelines(mylog)
	fo.close()

mylog = ['start...\n']

mylog.append('aa1\n')
mylog.append('aa2\n')

log1 = ['sls','aiaa','saely']
print(mylog)

log_to_file_2(mylog)