from flask import Flask, render_template, request
import os

app = Flask(__name__)

UPLOAD_FOLDER = "dataset"
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/upload", methods=["POST"])
def upload():
    if 'image' not in request.files:
        return "❌ No file part"

    file = request.files['image']

    if file.filename == '':
        return "❌ No selected file"

    if file:
        os.makedirs(app.config["UPLOAD_FOLDER"], exist_ok=True)
        filepath = os.path.join(app.config["UPLOAD_FOLDER"], file.filename)
        file.save(filepath)

        return render_template("index.html", result=result, filename=file.filename)

    return "❌ Upload failed"

if __name__ == "__main__":
    app.run(debug=True)