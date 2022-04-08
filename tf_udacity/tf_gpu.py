import tensorflow as tf

gpu = tf.config.list_physical_devices('GPU')
print(gpu)