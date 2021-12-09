graph = {'A' : ['B','S'], 'B' : ['A'], 'C' : ['S','D','F','E'], 'D' : ['C'], 'E' : ['C','H'], 'F' : ['G','C'], 'S' : ['C','A','G'],'G':['F','S','H'],'H':['E','G']}
visited = set()
def dfs(visited, graph, node):
    if node not in visited:
        print (node, "->", end=" ")
        visited.add(node)
        for neighbour in graph[node]:
            dfs(visited, graph, neighbour)
print("EKANSH JAIN A2305218211 7CSE-4X\n")
print("Graph:")
print(graph)
print("\nStarting Node: 'A'")
print("DFS Traversal: ")
dfs(visited, graph, 'A')
print("end")
