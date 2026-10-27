# Sparse data is data that has mostly unused elements (elements that don't carry any information ).
# It can be an array like this one:
# [1, 0, 2, 0, 0, 3, 0, 0, 0, 0, 0, 0]
# Sparse Data: is a data set where most of the item values are zero.
# Dense Array: is the opposite of a sparse array: most of the values are not zero.
# CSC - Compressed Sparse Column. For efficient arithmetic, fast column slicing.
# CSR - Compressed Sparse Row. For fast row slicing, faster matrix vector products
import numpy as np
from scipy.sparse import csr_matrix 
data=np.array([1,2,3,4,5,6,67,0,0,0,1,1,1,2,2,3,4,5])
print(csr_matrix(data))
# doesn't show 0 data
print(csr_matrix(data).data)    
# counting nonzero
print(csr_matrix(data).count_nonzero())
# remove zero entries from data
print("//////////////////////////////")
hi=csr_matrix(data)
hi.eliminate_zeros()
print(hi)
# Eliminating duplicate entries
print("///////////////////////////////")
hello=csr_matrix(data)
hello.sum_duplicates()
print("duplicate values:",hello)
# convert from csr to csc
newarr=csr_matrix(data).tocsc()
print(newarr)
