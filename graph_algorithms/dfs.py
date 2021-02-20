class DFSResult(object):
    def __init__(self):
        self.parent = {}
        self.start_time = {}
        self.finish_time = {}
        self.edges = {}
        self.order = []
        self.t = 0

def dfs(g):
    r = DFSResult()
    for v in g.itervertices():
        if v not in r.parent:
            dfs_visit(g, v, r)
    return r

def dfs_visit(g, v, r, parent=None):
    r.parent[v] = parent
    r.t += 1
    r.start_time[v] = r.t
    if parent:
        r.edges[(parent, v)] = 'tree'

    for u in g.neighbors(v):
        if u not in r.parent:
            dfs_visit(g, u, r, v)
        elif u not in r.finish_time:
            r.edges[(v, u)] = 'back'
        elif r.start_time[v] < r.start_time[u]:
            r.edges[(v, u)] = 'forward'
        else:
            r.edges[(v, u)] = 'cross'
    r.t += 1
    r.finish_time[v] = r.t
    r.order.append(v)