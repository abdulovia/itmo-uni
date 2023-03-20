nodes = ["Невский проспект", "Лиговский проспект", "Вознесенский проспект", "Литейный проспект", "Адмиралтейский проспект",
         "Улица Некрасова", "Улица Моховая", "Владимирский проспект", "Малая Морская улица", "Малая Садовая улица"]

def f(s):
    return nodes.index(s)

INF = int(1e9+7)

graph = [[INF for i in range(len(nodes))] for j in range(len(nodes))]

graph[f("Невский проспект")][f("Лиговский проспект")] = 1.5
graph[f("Лиговский проспект")][f("Вознесенский проспект")] = 1.7
graph[f("Лиговский проспект")][f("Адмиралтейский проспект")] = 2
graph[f("Вознесенский проспект")][f("Улица Некрасова")] = 1.7
graph[f("Улица Моховая")][f("Невский проспект")] = 1.2
graph[f("Владимирский проспект")][f("Улица Моховая")] = 1.9
graph[f("Малая Садовая улица")][f("Улица Некрасова")] = 1.7
graph[f("Малая Морская улица")][f("Адмиралтейский проспект")] = 1.6
graph[f("Малая Садовая улица")][f("Адмиралтейский проспект")] = 1.5
graph[f("Невский проспект")][f("Адмиралтейский проспект")] = 3.6

for i in range(len(nodes)):
    for j in range(len(nodes)):
        graph[i][j] = min(graph[i][j], graph[j][i]) # граф неориентированный

start_node = "Владимирский проспект"
end_node = "Малая Садовая улица"
d = [INF for i in range(len(nodes))]
p = [-1 for i in range(len(nodes))]
d[f(start_node)] = 0
s = set()
s.add((0, f(start_node)))
while len(s) != 0:
    v = s.pop()[1]
    for u in range(len(nodes)):
        if u != v and graph[v][u] != INF:
            if d[v] + graph[v][u] < d[u]:
                if (d[u], u) in s:
                    s.remove((d[u], u))
                d[u] = d[v] + graph[v][u]
                p[u] = v
                s.add((d[u], u))
ans = [end_node]
i = f(end_node)
while p[i] != -1:
    ans += [nodes[p[i]]]
    i = p[i]
ans.reverse()
print(f'Искомый маршрут: {" –> ".join(ans)}')
print(f'Длина маршрута: {d[f(end_node)]}')

'''
<Graph indexType="custom" height="400" width="400" nodes={[{label:"Невский проспект",center:{x:184.1,y:280.3}},{label:"Лиговский проспект",center:{x:256.7,y:156.5}},{label:"Вознесенский проспект",center:{x:322.2,y:51}},{label:"Литейный проспект",center:{x:381.7,y:174.7}},{label:"Адмиралтейский проспект",center:{x:292.9,y:267.3}},{label:"Улица Некрасова",center:{x:186.1,y:51.6}},{label:"Улица Моховая",center:{x:114.1,y:384}},{label:"Владимирский проспект",center:{x:56.8,y:262}},{label:"Малая Морская улица",center:{x:248.8,y:389.7}},{label:"Малая Садовая улица",center:{x:150.7,y:177.3}}]} edges={[{label:"1.8",source:0,target:1},{label:"1.7",source:1,target:2},{label:"2",source:1,target:4},{label:"1.7",source:2,target:5},{label:"1.2",source:6,target:0},{label:"1.9",source:7,target:6},{label:"1.7",source:9,target:5},{label:"1.6",source:8,target:4},{label:"1.5",source:9,target:4}]} />
'''
