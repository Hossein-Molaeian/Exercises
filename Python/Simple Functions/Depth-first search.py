graph = {
    '4': ['7', '9'],
    '7': ['6', '2'],
    '9': ['5'],
    '6': [],
    '2': ['1', '3'],
    '5': ['8'],
    '8': [],
    '1': [],
    '3': []
}

visited = set()


def dfs(visited, graph, node):
    if node not in visited:
        print(node, end=" ")
        visited.add(node)
        for neighbour in graph[node]:
            dfs(visited, graph, neighbour)


print("DFS research path:")
dfs(visited, graph, '4')
