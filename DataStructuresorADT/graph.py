
# Example graph represented as an adjacency list 
graph = { 'A': ['B', 'C'], 'B': ['A', 'D'], 'C': ['A', 'E', 'F'], 'D': ['B', 'G'], 'E': ['C', 'H'], 'F': ['C', 'I'], 'G': ['D', 'J', 'K'], 'H': ['E', 'K', 'L'], 'I': ['F', 'L', 'J'], 'J': ['G', 'I'], 'K': ['G', 'H'], 'L': ['H', 'I'] }

#generating edges
def generate_edges(g): 
    edges = [] 
    for node in g: 
        for neighbour in g[node]: 
            edges.append((node, neighbour)) 
        #next neighbour
    #next node
    return edges
#end function 

print(generate_edges(graph))
#finding shortest paths
def bfs_shortest_paths(g, start):
    paths = {node: [] for node in g}
    paths[start] = [start]

    queue = [start]

    while queue:
        current_node = queue.pop(0)

        for neighbour in g[current_node]:
            if not paths[neighbour]:
                paths[neighbour] = paths[current_node] + [neighbour]
                queue.append(neighbour)
            #endif
        #next neighbour
    #endwhile
    

    return paths
#end function

print("Shortest paths from 'A' to other nodes are:", bfs_shortest_paths(graph, 'A'))
print("Shortest paths from 'D' to other nodes are:", bfs_shortest_paths(graph, 'D'))