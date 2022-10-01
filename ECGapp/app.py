from flask import Flask, render_template, request, send_file, flash, redirect
from flask_restful import Resource, Api
from werkzeug.utils import secure_filename
from ECGapp import modelHandling
from ECGapp import modelHandling1
import json

app = Flask(__name__)
api = Api(app)


@app.route('/')
def HomePage():
    return render_template('/index.html')


@app.route('/upload')
def opening_Page():
    return render_template('/upload1.html')


@app.route('/uploader', methods=['GET', 'POST'])
def uploader():
    if request.method == 'POST':
        f = request.files['file']
        f.save(secure_filename(f.filename))
        # output, pictures_name = modelHandling.give_prediction(f.filename, 'ECGmodel.h5')
        # print(pictures_name)
        _, all_data = modelHandling1.give_prediction(f.filename, 'ECGmodel.h5')

        # return render_template('/download.html',results=pictures_name,tables=[output.to_html(classes='data')], titles=output.columns.values)
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
            output, pictures_name = modelHandling1.give_prediction(f.filename, 'ECGmodel.h5')
            print(pictures_name)
            # output, _ = modelHandling1.give_prediction(f.filename, 'ECGmodel.h5')

            return render_template('/download.html', results=pictures_name, tables=[output.to_html(classes='data')],
                                   titles=output.columns.values)
            # return output.to_json()
        else:
            return json.dumps({'value': 'Not the right file format'})


api.add_resource(Uploader1, '/upload1')

if __name__ == '__main__':
    app.run()
