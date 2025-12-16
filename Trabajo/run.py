# Search methods

import search
from Trabajo.search import calculate_time

ab = search.GPSProblem('A', 'B'
                       , search.romania)

print(search.breadth_first_graph_search(ab).path())
print(calculate_time("bfs", ab))
#print(search.depth_first_graph_search(ab).path())
#print(search.branch_bound_graph_search(ab).path())
#print(search.underestimation_branch_bound_graph_search(ab).path())

# Result:
# [<Node B>, <Node P>, <Node R>, <Node S>, <Node A>] : 101 + 97 + 80 + 140 = 418
# [<Node B>, <Node F>, <Node S>, <Node A>] : 211 + 99 + 140 = 450