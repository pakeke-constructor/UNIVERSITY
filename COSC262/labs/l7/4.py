


import datetime

def ptime(string):
    sp = string.split(":")
    return int(sp[0])*(60**2) + int(sp[1])*60 + int(sp[2])



def paz_input(st):
    'returns list of (end, id) of talks from a str.'
    lis = []
    for s in st.split("\n"):
        if s:
            splt = s.split("\t")
            while '' in splt:
                splt.remove('')
            lis.append((splt[0], ptime(splt[2]), ptime(splt[-1]) + ptime(splt[2])))
    return lis


def paz_show_input(lis):
    ret = []
    for id, start, rtime in lis:
        ret.append((id, start, start+rtime))
    return ret


def greedy(lis):
    # takes (id, start, end)
    time = -float('inf')

    takes = []
    for idd, start, end in sorted(lis, key=lambda x:x[-1]):
        if time <= start:
            takes.append(idd)
            time = end
    return takes


def print_shows(inp):
    shows = greedy(paz_show_input(inp))
    for id in shows:
        for (iid, start, rtime) in inp:
            if id == iid:
                print(iid, start, start + rtime)




u='''\
19	MarleneMckeever	09:20:00	00:10:00
3	LateshaLheureux	09:11:00	00:25:00
16	KeelyArboleda	09:31:00	00:15:00
103	JaneeJuarbe	11:02:00	00:20:00
81	ToccaraTussey	10:29:00	00:54:00
27	MichaelPotrzebie 	11:15:00	00:17:00
100	WinstonSwett	10:29:00	01:17:00
11	NidiaNowlin	11:18:00	00:44:00
92	LouraMancia	11:58:00	00:31:00
93	RockyRoiger	12:04:00	00:32:00
205	TowandaKinsel	12:42:00	00:07:00
6	RuthRister	13:24:00	00:06:00
24	IldaInabinet	12:42:00	01:50:00
159	OrvalObert	14:40:00	00:16:00
15	ArieCarabello	14:50:00	00:23:00
1	AnibalBrouwer	14:51:00	00:22:00
99	JeremiahBobb	14:36:00	00:43:00
77	RickRemus	15:15:00	00:09:00
5	PetraDimarco	15:34:00	00:20:00
'''


# The example from the lecture notes
print_shows([
    ('a', 0, 6),
    ('b', 1, 3),
    ('c', 3, 2),
    ('d', 3, 5),
    ('e', 4, 3),
    ('f', 5, 4),
    ('g', 6, 4), 
    ('h', 8, 3)])


print(list(map(lambda x:int(x),greedy(paz_input(u)))))
