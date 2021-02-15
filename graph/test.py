from bfs import *

# test BFS
def print_bfs_result(r):
    print('BFS Result:')
    print('Level: ', r.level)
    print('Parent: ', r.parent)

g = Graph()
g.adj = {
    1: [2, 5],
    2: [1, 3, 4, 5],
    3: [2, 4],
    4: [2, 3, 5],
    5: [1, 2, 4]
}
bfs_result = bfs(g, 1)
print_bfs_result(bfs_result)