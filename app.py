from flask import Flask, render_template, request
from werkzeug.utils import secure_filename
import modeling as ml
import tensorflow as tf
import numpy as np
import rps_battle

model = tf.keras.models.load_model('MobileNet_Colab.h5')
class_names = {0: 'paper', 1: 'rock', 2: 'scissor'}

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "GET":
        return render_template("index.html")

    if request.method == "POST":
        f = request.files['imageFile']
        if secure_filename(f.filename) == '' or secure_filename(f.filename)[-4:] not in ['.jpg', '.png']:
            return render_template("index.html", error=404)
        file_path = 'static/images/' + secure_filename(f.filename)
        f.save(file_path)
        probability = ml.rps_predict(file_path, model)
        user_str = class_names[np.argmax(probability)]
        com, com_path, result = rps_battle.checkWin(np.argmax(probability))
        com_str = class_names[com]
        move = 'Battle'
        return render_template("index.html", img=file_path, ret_=user_str, com=com_str, com_path=com_path,
                               result=result, move=move)


if __name__ == "__main__":
    app.run(debug=True)
