flag = ''


if __name__ == '__main__':
    global flag
    while flag != 'exit':
        print 'input ur choose:\n1.Tom\n2.SSH\n3.exit'
        choice = raw_input('>')

        if choice == '1':
            print "it's 1"
        elif choice == '2':
            print "it's 2"
        elif choice == 'exit':
            flag = 'exit'
        else:
            print "it's else"


