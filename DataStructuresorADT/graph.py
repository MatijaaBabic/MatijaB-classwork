import networkx as nx
import matplotlib.pyplot as plt


# Example graph represented as an adjacency list 
graph = { 'A': ['B', 'C'], 'B': ['A', 'D'], 'C': ['A', 'E', 'F'], 'D': ['B', 'G'], 'E': ['C', 'H'], 'F': ['C', 'I'], 'G': ['D', 'J', 'K'], 'H': ['E', 'K', 'L'], 'I': ['F', 'L', 'J'], 'J': ['G', 'I'], 'K': ['G', 'H'], 'L': ['H', 'I'] }

#generating edges
def generate_edges(g): 
    edges = [] 
    for node in g: 
        for neighbour in g[node]: 
            edges.append((node, neighbour)) 
    return edges 

print(generate_edges(graph))

g = nx.Graph(graph)
 
g.add_edge(1, 2)
g.add_edge(2, 3)
g.add_edge(3, 4)
g.add_edge(1, 4)
g.add_edge(1, 5)
 
nx.draw(g)
plt.savefig("filename.png")

