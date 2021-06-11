
INF=float('inf')
EN=enumerate

def paz(graph_string):
    header, *edges = [s.split() for s in graph_string.splitlines()]
    directed = header[0] == 'D'
    weighted = len(header) == 3 and header[2] == 'W'
    num_vertices = int(header[1])
    adj_list = [[] for _ in range(num_vertices)]
    for edge in edges:
        edge_data = map(int, edge)
        if weighted:
            source, target, weight = edge_data
        else:
            source, target = edge_data
            weight = None
        adj_list[source].append((target, weight))
        if not directed:
            adj_list[target].append((source, weight))
    return adj_list


def nextv(intree, distance):
    best = None
    bestd = INF
    for v,each in EN(intree):
        if not each and distance[v] < bestd:
            bestd = distance[v]
            best = v
    return best




def prim(adj, s):
    n = len(adj)
    intree = [False] * n
    distance = [INF] * n
    parent = [None] * n
    distance[s] = 0
    while not all(intree):
        print(distance)
        print(parent)
        print(intree)
        print("\n\n")
        u = nextv(intree, distance)
        intree[u] = True
        for v, weight in adj[u]:
            if not intree[v] and weight < distance[v]:
                distance[v] = weight
                parent[v] = u
    return parent, distance


def path_length(parent, start, end):
    



prim(paz(
'''\
U 6 W
0 1 1
0 3 2
1 3 3
3 4 4
1 4 5
1 2 6
2 4 7
4 5 8
2 5 9
'''
),0)