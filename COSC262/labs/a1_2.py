

#from l4 import *
#from l5 import *



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



def bubbles(phys):
    adj = adjacency_list(phys)
    if len(adj) == 0:
        return []
    
    nodes = set(range(len(adj)))
    components = 0

    bubs = []

    while len(nodes) > 0:
        components += 1
        person = nodes.pop()
        visited = set(bfs_adj_list(adj, person))
        bubs.append({person}.union(visited))
        nodes = nodes - visited
    
    return bubs



physical_contact_info = """\
U 2
0 1
"""

print(sorted(sorted(bubble) for bubble in bubbles(physical_contact_info)))
[[0, 1]]
physical_contact_info = """\
U 2
"""

print(sorted(sorted(bubble) for bubble in bubbles(physical_contact_info)))
[[0], [1]]
physical_contact_info = """\
U 7
1 2
1 5
1 6
2 3
2 5
3 4
4 5
"""

print(sorted(sorted(bubble) for bubble in bubbles(physical_contact_info)))
[[0], [1, 2, 3, 4, 5, 6]]
physical_contact_info = """\
U 0
"""

print(sorted(sorted(bubble) for bubble in bubbles(physical_contact_info)))
[]
physical_contact_info = """\
U 1
"""

print(sorted(sorted(bubble) for bubble in bubbles(physical_contact_info)))


    


