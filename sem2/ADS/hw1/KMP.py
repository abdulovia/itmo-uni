# Knuth-Morris-Pratt search algorithm
# author: @estle

from fib import s

def prefixF(n):
    p = []
    for j in range(len(n)):
        a = n[:j+1]
        if len(a)==1:
            p += [0]
        else:
            i = 0
            while i < len(a) and a[i] == a[-i-1]:
                i += 1
            p += [i]
    return p


ans = [0]*100
for num in range(10, 100):
    n = str(num)
    pF = prefixF(n)
    i = 0
    while i < len(s):
        j = i
        while j-i < len(n) and j < len(s) and n[j-i] == s[j]:
            j += 1
        if j-i == len(n) or j == len(s):
            ans[num] += 1
            i += 1
        else:
            step = j-i-1-pF[j-i]+1
            if step > 0:
                i += j-i-1-pF[j-i]+1
            else:
                i += 1
mx = max(ans)
print(mx)
for i in range(len(ans)):
    if ans[i] == mx:
        print(i)