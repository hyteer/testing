import re
n=2
def isnumber(num):
    regex = re.compile(r"^(-?\d+)(\.\d*)?$")
    if re.match(regex,n):
        return True
    else:
        return False


