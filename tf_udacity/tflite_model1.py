from doctest import OutputChecker
import pathlib
import numpy as np
import matplotlib.pyplot as plt
import tensorflow as tf
from tensorflow.keras.models import Model
from tensorflow.keras.layers import Input

# creating a simple keras model
x = [-1, 0, 1, 2, 3, 4]
y = [-3, -1, 1, 3, 5, 7]

model = tf.keras.models.Sequential([tf.keras.layers.Dense(units=1, input_shape=[1])])
model.compile(optimizer='sgd', loss='mean_squared_error')
model.fit(x, y, epochs=200, verbose=1)
# The TensorFlow library was compiled to use AVX instructions, but these aren't available on your machine.

# generate a saved model
export_dir = '/tmp/saved_model/'
tf.saved.model.save(model, export_dir)

# convert the saved model to tflite
converter = tf.lite.TFLiteConverter.from_saved_model(export_dir)
tflite_model = converter.convert()

tflite_model_file = pathlib.Path('/tmp/saved_model/saved_model.tflite')
tflite_model_file.write_bytes(tflite_model)

# initalize the TF Lite interpreter to try it out
interpreter = tf.lite.Interpreter(model_content=tflite_model)
interpreter.allocate_tensors()

input_details = interpreter.get_input_details()
output_details = interpreter.get_output_details()

# test the TF Lite model on random input data
input_shape = input_details[0]['shape']
inputs, outputs = [], []

for _ in range(100):
    input_data = np.array(np.random.random_sample(input_shape), dtype=np.float32)
    interpreter.set_tensor(input_details[0]['index'], input_data)

    interpreter.invoke()
    tflite_results = interpreter.get_tensor(output_details[0]['index'])

    # test TF model on random input data
    tf_results = model(tf.constant(input_data))
    output_data = np.array(tf_results)

    inputs.append(input_data[0][0])
    outputs.append(output_data[0][0])

# vizualize the results
plt.plot(inputs, outputs, 'r')
plt.show()

"""
# download the model
try:
    from google.colab import files
    files.download(tflite_model_file)
except:
    pass
"""