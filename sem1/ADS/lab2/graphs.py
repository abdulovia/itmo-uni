import itertools
import networkx as nx
import numpy as np
import matplotlib.pyplot as plt
from answers import students
from questions import for_graph

graph = nx.Graph()
ixes = list(range(len(students)))  # индексы студентов
for ix in ixes:
    node_name = students[ix]["name"].replace(' ', '\n')
    graph.add_node(node_name)

for i in for_graph.keys():
    graph.add_node(for_graph[i])


def add_edge(f_item, s_item, graph=None):
    graph.add_edge(f_item, s_item)
    graph.add_edge(s_item, f_item)


for i in for_graph.keys():
    for ix in ixes:
        node_name = students[ix]["name"].replace(' ', '\n')
        if students[ix][i]:
            add_edge(node_name, for_graph[i], graph=graph)

nx.draw_shell(graph, node_color='white', node_size=300, with_labels=True)  # draw_circular/draw_shell
