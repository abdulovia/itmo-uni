def dist(t1, v1, t2, v2): # считает путь
    return t1*v1+t2*v2

t1, v1, t2, v2 = map(float, input().split())
print("%.2f" % dist(t1, v1, t2, v2))