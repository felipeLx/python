# post trainning quantization example
import tensorflow as tf

saved_model_dir = '/tmp/saved_model'
converter = tf.lite.TFLiteConverter.from_saved_model(saved_model_dir)
converter.optimizations = [tf.lite.Optimize.OPTIMIZE_FOR_SIZE]
tflite_quant_model = converter.convert()

# define the generator
def generator():
    data = tfds.load()
    for _ in range(num_calibration_steps):
        image, = data.take(1)
        yield [image]

converter = tf.lite.TFLiteConverter.from_saved_model(saved_model_dir)

# set the optimization model
converter.optimizations = [tf.lite.Optimize.DEFAULT]

# pass the representative dataset to converter
converter.representative_dataset = tf.lite.RepresentativeDataset(generator)

# restricting supported target op specification to INT8
converter.target_spec.supported_ops = [tf.lite.OpsSet.TFLITE_BUILTINS_INT8]