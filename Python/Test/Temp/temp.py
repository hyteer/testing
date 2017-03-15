# coding: utf-8

PAY_TYPE = 1 
PAY_TYPES = [
        {'name': 'WXPAY.JSAPI','openid': 'oRs4Ywkv_6HCQu8DLQZAcyNARtPc'},
        {'name': 'ALIPAY.JSAPI','openid': '2088302373341516'},
    ]

print(PAY_TYPES[PAY_TYPE])
print(PAY_TYPES[PAY_TYPE]['openid'])

seq = ['start...']
seq.append('ending...')
print(seq)

class TempTest(object):
    seq = ['start...']
    fo = open("F:\\Log\\log_test_20170314.txt", "w")
    #print "文件名为: ", fo.name
    #seq = ["Ytest string 1.\n", "Ytest string2..."]
    fo.writelines( seq )

    def end_log(self):
        # Ending...
        self.seq.append('ending...')
        self.fo.writelines( seq )
        self.fo.close()

def log_to_file_():
    fo = open("F:\\Log\\log_test11.txt", "w")
    #print "文件名为: ", fo.name
    seq = ["Ytest string 1.\n", "Ytest string2..."]
    fo.writelines( seq )
    fo.close()

log_to_file_()