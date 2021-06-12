
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
        if (not each) and distance[v] < bestd:
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


    



def longest_common_subsequence(list1, list2):
    lcs = longest_common_subsequence
    keyy = lambda lis : len(lis)
    if len(list1) == 0 or len(list2) == 0:
        return []
    ret = []
    if list1[0] == list2[0]:
        ret.append(list1[0])
        return max(lcs(list1[1:], list2[2:]),
                    lcs(list1[2:], list2[1:]), key=keyy)






list1 = [19, 5, 5, 0, 13, 5, 0, 1, 14, 7, 21, 1]
list2 = [19, 5, 5, 0, 20, 8, 5, 0, 7, 21, 19]
print(longest_common_subsequence(list1, list2))
[19, 5, 5, 0, 5, 0, 7, 21]
list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
list2 = [10, 20, 30, 40, 50, 60, 70, 80, 90]
print(longest_common_subsequence(list1, list2))
[]
list1 = [1, -1, 3, 5, 7, 9, 5, 3, 2, 11]
list2 = [1, -1, 3, 5, 7, 9, 5, 3, 2, 11]
print(longest_common_subsequence(list1, list2))

