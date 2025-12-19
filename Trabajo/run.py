# Search methods

import search
from Trabajo.search import calculate_time

ab = search.GPSProblem('M', 'F'
                       , search.romania)
print('===BFS===')
print(search.breadth_first_graph_search(ab).path())
print(calculate_time("bfs", ab))
print('===DFS===')
print(search.depth_first_graph_search(ab).path())
print(calculate_time("dfs", ab))
print('===B&B==')
print(search.branch_bound_graph_search(ab).path())
print(calculate_time("bnb", ab))
print('===B&B&H===')
print(search.underestimation_branch_bound_graph_search(ab).path())
print(calculate_time("ubb", ab))
print('===B&B&H sobreestimado===')
print(search.overestimation_branch_bound_graph_search(ab).path())
print(calculate_time("ubbe", ab))

# Result:
# [<Node B>, <Node P>, <Node R>, <Node S>, <Node A>] : 101 + 97 + 80 + 140 = 418
# [<Node B>, <Node F>, <Node S>, <Node A>] : 211 + 99 + 140 = 450