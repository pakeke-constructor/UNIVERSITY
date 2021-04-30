



from math import inf

EN=enumerate
RL= lambda x: range(len(x))


def get_info(info):
    directed = False
    weighted = False
    if info[0] == 'D':
        directed = True
    num_verts = int(info[1])
    if len(info) > 2:
        if info[2] == "W":
            weighted = True
    return (directed, num_verts, weighted)


def adjacency_list(st):
    info = st.splitlines()
    directed, num_verts, weighted = get_info(info[0].split())
    adj_list = []
    for i in range(num_verts):
        adj_list.append([])
    for edge in info[1:]:
        edge_info = edge.split()
        s_v = int(edge_info[0])
        e_v = int(edge_info[1])
        if weighted:
            adj_list[s_v].append((e_v, int(edge_info[2])))
        else:
            adj_list[s_v].append((e_v, None))
        if not directed:
            if weighted:
                adj_list[e_v].append((s_v, int(edge_info[2])))
            else:
                adj_list[e_v].append((s_v, None))
    return adj_list




def next_vertex(in_tree, distance):
    n_visited = []
    for i, vertex in enumerate(in_tree):
        if vertex == False:
            n_visited.append((distance[i], i))
    n_visited.sort()
    weight, next_vert = n_visited[0]
    return next_vert



def dijkstra(adj, start, d_s=None, p_s=None, in_s=None):
    n = len(adj)
    in_tree = [False] * n
    distance = [inf]*n
    parent = [None] * n
    distance[start]=0
    while not all(in_tree):
        u = next_vertex(in_tree, distance)
        in_tree[u] = True
        for v,w in adj[u]:
            if not in_tree[v] and distance[u] + w < distance[v]:
                distance[v] = distance[u] + w
                parent[v] = u
    return parent, distance




def min_capacity(city_map, depot):
    adj = adjacency_list(city_map)
    max_d = -1
    furthest = None
    _, d = dijkstra(adj, depot)
    for v in RL(adj):
        if d[v] > max_d and d[v] is not inf:
            max_d = d[v]
            furthest = v 

    return int((max_d * 6 * 3 * 2) / 0.8)

city_map = """\
U 4 W
0 2 5
0 3 2
3 2 2
"""

print(min_capacity(city_map, 0))
print(min_capacity(city_map, 1))
print(min_capacity(city_map, 2))
print(min_capacity(city_map, 3))



