from flask import Flask
from flask_cors import CORS
import csv

app = Flask(__name__)
CORS(app)


@app.route('/')
def hello_world():  # put application's code here
    file = open('static/2010.csv')
    reader = csv.reader(file)
    lines = list(reader)
    temp_str = str(lines[:10])
    return temp_str


if __name__ == '__main__':
    app.run()