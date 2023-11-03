import os
import tensorflow as tf
import numpy as np
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.applications.convnext import preprocess_input

class model:
    def __init__(self, path):
        self.model = tf.keras.models.load_model(os.path.join(path, 'SubmissionModel'))

    def predict(self, X):

        dataset_img_size = (96, 96)

        rot_gen = ImageDataGenerator(rotation_range=180)
        shift_gen = ImageDataGenerator(width_shift_range=0.4)
        height_gen = ImageDataGenerator(height_shift_range=0.4)
        zoom_gen = ImageDataGenerator(zoom_range=0.4)
        flip_gen = ImageDataGenerator(horizontal_flip=True)
        vertical_flip = ImageDataGenerator(vertical_flip=True)
        fill_mode = ImageDataGenerator(fill_mode='reflect')
        
        # Get random transformations        
        rot_ts = [rot_gen.get_random_transform(img_shape=dataset_img_size) for i in range(6)]

        shift_ts = [shift_gen.get_random_transform(img_shape=dataset_img_size) for i in range(6)]
        
        height_ts = [height_gen.get_random_transform(img_shape=dataset_img_size) for i in range(6)]
        
        zoom_ts = [zoom_gen.get_random_transform(img_shape=dataset_img_size) for i in range(6)]
        
        flip_t = flip_gen.get_random_transform(img_shape=dataset_img_size)
        
        vertical_t = vertical_flip.get_random_transform(img_shape=dataset_img_size)
        

        predictions = []

        for x in X:
            x = x.numpy()
            # Apply the transformation
            gen = ImageDataGenerator(fill_mode='reflect', cval=0.)
            x_np =                  np.array([x])
            rotateds =              np.array([gen.apply_transform(x, rot_t) for rot_t in rot_ts])
            whidth_shifteds =       np.array([gen.apply_transform(x, shift_t) for shift_t in shift_ts])
            height_shifteds =       np.array([gen.apply_transform(x, height_t) for height_t in height_ts])
            zoomeds =               np.array([gen.apply_transform(x, zoom_t) for zoom_t in zoom_ts])
            horizontal_flipped =    np.array([gen.apply_transform(x, flip_t)])
            vertical_flipped =      np.array([gen.apply_transform(x, vertical_t)])
        
            x_augmented = np.concatenate([x_np, rotateds, whidth_shifteds, height_shifteds, zoomeds, horizontal_flipped, vertical_flipped])
            
            x_augmented = preprocess_input(x_augmented) 

            preds = self.model.predict(x_augmented)
        
            predictions.append(np.mean(preds, axis=0))

        out = tf.argmax(predictions, axis=-1)

        return out
