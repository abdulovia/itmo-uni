pole = {}
first_mass = [[6, 5, 12, 10, 9, 11, 1]]
pole[1] = first_mass
step = 2
k = 1

while k:
    mass = []
    for i in pole[step - 1]:
        if len(i) > 1:
            mass.append(i[:len(i) // 2:])
        mass.append(i[len(i) // 2::])
    pole[step] = mass
    k = 0
    for i in pole[step]:
        if len(i) != 1:
            k = 1
    step += 1

step -= 1


def sorter(x, y):
    res = []
    while x != [] or y != []:
        if x == []:
            for i in y:
                res.append(i)
            return res
        if y == []:
            for i in x:
                res.append(i)
            return res
        res.append(min(x[0], y[0]))
        if x[0] < y[0]:
            x.pop(0)
        else:
            y.pop(0)
    return res


pole2 = {}
pole2[step] = pole[step][::]
pole.pop(step)

while len(pole2[step]) > 1:
    mass = []
    for i in range(1, len(pole2[step]), 2):
        mass.append(sorter(pole2[step][i][::], pole2[step][i - 1][::]))
    if len(pole2[step]) % 2 == 1:
        mass.append(pole2[step][-1])
    pole2[step + 1] = mass
    step += 1

for i in pole.keys():
    print(i, pole[i])
for i in pole2.keys():
    print(i, pole2[i])
