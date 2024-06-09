#A post request recieving backend, made with python, just host the app(on pythonanywhere ie FREE, etc) and add its link + /webhook to the url in Code.gs file.

from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/webhook', methods=['POST'])
def webhook():
    if request.method == 'POST':
        data = request.json
        print(f"Received data: {data}")
        # Do something with the data here, e.g., store it in a database
        return jsonify({'status': 'successfully', 'data': data}), 200
    else:
        return jsonify({'status': 'failure', 'message': 'Invalid request method'}), 400

