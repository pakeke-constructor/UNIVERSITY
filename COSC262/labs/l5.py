


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
        mat.append([inf] * n)
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


from math import inf

def distance_matrix(adj):
    dist = make2d(len(adj))
    
    for i in range(len(adj)):
        dist[i][i] = 0

    for i, verts in EN(adj):
        for v, w in verts:
            if dist[i][v] > w:
                dist[i][v] = w
    return dist


import copy
from pprint import pprint


def floyd(mat):
    n = len(mat)
    mat = copy.deepcopy(mat)

    for k in range(n):
        if k == 2:
            print("[")
            for e in mat:
                print(e)
            print("]")
        for i in range(n):
            for j in range(n):
                if mat[i][j] > mat[i][k] + mat[k][j]:
                    mat[i][j] = mat[i][k] + mat[k][j]
    return mat











def dfs_backtrack(c, adj, dest, output_data):
    if is_solution(c, dest):
        add_to_output(c, output_data)
    else:
        for chil in children(c, adj, dest):
            dfs_backtrack(chil, adj, dest, output_data)



def add_to_output(c, output_data):
    output_data.append(c)



def is_solution(c, dest):
    return c[-1] == dest


def children(c, input_data, dest):
    # (1,2,3) candidate
    out = []
    if c[-1] == dest:
        return out
    for (to, w) in input_data[c[-1]]:
        if to not in c:
            out.append((*c,to))
    return out


def all_paths(adj_list, source, destination):
    lis = []
    dfs_backtrack((source,), adj_list, destination, lis)
    return lis


