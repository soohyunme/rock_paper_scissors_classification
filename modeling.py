import tensorflow as tf
import numpy as np
import cv2
import os


def rps_predict(file_path):

    # Define Hyperparameter
    IMG_WIDTH = 112
    IMG_HEIGHT = 112

    src_img = cv2.imread(file_path, cv2.IMREAD_COLOR)

    dst_img = cv2.cvtColor(src_img, cv2.COLOR_BGR2RGB)
    dst_img = cv2.resize(dst_img, dsize=(IMG_WIDTH, IMG_HEIGHT))
    dst_img = dst_img / 255.0

    x_data = dst_img.reshape(-1, IMG_WIDTH, IMG_HEIGHT, 3)

    model = tf.keras.models.load_model('MobileNet_Colab.h5')

    class_names = {0: 'paper', 1: 'rock', 2: 'scissor'}
    ret_ = class_names[np.argmax(model.predict(x_data))]

    return ret_
