from fib import s

mas=[0]*100

for j in range(10,100):
    st=str(j)
    i=0
    while i<len(s)-1:
        #print(st,s[i],s[i+1])
        if st[0]==s[i] and st[1]==s[i+1]:
            mas[j]+=1
            i+=1
        else:
            i+=1
#print(mas)
#print(s)
maxi=0
for i in range(len(mas)):
    maxi=max(mas[i],maxi)

for j in range(len(mas)):
    if mas[j]==maxi:
        print(j,maxi)