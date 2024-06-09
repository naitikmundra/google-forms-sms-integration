#A post request recieving backend, made with python, just host the app(on pythonanywhere ie FREE, etc) and add its link + /webhook to the url in Code.gs file.

from flask import Flask, request, jsonify

app = Flask(__name__)
def response(contact):
    user_mobile_no = contact
    #Send sms to user_mobile_no
    pass
    
@app.route('/webhook', methods=['POST'])
def webhook():
    if request.method == 'POST':
        data = request.json
        print(f"Received data: {data}")
        response = data['message'][0] #Change 0 according to  the question no. for contact number in form.
        sendsms(response)
        # Do something with the data here, e.g., store it in a database
        return jsonify({'status': 'successfully', 'data': "sent sms"}), 200
    else:
        return jsonify({'status': 'failure', 'message': 'Invalid request method'}), 400

