#A post request recieving backend, made with python, just host the app(on pythonanywhere ie FREE, etc) and add its link + /webhook to the url in Code.gs file.

from flask import Flask, request, jsonify
import os
from twilio.rest import Client
app = Flask(__name__)
def sendsms(contact):
    user_mobile_no = contact
    # Download the helper library from https://www.twilio.com/docs/python/install
    # Find your Account SID and Auth Token at twilio.com/console
    # and set the environment variables. See http://twil.io/secure
    account_sid = os.environ['TWILIO_ACCOUNT_SID']
    auth_token = os.environ['TWILIO_AUTH_TOKEN']
    client = Client(account_sid, auth_token)
    
    message = client.messages \
                    .create(
                         body="Thanks for submitting the google form",
                         from_='+15017122661',
                         to='contact'
                     ) 
    #Chekout https://www.twilio.com/docs/messaging/quickstart/python for more details and docs
    
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

