from flask import Flask
from flask import request
from flask import Response
from collections import OrderedDict
import werkzeug
import function


app = Flask(__name__)


@app.route("/", methods=['POST'])
def index():
    # Ensure student number and student name are set
    if request.form.get('studentNumber') == "" or request.form.get('studentName') == "":
        @app.errorhandler(werkzeug.exceptions.BadRequest)
        def handle_bad_request(e):
            return 'Bad request! Ensure student number and name are entered.', 400
    else:
        input = OrderedDict()

        input['Student Number'] = request.form.get('studentNumber')
        input['Student Name'] = request.form.get('studentName')
        input['Programming'] = request.form.get('programming')
        input['Computing foundations'] = request.form.get(
            'computingFoundations')
        input['Databases'] = request.form.get('databases')
        input['Software Engineering'] = request.form.get(
            'softwareEngineering')
        input['Web Development'] = request.form.get('webDevelopment')
        input['Data Analysis'] = request.form.get('dataAnalysis')
        input['User Experience'] = request.form.get('userExperience')
        input['Cloud Computing'] = request.form.get('cloudComputing')

        r = function.createPDF(input)

        return r


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
