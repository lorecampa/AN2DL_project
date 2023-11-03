import os
import tensorflow as tf
import numpy as np
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.applications.convnext import preprocess_input

class model:
    def __init__(self, path):
        self.models = [0]*3
        self.models[1] = tf.keras.models.load_model(os.path.join(path, 'SubmissionModel_1'))
        self.models[2] = tf.keras.models.load_model(os.path.join(path, 'SubmissionModel_2'))
        self.models[3] = tf.keras.models.load_model(os.path.join(path, 'SubmissionModel_3'))

    def predict(self, X):

        results = np.zeros((X.shape[0], 8))


        for j in range(3):
            results = results + models[j].predict(X)

        out = np.argmax(results, axis=1)

        return out
