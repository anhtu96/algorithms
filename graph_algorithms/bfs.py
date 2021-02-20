from collections import deque

class BFSResult(object):
    def __init__(self):
        self.level = {}
        self.parent = {}

def bfs(g, s):
    """ Queue-based implementation of BFS.

    Args:
    - g: a graph with adjacency list adj s.t g.adj[u] is a list of u's neighbors.
    - s: source vertex.
    """
    r = BFSResult()
    r.parent = {s: None}
    r.level = {s: 0}

    queue = deque()
    queue.append(s)

    while queue:
        u = queue.popleft()
        for n in g.adj[u]:
            if n not in r.level:
                r.parent[n] = u
                r.level[n] = r.level[u] + 1
                queue.append(n)
    return r