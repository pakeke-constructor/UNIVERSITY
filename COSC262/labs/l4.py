
EN=enumerate


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



def make2d(n):
    mat = []
    for _ in range(n):
        mat.append([None] * n)
    return mat

def adjacency_matrix(adj_list):
    if isinstance(adj_list, str):
        adj_list = adjacency_list(adj_list)

    mat = make2d(len(adj_list))

    for i,ar in EN(adj_list):
        for v, weight in ar:
            if weight is not None:
                mat[i][v]=weight
            else:
                mat[i][v]=1

    return mat



def matrix_to_adj_list(matrix, weighted):
    adj_list = [None] * len(matrix)

    for i,arr in EN(matrix):
        adj_list[i] = []
        for v,ww in EN(arr):
            if ww is not None:
                if weighted:
                    w = ww
                else:
                    w = None
                adj_list[i].append((v,w))
    
    return adj_list


def transpose_matrix(mat):
    new = make2d(len(mat))
    for k,_ in EN(mat):
        for j,_ in EN(mat):
            new[k][j] = mat[j][k]
    return new


def is_weighted(adj_list):
    for a in adj_list:
        for v,w in a:
            if w:
                return True
    return False

def transpose(adj_list):
    m = transpose_matrix(adjacency_matrix(adj_list))
    if is_weighted(adj_list):
        we = True
    else:
        we = False
    return matrix_to_adj_list(m,we)


def bfs_adj_list(adj_list, start):
    visited, queue = ([start], [start])
    while queue:
        curr = queue.pop(0)
        adj_verts = adj_list[curr]
        for vert, weight in adj_verts:
            if vert not in visited:
                visited.append(vert)
                queue.append(vert)
    return visited


def top_sorts(adj_list):
    sorts = []
    for v,ar in EN(adj_list):
        vis = bfs_adj_list(adj_list,v)
        if len(vis)==len(adj_list):
            # is a valid order
            vis = vis[::-1]
            if vis not in sorts:
                sorts.append(vis)
    return sorts


'''
L ← Empty list that will contain the sorted elements
S ← Set of all nodes with no incoming edge

while S is not empty do
    remove a node n from S
    add n to L
    for each node m with an edge e from n to m do
        remove edge e from the graph
        if m has no other incoming edges then
            insert m into S

if graph has edges then
    return error   (graph has at least one cycle)
else 
    return L   (a topologically sorted order)
'''

import copy

def top_sort(adj_list):
    adj_list = copy.deepcopy(adj_list)
    L = []
    S = set(range(adj_list)) # Getting the set of verts with no incoming edge
    for vert in range(len(adj_list)):
        for v, w in adj_list[vert]:
            S.remove(v)

    while len(S) > 0:
        n = S.pop()
        L.append(n)
        for v, w in adj_list[n]:
            pass






'''
1 procedure Dijkstra(Adj, s)
2 n ← number of vertices (the length of Adj)
3 in-tree ← an array of length n filled with False
4 distance ← an array of length n filled with ∞
5 parent ← an array of length n filled with null
6 distance[s] ← 0
7 while ¬all(in-tree)
8 u ← Next-Vertex(in-tree, distance)
9 in-tree[u] ← True
10 for v, weight in Adj[u]
11 if ¬ in-tree[v] ∧ distance[u] + weight < distance[v]
12 distance[v] ← distance[u] + weight
13 parent[v] ← u
14 return parent, distance
'''


def next_vertex(in_tree, distance):
    n_visited = []
    for i, vertex in enumerate(in_tree):
        if vertex == False:
            n_visited.append((distance[i], i))
    return min(n_visited)[1]




def next_vertex(in_tree, distance):
    n_visited = []
    for i, vertex in enumerate(in_tree):
        if vertex == False:
            n_visited.append((distance[i], i))
    n_visited.sort()
    return n_visited[0][1]



from math import inf

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


from math import inf

def prims(adj, s):
    n = len(adj)
    inn = [False]*n
    distance = [inf] * n
    parent = [None] * n

    distance[s] = 0
    while not all(inn):
        u = next_vertex(inn, distance)
        inn[u] = True
        for v, w in adj[u]:
            if not inn[u] or weight < distance[v]:
                distance[v] = weight
                parent[v] = u
        

u = '''\
U 5 W
0 1 1
0 2 4
1 2 2
2 3 1
2 4 3
4 0 8
4 3 2
'''

if __name__ == "__main__":
    print(dijkstra(adjacency_list(u),3))



def num_sorts(adj_list):
    pass


def is_strongly_connected(adj_list):
    cn = []
    for i in range(len(adj_list)):
        cn.append(bfs_adj_list(adj_list, i))
    for conn_list in cn:
        if len(conn_list) != len(adj_list):
            return False
    return True


EN = enumerate
RL = lambda x: range(len(x))

def next_vertex(intree, distances):
    for i,each in EN(distances):






