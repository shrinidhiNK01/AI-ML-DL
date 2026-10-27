# Spatial data refers to data that is represented in a geometric space.
# A Triangulation of a polygon is to divide the polygon into multiple triangles with which we can compute an area of the polygon.
from scipy.spatial import Delaunay
import numpy as np
import matplotlib.pyplot as plt
points = np.array([
  [2, 4],
  [3, 4],
  [3, 0],
  [2, 2],
  [4, 1]
])
simplices=Delaunay(points).simplices
plt.triplot(points[:,0],points[:,1],simplices )
plt.scatter(points[:,0],points[:,1],color='r')
plt.show()

# A convex hull is the smallest polygon that covers all of the given points.
from scipy.spatial import ConvexHull
points = np.array([
  [2, 4],
  [3, 4],
  [3, 0],
  [2, 2],
  [4, 1]
])
hull=ConvexHull(points).simplices 
plt.scatter(points[:,0],points[:,1])
for i in hull:
    plt.plot(points[i,0],points[i,1],'k-')
plt.show()

# KDTrees are a datastructure optimized for nearest neighbor queries.
