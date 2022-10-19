from flask import Flask, render_template, request, send_file, flash, redirect
from flask_restful import Resource, Api
from werkzeug.utils import secure_filename
import modelHandling1
import json

app = Flask(__name__)
api = Api(app)


@app.route('/')
def opening_Page():
    return render_template('/upload1.html')


@app.route('/uploader', methods=['GET', 'POST'])
def uploader():
    if request.method == 'POST':
        f = request.files['file']
        f.save(secure_filename(f.filename))
        _, all_data = modelHandling1.give_prediction(f.filename, 'Models/ECGModelsmall.pkl')
        print(all_data)
        return render_template('/download1.html', allData=all_data)


@app.route('/download')
def downloader():
    filename = 'output.csv'
    return send_file(secure_filename(filename))


def allowed_file(filename):
    Allowed_extensions = ['csv']
    if filename.split('.')[1] in Allowed_extensions:
        return True
    else:
        return False


class Uploader1(Resource):
    def post(self):

        if 'file' not in request.files:
            return json.dumps({'value': 'Not file part'})

        f = request.files['file']
        if f.filename == '':
            return json.dumps({'value': 'No file'})

        if f and allowed_file(f.filename):
            f.save(secure_filename(f.filename))

            output, _ = modelHandling1.give_prediction(f.filename, 'Models/ECGModelsmall.pkl')

            return output.to_json()
        else:
            return json.dumps({'value': 'Not the right file format'})


api.add_resource(Uploader1, '/upload1')

if __name__ == '__main__':
    app.run()

