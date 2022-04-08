from matplotlib.font_manager import _Weight
import tensorflow as tf
import pathlib

# Load the MobileNet tf.keras model
model = tf.keras.applications.MobileNetV2(weights = 'imagenet', input_shape = (224, 224, 3))

# Convert the model
converter = tf.lite.TFLiteConverter.from_keras_model(model)
tflite_model = converter.convert()

# Save the model
tflite_model_file = pathlib.Path('/tmp/mobilenet.tflite')
tflite_model_file.write_bytes(tflite_model)