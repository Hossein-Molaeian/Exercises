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

visited = []
queue = []


def bfs(visited, graph, node):
    visited.append(node)
    queue.append(node)

    while queue:
        m = queue.pop(0)
        print(m, end=" ")

        for neighbour in graph[m]:
            if neighbour not in visited:
                visited.append(neighbour)
                queue.append(neighbour)


print("Following is the research path:")
bfs(visited, graph, '4')
