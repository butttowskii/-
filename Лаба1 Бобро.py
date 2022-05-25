import networkx as nx
import matplotlib.pyplot as plt
a = int(input("введите количество ребер: "))
b = int(input("Ввведите начальную вершину"))
c = int(input("Ввведите конечную вершину"))
spisok = []
for i in range(a):
    spisok.append([int(z) for z in input("введите ребро и его вес: ").split()])
print("spisok = ",spisok)

G = nx.DiGraph()
nodes = []

for i in range(a):
    for j in range(2):
        nodes.append(spisok[i][j])
print(nodes)

G.add_nodes_from(nodes)

for i in range(a):
    G.add_edge(spisok[i][0],spisok[i][1], weight=spisok[i][2])
print(nx.dijkstra_path(G, b, c))
print(nx.dijkstra_path_length(G, b, c))
nx.draw_circular(G,
         node_color='red',
         node_size=1000,
         with_labels=True)
plt.show()





