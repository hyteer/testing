import datetime
print(
    datetime.datetime.fromtimestamp(
        int("1487200061")
    ).strftime('%Y-%m-%d %H:%M:%S')
)

mytime = 1488420394

print(datetime.datetime.fromtimestamp(mytime).strftime('%Y-%m-%d %H:%M:%S'))