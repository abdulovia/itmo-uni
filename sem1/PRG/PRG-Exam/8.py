from datetime import datetime

now = datetime.now()
now = now.strftime("%d.%m.%Y %H:%M:%S")
print(now)
out = open(now, 'w')

names = ["dat.csv", "data.csv"]
for i in names:
    data = open(i).read()
    print(data, file=out)