from random import randint
product = ['яблоки', 'апельсины', 'мандарины', 'киви', 'нектарины', 'груша', 'вишня', 'черешня', 'ананас', 'арбуз']
cost = []
for i in range(10):
    cost += [randint(20, 60)]
price = []
# print(product)
# print(cost)
for i in range(10):
    price += [int(cost[i]*1.15)]
shop = list(zip(product, cost, price))
for prod in shop:
    print(prod)