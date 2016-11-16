def ceiling(x):
    n = int(x)
    return n if n-1 < x <= n else n+1

print ceiling(8.1334)
