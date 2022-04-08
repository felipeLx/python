import tensorflow as tf

# Load the MobileNet tf.keras model
model = tf.keras.applications.MobileNetV2(weights = 'imagenet', input_shape = (224, 224, 3))

# Get the concrete function from the Keras model
run_model = tf.function(lambda x: model(x))

# Save the concrete function
concrete_func = run_model.get_concrete_function(tf.TensorSpec(model.inputs[0].shape, model.inputs[0].dtype))

# Save the model
converter = tf.lite.TFLiteConverter.from_concrete_functions([concrete_func])
tflite_model = converter.convert()

"""
We can use the command line to convert the model to a tflite file.
!usr/bin/env bash

# saving from a SavedModel
tflite_convert --output_file=model.tflite --saved_model_dir=/tmp/saved_model

# saving from a Keras model
tflite_convert --output_file=model.tflite --keras_model_file=model.h5
"""