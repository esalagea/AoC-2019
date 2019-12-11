def create_graph(filepath):
    graph = {}
    with open(filepath) as fp:
        line = fp.readline()
        while line:
            source, orbital = line.rstrip().split(")")
            graph[orbital] = {"s": source, "d": -1, "me":0, "santa":"0"}
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



def trace_route(graph, node, who):
    while node != "COM":
        graph[node][who] = 1
        node = graph[node]["s"]


def dist_to_intersection(graph, node):
    dist = 0
    while node != "COM":
        if graph[node]["me"] == 1 and graph[node]["santa"] == 1:
            return dist -1
        dist = dist+1
        node = graph[node]["s"]



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

trace_route(graph, "YOU", "me")
trace_route(graph, "SAN", "santa")

print graph

y =  dist_to_intersection(graph, "YOU")
s =  dist_to_intersection(graph, "SAN")

print y + s