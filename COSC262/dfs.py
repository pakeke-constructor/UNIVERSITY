

'''


dfs lab

(YES I KNOW THIS CODE IS TERRIBLE.
I DONT CODE LIKE THIS NORMALLY I PROMISE.)

'''

enm = enumerate

class Q(object):
    def __init__(self, iterab=[]):
        self.q = list(iterab)

    def queue(self, item):
        self.q.insert(0,item)
        return item

    def dequeue(self):
        return self.q.pop()

    def __len__(self):
        return len(self.q)


class Vr(object):
    ''' vertex '''
    Verts = []
    N = 0
    weighted = False
    directed = False

    @classmethod
    def clear(cls):
        cls.Verts = []
        cls.N = 0

    def __init__(self, n, directed=False, weighted=False):
        self.weighted = weighted
        self.directed = directed

        self.chil = []
        self.chil_n = []
        self.weights  = {}
        self.n = n
        self._parent = None # temporary field for DFT

        Verts = Vr.Verts
        if self.n >= len(Verts):
            Verts.append(None)
            Verts[n] = self
        else:
            if Verts[n] is None:
                Verts[n] = self

    def bind(self, oth, weight = None):
        if isinstance(oth, int):
            oth = Vr.Verts[oth] # index into ar
        self.chil.append(oth)
        self.weights[oth.n] = (weight)
        self.chil_n.append(oth.n)
        if not self.directed:
            if not (self in oth.chil):
                oth.bind(self, weight)

    @classmethod
    def ct_str(cls, st):
        st = st.split("\n")
        while '' in st:
            st.remove('')

        start = st[0].split(' ')
        if len(start) == 2:
            dire, num = start
            w = False
        elif len(start) == 3:
            dire, num, _ = start
            w = True
        else:
            raise ValueError("invalid yo")
        
        num = int(num)
        st = st[1:]

        is_directed = (dire == "D")
        cls.N = num
        cls.directed = is_directed
        cls.weighted = w

        for i in range(num):
            cls(i, is_directed, w)

        for line in st:
            spl = line.split(" ")
            n1, n2 = int(spl[0]), int(spl[1])
            weight = None
            if w:
                weight = int(spl[-1])

            cls.Verts[n1].bind(n2, weight)
        
    @classmethod
    def ct_adj_list(cls, lis):
        n = len(lis)
        u = []
        for i in range(n):
            u.append(cls(i,True)) # fields tbd later

        cls.N = n
        for i,nodes in enumerate(lis):
            for tup in nodes:
                num, w = tup
                u[i].bind(u[num], w)
        return u


    @classmethod
    def adj_mat(cls):
        fill = 0
        if cls.weighted:
            fill = None
        
        ar = [
            [fill for _ in range(cls.N)] for _ in range(cls.N)
        ]
        
        for x in range(cls.N):
            for y in range(cls.N):
                v = cls.Verts[x]
                if y in v.chil_n:
                    if cls.weighted:
                        ar[x][y] = v.weights[y] or 0
                    else:
                        ar[x][y] = 1
        return ar
        
    @classmethod
    def adj_mat_p(cls):
        print("[")
        for e in cls.adj_mat():
            print(e)
        print("]")

    @classmethod
    def adj_list_p(cls):
        print("[")
        for v in cls.Verts:
            print(v.chil_n)
        print("]")

    @classmethod
    def adj_list(cls):
        ar = []
        for v in cls.Verts:
            tt = []
            for n in v.chil_n:
                tt.append((n, v.weights[n]))
            ar.append(tt)
        return ar

    @classmethod
    def bft(cls, root):
        '''
            breadth first tag
        '''
        if isinstance(root, int):
            root = cls.Verts[root]#conv to obj

        q = Q([root])
        cache = []
        seen = set([root.n])

        root = None

        while len(q) > 0:
            root = q.dequeue()
            cache.append(root)
            for e in root.chil:
                if not (e.n in seen):
                    q.queue(e)
                    e._parent = root
                    seen.add(e.n)

        ret = []
        for i in range(cls.N):
            v = cls.Verts[i]
            if v._parent:
                ret.append(cls.Verts[i]._parent.n)
            else:
                ret.append(None)
        return ret

    @classmethod
    def dfs(cls, root, vt=None, cycle_detect=False):
        if vt is None:
            vt = [root]
        for v in root.chil:
            if v not in vt:
                v._parent = root
                vt.append(v)
                cls.dfs(v, vt)
            else:
                # we have already visited! cycle
                cycle_detect=True
        return vt, cycle_detect

    @classmethod
    def dft(cls, root):
        vv, cyc_d = cls.dfs(root)
        for e in sorted(vv, key=lambda L:L.n):
            if e._parent:
                print(e.n, ":  ", e._parent.n)
            else:
                print(e.n, ":  ", None)
        return vv, cyc_d

def adjacency_list(graph_str):
    Vr.ct_str(graph_str)
    return Vr.adj_list()


def adjacency_matrix(graph_str):
    Vr.ct_str(graph_str)
    return Vr.adj_mat()


def bfs_tree(adj_list, start):
    Vr.ct_adj_list(adj_list)
    ret = Vr.bft(Vr.Verts[start])
    Vr.clear()
    return ret

def dfs_tree(adj_list, start):
    Vr.ct_adj_list(adj_list)
    tmp, cyc = Vr.dfs(Vr.Verts[start])
    ret = [None] * Vr.N
    for v in (sorted(tmp, key=lambda k:k.n)):
        if v._parent:
            ret[v.n]=(v._parent.n)
        else:
            ret[v.n]=(v._parent)
    Vr.clear()
    return ret
