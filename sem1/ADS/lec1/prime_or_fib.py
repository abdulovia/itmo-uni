def Prime(n):
    if n < 2: return False
    for i in range(2, int(n**0.5)+1):
        if n%i==0: return False
    return True

def Fib(n):
    a1, a2 = 1, 2
    while a2 < n:
        a1, a2 = a2, a1 + a2
    return n==a2 or n==a1


for i in range(1, 20):
    # n = int(input())
    n = i
    prime, fib = Prime(n), Fib(n)
    if prime and fib:
        print('Простое и Фибонначи')
    elif prime:
        print('Простое')
    elif fib:
        print('Фибонначи')
    else:
        print(n)
