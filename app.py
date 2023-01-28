import os
import torch
import io
from flask import Flask, render_template, send_file
from flask_wtf import FlaskForm
from wtforms import FileField, SubmitField
from werkzeug.utils import secure_filename
from wtforms.validators import InputRequired
from PIL import Image

app = Flask(__name__)
app.config['SECRET_KEY'] = 'supersecretkey'
app.config['UPLOAD_FOLDER'] = 'static/files'

def find_model():
    for f  in os.listdir():
        if f.endswith(".pt"):
            return f
    print("Please make sure that weigth file in project directory!")
    
model_name = find_model()
model =torch.hub.load("WongKinYiu/yolov7", 'custom', model_name)

model.eval()

def get_prediction(img_bytes):
    img = Image.open(io.BytesIO(img_bytes))
    imgs = [img]
    results = model(imgs, size=640)
    return results

class UploadFileForm(FlaskForm):
    file = FileField("File", validators=[InputRequired()])
    submit = SubmitField("Upload File")

@app.route('/', methods=['GET',"POST"])
@app.route('/home', methods=['GET',"POST"])
def home():
    form = UploadFileForm()
    if form.validate_on_submit():
        file = form.file.data # Get the file from form
        fileName = file.filename
        filePath = os.path.join(os.path.abspath(os.path.dirname(__file__)),app.config['UPLOAD_FOLDER'],secure_filename(fileName))
        file.save(filePath)

        with open(filePath, "rb") as image:
            f = image.read()
            img_bytes = bytearray(f)
        results = get_prediction(img_bytes)
        
        imgName = os.path.splitext(fileName)[0]
        results.save(save_dir='static/results/' + imgName)
        relPath = "results/" + imgName + "/image0.jpg"
        return render_template('prediction.html', filePath=relPath, form=form)
    return render_template('index.html', form=form)

if __name__ == '__main__':
    app.run(debug=True)