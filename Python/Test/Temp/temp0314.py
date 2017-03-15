
logs = ['aa1','bb','cc']

def collect_logs(newlog):
    global logs
    if len(logs) < 2:
        logs.append(newlog)


collect_logs('slaa')

print(logs)



