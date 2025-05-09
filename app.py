from flask import Flask, jsonify, send_from_directory
import pandas as pd
import time
from datetime import datetime
import os

app = Flask(__name__)
start_time = time.time()

@app.route('/data')
def get_data():
    ts = time.time()
    date = datetime.fromtimestamp(ts).strftime("%d-%m-%Y")
    timestamp = datetime.fromtimestamp(ts).strftime("%H:%M-%S")
    count = int((ts - start_time) // 2)

    # FizzBuzz logic
    if count == 0:
        status = "Count is zero"
    elif count % 3 == 0 and count % 5 == 0:
        status = "FizzBuzz"
    elif count % 3 == 0:
        status = "Fizz"
    elif count % 5 == 0:
        status = "Buzz"
    else:
        status = f"Count: {count}"

    # Load attendance CSV
    filepath = f"Attendance/Attendance_{date}.csv"
    if os.path.exists(filepath):
        df = pd.read_csv(filepath)
        data = df.to_dict(orient="records")
        columns = df.columns.tolist()
    else:
        data = []
        columns = []

    return jsonify({
        "status": status,
        "data": data,
        "columns": columns,
        "timestamp": timestamp
    })

@app.route('/')
def index():
    return send_from_directory('.', 'index.html')

if __name__ == '__main__':
    app.run(debug=True)
