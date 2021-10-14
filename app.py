from flask import Flask, request
from flask_cors import CORS
import csv

app = Flask(__name__)
CORS(app)


@app.route('/pm')
def get_past_pm():  # put application's code here
    year = request.args.get('year')
    month = request.args.get('month')
    day = request.args.get('day')
    hour = request.args.get('hour')
    file = open('static/' + year + '.csv')
    reader = csv.reader(file)
    lines = list(reader)[1:]
    pm = {}
    for line in lines:
        location, time, pm10 = line[0], line[1], line[6]
        if time in pm:
            pm[time][location] = pm10
        else:
            temp = {location: pm10}
            pm[time] = temp
    datetime = year + '-' + month.zfill(2) + '-' + day.zfill(2) + ' ' + hour + ':00'
    return pm[datetime]


if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)