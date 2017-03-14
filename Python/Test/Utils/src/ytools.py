import os,sys
import csv
import requests

# File manipulation
def read_csv(filename,):
    #import csv
    with open(filename, newline='') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
        for row in spamreader:
            #print(', '.join(row))
            print(row[0])


def write_csv(filename):
    with open('eggs.csv', 'w', newline='') as csvfile:
        spamwriter = csv.writer(csvfile, delimiter=' ',
                                quotechar='|', quoting=csv.QUOTE_MINIMAL)
        spamwriter.writerow(['Spam'] * 5 + ['Baked Beans'])
        spamwriter.writerow(['Spam', 'Lovely Spam', 'Wonderful Spam'])

# Requests

def req(url):
    print("URL:",url)
    r = requests.get(url)
    print("Code:",r.status_code)

########## Test #############

if __name__ == '__main__':

    sys.path.append(os.path.dirname(sys.path[0]))
    CSV_FILE = 'F:\\Temp\\wkd_users.csv'
    read_csv(CSV_FILE)

