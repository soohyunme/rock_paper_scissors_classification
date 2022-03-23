from flask import Flask, render_template, request
from werkzeug.utils import secure_filename
import modeling as model

app = Flask(__name__)


@app.route("/")
def main():
    return render_template("new_index.html")


@app.route("/sub", methods=['GET', 'POST'])
def submit():
    if request.method == "POST":
        f = request.files['file']
        file_path = 'static/uploads/' + secure_filename(f.filename)
        static_path = '/uploads/' + secure_filename(f.filename)
        f.save(file_path)
        predict = model.rps_predict(file_path)

    return render_template("sub.html", img=static_path, ret_=predict)


if __name__ == "__main__":
    app.run(debug=True)

