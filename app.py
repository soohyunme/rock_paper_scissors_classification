from flask import Flask, render_template, request
from werkzeug.utils import secure_filename
import modeling as model
import os

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "GET":
        return render_template("index.html")

    if request.method == "POST":
        print(type(request))
        f = request.files['imageFile']
        file_path = 'static/uploads/' + secure_filename(f.filename)
        static_path = '/uploads/' + secure_filename(f.filename)
        f.save(file_path)
        predict = model.rps_predict(file_path)
        return render_template("index.html", img=static_path, ret_=predict)


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=int(os.environ.get("PORT",5000)))



