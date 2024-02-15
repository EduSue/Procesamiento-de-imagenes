h = input()
h = float(h)

# print(h)

if h == 1:
    print(1)
else:
    o = 0
    n = 0
    m = 1
    r = 0
    while o < h:
        r = n
        
        n = n + m

        m = r

        o = o + 1
        print(n)