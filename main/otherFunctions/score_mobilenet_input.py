import numpy as np
import os
from keras.models import Model
from keras.layers import Dense, Dropout
from keras.applications.mobilenet import MobileNet
from keras.applications.mobilenet import preprocess_input
from keras.preprocessing.image import load_img, img_to_array
import tensorflow as tf
from .utils.score_utils import mean_score, std_score

def assessPicture(imgPath):
    # 利用相對路徑取圖片路徑
    imgPath = os.path.join(os.path.abspath(os.path.join(os.getcwd(),"media")), imgPath)
    with tf.device('/CPU:0'):
        base_model = MobileNet((None, None, 3), alpha=1, include_top=False, pooling='avg', weights=None)
        x = Dropout(0.75)(base_model.output)
        x = Dense(10, activation='softmax')(x)
        model = Model(base_model.input, x)
        model.load_weights(os.path.abspath(os.path.join(os.path.join(os.getcwd(),"main/otherFunctions/weights/mobilenet_weights_others.h5"))))
        img = load_img(imgPath, target_size=(224,224))
        x = img_to_array(img)
        x = np.expand_dims(x, axis=0)
        x = preprocess_input(x)
        scores = model.predict(x, batch_size=1, verbose=0)[0]
        mean = mean_score(scores)
        std = std_score(scores)

        print()
        print("Evaluating : ", imgPath)
        print("NIMA Score : %0.3f +- (%0.3f)" % (mean, std))
        print()
        mean_update = -17 + 4.5*mean
        if mean_update > 10:
            mean_update = 10
        elif mean_update < 1:
            mean_update = 1
        return round(mean_update,1)

