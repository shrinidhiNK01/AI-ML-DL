# Graphs are an essential data structure.
# adjecency matrix
import numpy as np
from scipy.sparse import csr_matrix
from scipy.sparse.csgraph import connected_components
arr = np.array([
  [0, 1, 2],
  [1, 0, 0],
  [2, 0, 0]
])
mat=csr_matrix(arr)
print(connected_components(mat))

# djkstra algorithm to find positive shortest path
import numpy as np
from scipy.sparse import csr_matrix
from scipy.sparse.csgraph import dijkstra
arr = np.array([
  [0, 1, 2],
  [1, 0, 0],
  [2, 0, 0]
])
mat=csr_matrix(arr)
print(dijkstra(mat,return_predecessors=True,indices=0))

# Use the floyd_warshall() method to find shortest path between all pairs of elements.
from scipy.sparse.csgraph import floyd_warshall
arr = np.array([
  [0, 1, 2],
  [1, 0, 0],
  [2, 0, 0]
])
mat=csr_matrix(arr)
print(floyd_warshall(mat,return_predecessors=True))

# The bellman_ford() method can also find the shortest path between all pairs of elements, but this method can handle negative weights as well.
print("```````````````````````````````````````````")
from scipy.sparse.csgraph import bellman_ford
arr = np.array([
  [0, -1, 2],
  [1, 0, 0],
  [2, 0, 0]
])
newarr=csr_matrix(arr)
print(bellman_ford(newarr,return_predecessors=True,indices=0))
'''The depth_first_order() method returns a depth first traversal from a node.

This function takes following arguments:

the graph.
the starting element to traverse graph from.'''
from scipy.sparse.csgraph import depth_first_order
arr = np.array([
  [0, 1, 0, 1],
  [1, 1, 1, 1],
  [2, 1, 1, 0],
  [0, 1, 0, 1]
])
newarr=csr_matrix(arr)
print(depth_first_order(newarr,1))

'''The breadth_first_order() method returns a breadth first traversal from a node.

This function takes following arguments:

the graph.
the starting element to traverse graph from.'''
from scipy.sparse.csgraph import breadth_first_order
arr = np.array([
  [0, 1, 0, 1],
  [1, 1, 1, 1],
  [2, 1, 1, 0],
  [0, 1, 0, 1]
])
newarr=csr_matrix(arr)
print(breadth_first_order(newarr,1))