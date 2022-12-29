def recpow(a, n): # рекурсивное возведение в степень
    if n == 0:
        return 1
    return a*recpow(a, n-1)

def pow(a, n): # возведение в степень без рекурсии
    ans = 1
    for i in range(n):
        ans *= a
    return ans

print(recpow(2, 1))
print(pow(2, 1))