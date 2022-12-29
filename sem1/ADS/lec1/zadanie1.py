def f(n):
	if n%3==0 and n%5==0:
		print("FizzBuzz", end=' ')
	elif n%3==0:
		print("Fizz", end=' ')
	elif n%5==0:
		print("Buzz", end=' ')
	else:
		print(n, end=' ')


n = int(input())
for i in range(1, n+1):
	f(i)
print()
