import tensorflow as tf
one=tf.constant(4)
two=tf.constant([1,2,3,4,5] ,dtype=tf.float32)
# two_true=tf.constant([1,2,3,4,5] ,dtype=tf.bool)
casting=tf.cast(two,dtype=tf.int32)

print(two)
# print(two_true)
print(casting)

three=tf.constant([[1,2,3],[4,5,6],[7,8,9]])
four = tf.constant([
    [
        [1,2,3,4],
        [5,6,7,8],
        [9,10,11,12]
    ],
    [
        [13,14,15,16],
        [17,18,19,20],
        [21,22,23,24]
    ]
])

five=tf.constant([
[
    [
        [1,2,3,4],
        [5,6,7,8]
    ],
    [
        [9,10,11,12],
        [13,14,15,16]
    ]

],
[
    [
        [17,18,19,20],
        [21,22,23,24]
    ],
    [
        [25,26,27,28],
        [29,30,31,32]
    ]
]

])
print(four.shape)
print(four.ndim)
print(five.shape)
print(five.ndim)
print(tf.rank(five))


# Numpy array into tensors
import numpy as np
x=np.array([1,2,3,4,5] )
six=tf.convert_to_tensor(x)
print(six)

seven=tf.eye(
    num_rows=4,
    num_columns=4,
    dtype=tf.float32,
    name="shrinidhi",
    batch_shape=[3,4]
)
print(seven)
print(3*seven)


eight=tf.fill(
    [4,5],5
)
print(eight)

nine=tf.ones(
    [3,4],
    dtype=tf.float32
)
print(nine)

ten=tf.ones_like(eight)
print(ten)

eleven=tf.zeros(
    [3,2]
)
print(eleven)
print(eleven.shape)

twelve=tf.random.normal(
    [3,5],
    mean=  100,
    stddev=1.0
)
print(twelve)
thirteen=tf.random.uniform(
    [5,5],
    minval=  0,
    maxval=100
)
print(thirteen)

tf.random.set_seed(5)
print(tf.random.uniform(shape=[3,],maxval=5,seed=10))