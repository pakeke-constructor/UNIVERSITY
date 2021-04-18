

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



def which_segments(city_map):
    adj = adjacency_list(city_map)
    par = prims(adj)
    edges_req = []

    for v in RL(par):
        if par[v] is not None:
            new = ((tuple(sorted([v, par[v]]))))
            edges_req.append(new)
    return edges_req


def prims(adj, start=0):
        n = len(adj)

        tree = [False for _ in range(n)]
        distance = [inf for _ in range(n)]
        par = [None for _ in range(n)]

        distance[start] = 0

        while False in tree:
            cur = next_vert(tree, distance)
            tree[cur] = True
            for v, w in adj[cur]:
                if not tree[v] and w < distance[v]:
                    distance[v] = w
                    par[v] = cur
        return par


def next_vert(tree, distance):
    data = []

    for v, b in EN(tree):
        if not b:
            data.append((v, distance[v]))
    
    cur = data[0][1]
    minn = data[0][0]

    for dat in data:
        if dat[1] < cur:
            cur = dat[1]
            minn = dat[0]
    return minn



city_map = """\
U 3 W
0 1 1
2 1 2
2 0 4
"""

print(sorted(which_segments(city_map)))
[(0, 1), (1, 2)]
city_map = """\
U 1 W
"""

print(sorted(which_segments(city_map)))


	
city_map = """\
U 6 W
2 0 1
1 2 3
0 1 2
2 3 4
5 2 7
3 4 5
4 5 6
"""

print(sorted(which_segments(city_map)))