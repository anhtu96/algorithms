from dfs import *
def topological_sort(g):
    dfs_result = dfs(g)
    dfs_result.order.reverse()
    return dfs_result.order