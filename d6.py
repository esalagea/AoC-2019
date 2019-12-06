def create_graph(filepath):
    graph = {}
    with open(filepath) as fp:
        line = fp.readline()
        while line:
            source, orbital = line.rstrip().split(")")
            graph[orbital] = {"s": source, "d": -1}
            line = fp.readline()
    return graph


def calculate_distance(graph, node):
    if graph[node]["d"] != -1:
        return graph[node]["d"]

    source = graph[node]["s"]

    if source == "COM":
        graph[node]["d"] = 1
        return 1

    distance = 1 + calculate_distance(graph, source)
    graph[node]["d"] = distance
    return distance


graph = create_graph("input/d6.txt")

# print graph
#
# print calculate_distance(graph, "D")
# print graph
#
# print calculate_distance(graph, "L")
#
# print graph

total_distance = 0
for node in graph:
    total_distance = total_distance + calculate_distance(graph, node)

print total_distance