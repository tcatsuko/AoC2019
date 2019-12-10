import networkx as nx
f = open('aoc06.txt','r')
input_file = []
for line in f:
    input_file += [line[:-1]]
f.close()
G = nx.DiGraph()
G2 = nx.Graph()
for item in input_file:
    split_items = item.split(')')
    G.add_edge(split_items[0], split_items[1])
    G2.add_edge(split_items[0], split_items[1])
orbits = 0
root_node = [n for n, d in G.in_degree() if d == 0][0]
for node in G.nodes:
    orbits += nx.shortest_path_length(G, root_node, node)
print('Part 1: there are ' + str(orbits) + ' orbits')
print('Paet 2: You need to do ' + str(nx.shortest_path_length(G2, 'YOU', 'SAN')-2) + ' transfers.')