

RL=lambda x: range(len(x))
EN = enumerate


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




'''
Require: G is a directed acyclic graph (DAG)
    1: function Topsort(G)
    2: T ← empty list
    3: Z ← empty queue/stack/whatever
    4: in ← dictionary mapping all vertices to 0 
    5: for each v ∈ V do
        6: for each u adjacent to v do
            7: increment in[v]
    8: for each v ∈ V do
    9:      if in[v] = 0 then
    10:         add v to Z
    11: while S is not empty do 
            12: v ← Z.remove
            13: append v to T 
            14: for each u adjacent to v do 
                15: decrement in[u]
                16: if in[u] = 0 then
                    17: add u to Z
    return T

'''



def top_sort(adj, order):
    if len(order) == len(adj):
        return order

    inn = {}

    for v in RL(adj):
        inn[v] = 0

    for v in RL(adj):
        for u, w in adj[v]:
            inn[u] += 1

    for v in RL(adj):
        if inn[v] == 0:
            if v not in order:
                order.append(v)
                adj[v] = []

    return top_sort(adj, order)




def build_order(dep):
    adj = adjacency_list(dep)
    return top_sort(adj, [])







dependencies = """\
D 2
0 1
"""

print(build_order(dependencies))
[0, 1]
dependencies = """\
D 3
1 2
0 2
"""

print(build_order(dependencies) in [[0, 1, 2], [1, 0, 2]])
True
dependencies = """\
D 3
"""
# any permutation of 0, 1, 2 is valid in this case.
solution = build_order(dependencies)
if solution is None:
    print("Wrong answer!")
else:
    print(sorted(solution))

