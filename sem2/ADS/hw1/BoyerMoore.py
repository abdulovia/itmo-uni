from fib import s

ans = [0]*100
for num in range(10, 100):
    n = str(num)
    i = len(n)-1
    while i < len(s):
        j = i
        while j-i-1 >= -2 and n[j-i-1] == s[j]: # j-i-1 будет идти с конца шаблона (справа налево)
            j -= 1
        if j-i-1 == -3:
            ans[num] += 1
        elif j-i-1 > -2 and s[j] != n[j-i-2]: # когда символ не равен предыдущему в шаблоне
            i += 1
        i += 1
mx = max(ans)
print(mx)
for i in range(len(ans)):
    if ans[i] == mx:
        print(i)