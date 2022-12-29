def sdvig(s, n):
    s1 = [0]*len(s)
    for i in range(len(s)):
        s1[(i+n)%len(s)] = s[i]
    return s1


spisok1 = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
n = int(input())
print(*sdvig(spisok1, n))
spisok2 = [i for i in map(int, input().split())]
n = int(input())
print(*sdvig(spisok2, n))