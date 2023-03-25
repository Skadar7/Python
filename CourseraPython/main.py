import sys
def D1c1w1t():
    print(sum(int(i) for i in sys.argv[1]))

def D1c1w2t(n):
    for i in range(n+1):
        print(" "*(n-i)+"#"*i)

#D1c1w2t(int(sys.argv[1]))

def D1c1w3t(a, b, c):
    from math import sqrt
    a = int(a)
    b = int(b)
    c = int(c)
    d = b * b - 4 * a * c

    x1 = (-b + sqrt(d)) / (2 * a)
    x2 = (-b - sqrt(d)) / (2 * a)

    print(int(x1))
    print(int(x2))


#D1c1w3t(sys.argv[1], sys.argv[2], sys.argv[3])

#print(list(map(lambda x: str(x), [i for i in range(10, 21)])))
