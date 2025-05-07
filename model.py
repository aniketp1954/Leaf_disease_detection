
import numpy as np
from keras.preprocessing import image
from keras.models import load_model
import tensorflow as tf



# Ensure eager execution is enabled
tf.compat.v1.enable_eager_execution()  # Only necessary if using TensorFlow 1.x compatibility mode

# Load the model globally (once, instead of reloading it in each function call)
model = load_model('md.h5', compile=False)

# Class names
class_name = ['Healthy', 'Septoria', 'stripe_rust']

def result_str(img_path):
    # Load and preprocess the image
    test_image = image.load_img(img_path, target_size=(224, 224))
    test_image = image.img_to_array(test_image)
    test_image = np.expand_dims(test_image, axis=0)  # Make it a batch of 1

    # Predict using the pre-loaded model
    result = model.predict(test_image)

    # Return the class with the highest probability
    prediction = class_name[np.argmax(result[0])]
    return prediction
