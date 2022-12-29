# Vstan v stroy!
rost = [155, 149, 180, 175, 164, 195]
rost.sort(reverse=True)
while True:
    r = input()
    if r == 'все построены':
        break
    r = int(r)
    ix = -1
    for i in range(len(rost)):
        if rost[i] <= r:
            ix = i
            break
    if ix == -1: ix = len(rost)
    print(*rost)
    print(ix+1)
    rost.append(r)
    rost.sort(reverse=True)
print(*rost)
    