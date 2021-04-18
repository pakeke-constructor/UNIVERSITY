

'''
from l5 import *
from l4 import *
from os import system
system('cls')
'''





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



from math import inf



def format_sequence(converters_info, source_format, destination_format):
    '''
    find the shortest path between A -> B in the graph

    '''
    adj = adjacency_list(converters_info)
    paths = all_paths(adj, source_format, destination_format)
    
    best = "No solution!"
    best_len = inf
    for path in paths:
        if len(path) < best_len:
            best_len = len(path)
            best = path
            
    if type(best) == str:
        return best
    return list(best)


converters_info_str = """\
D 2
0 1
"""

source_format = 0
destination_format = 1

print(format_sequence(converters_info_str, source_format, destination_format))
[0, 1]
converters_info_str = """\
D 2
0 1
"""

print(format_sequence(converters_info_str, 1, 1))
[1]
converters_info_str = """\
D 2
0 1
"""

print(format_sequence(converters_info_str, 1, 0))


converters_info_str = """\
D 5
1 0
0 2
2 3
1 2
"""

print(format_sequence(converters_info_str, 1, 2))
[1, 2]
converters_info_str = """\
D 1
"""

print(format_sequence(converters_info_str, 0, 0))

