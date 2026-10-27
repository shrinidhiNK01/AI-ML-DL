import tensorflow as tf

data = tf.constant([-1.0, 2.0, -3.0, 4.0])  # use floats for trigonometric ops

print(tf.maximum(data))
print(tf.minimum(data))
print(tf.reduce_min(data))
print(tf.reduce_max(data))
print(tf.reduce_mean(data))

print(tf.abs(data))              # absolute values
# tf.acos() and tf.asin() need values between -1 and 1, so we’ll use a safe tensor
limited_data = tf.constant([-1.0, -0.5, 0.5, 1.0])
print(tf.acos(limited_data))     # inverse cosine
print(tf.asin(limited_data))     # inverse sine

print(tf.square(data))           # squares each element
print(tf.__version__)            # show TensorFlow version (no brackets!)
print(tf.reduce_sum(data))       # sum of all elements

# tf.add() requires two tensors — not one.
# For example, add data to itself:
print(tf.add(data, data))
print(tf.subtract(data, data))
print(tf.multiply(data, data))
print(tf.divide(data, data))

# Sort indices of data in ascending order
print(tf.argsort(data))
print(tf.argmax(data))
print(tf.argmin(data))

# tf.concat() requires a list of tensors and an axis to concatenate along
# Example: concatenating data with itself along axis 0
print(tf.concat([data, data], axis=0))

data2=tf.constant([[-2.25+4.75j],[-3+45j]])  #Complex Method
print(tf.abs(data2))


x=tf.constant([1,2,3,4,5])
y=tf.constant([6,7,8,9,10])

print(tf.equal(x,y))
print(tf.pow(x,y))
print(tf.sigmoid(x))
print(tf.top_k(x))
print(tf.linalg.matmul(x ))
print(tf.transpose(x))
