from flask import Flask, render_template, request
from twilio.rest import TwilioRestClient
import os

TWILIO_ID = os.environ['TWILIO_ID']
TWILIO_TOKEN = os.environ['TWILIO_TOKEN']
TWILIO_PHONE_NUMBER = os.environ['TWILIO_PHONE_NUMBER']

app = Flask(__name__)
twilio = TwilioRestClient(TWILIO_ID, TWILIO_TOKEN)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/', methods=['POST'])
def send():
	# TODO: input validation
	# TODO: https://www.twilio.com/blog/2012/08/build-a-scheduled-reminder-app-with-twilio-and-ironworker.html
	phone = request.form.get('phone').strip()
	message = request.form.get('message').strip()
	response = twilio.messages.create(body=message, to=phone, from_='+1646-480-2597')
	return render_template('index.html')

if __name__ == '__main__':
	port = int(os.environ.get('PORT', 5000))
	app.run(host='0.0.0.0', port=port, debug=True)