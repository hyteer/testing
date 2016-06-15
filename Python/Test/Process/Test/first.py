from multiprocessing import Pool

list = range(1,20,3)

def f(x):
    return x*x

if __name__ == '__main__':
    p = Pool(5)
    print(p.map(f, list))