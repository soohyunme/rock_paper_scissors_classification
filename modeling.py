import cv2


def rps_predict(file_path, model):

    # Define Hyperparameter
    IMG_WIDTH = 112
    IMG_HEIGHT = 112

    src_img = cv2.imread(file_path, cv2.IMREAD_COLOR)

    dst_img = cv2.cvtColor(src_img, cv2.COLOR_BGR2RGB)
    dst_img = cv2.resize(dst_img, dsize=(IMG_WIDTH, IMG_HEIGHT))
    dst_img = dst_img / 255.0

    x_data = dst_img.reshape(-1, IMG_WIDTH, IMG_HEIGHT, 3)

    return model.predict(x_data)

