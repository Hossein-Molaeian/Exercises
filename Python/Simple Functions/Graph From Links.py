def graph(lst):
    graph_dict = {}

    for tople in lst:
        for node in tople:
            if node not in graph_dict:
                graph_dict[node] = []

        graph_dict[tople[0]].append(tople[1])
        graph_dict[tople[1]].append(tople[0])

    return graph_dict


print(graph([(1, 2), (1, 4), (2, 3), (3, 4)]))
