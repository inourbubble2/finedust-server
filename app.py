import csv

from werkzeug.exceptions import BadRequest

from helper import get_string_param, get_now_datetime

from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
model = None
CORS(app)


@app.route('/pm')
def get_pm():
    now_year, now_month, now_day, now_hour = get_now_datetime()

    year = get_string_param('year', now_year)
    month = get_string_param('month', now_month)
    day = get_string_param('day', now_day)
    hour = get_string_param('hour', now_hour)
    print(year, month, day)

    try:
        file = open('static/' + year + '-intg.csv')
    except:
        return "File Not Found", 400

    reader = csv.reader(file)
    lines = list(reader)[1:]
    pm = {}
    for line in lines:
        location, y, m, d, h, pm10 = line[0], line[1], line[2], line[3], line[4], line[9]
        time = y + '-' + m.zfill(2) + '-' + d.zfill(2) + ' ' + h + ':00'
        if time in pm:
            pm[time][location] = pm10
        else:
            temp = {location: pm10}
            pm[time] = temp
    datetime = year + '-' + month.zfill(2) + '-' + day.zfill(2) + ' ' + hour + ':00'

    try:
        pm_result = pm[datetime]
    except:
        return "Wrong Parameter", 400

    result = {'pm_result': pm_result,
              'year': year,
              'month': month,
              'day': day,
              'hour': hour}
    return result


def load_model():
    global model
    # TODO: define model =


@app.route('/predict', methods=["GET"])
def predict():
    year = request.args.get('year')
    month = request.args.get('month')
    day = request.args.get('day')
    time = request.args.get('time')
    if not (year and month and day and time):
        raise BadRequest

    # TODO: load prediction from model

    return jsonify({
        'date': year + month + day + time,
        'result': {

        }
    })


if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)
