#import libraries
from flask import Flask, request, jsonify, render_template
from faker import Faker
from twilio.jwt.access_token import AccessToken
from twilio.jwt.access_token.grants import SyncGrant
app = Flask(__name__)
fake = Faker()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/token')
def generate_token():
    TWILIO_ACCOUNT_SID = 'AC0510da1e6027d822ad4bbde1802260e3'
    TWILIO_SYNC_SERVICE_SID = 'IS1f9238929f4ee43daff3a2a86bfb9fbe'
    TWILIO_API_KEY = 'SK88482b13525fc4030dc005d8a2d97d2e'
    TWILIO_API_SECRET = 'rRgJWaj1AI6RQBp1kwxUbkCk4N4UN7fU'

    username = request.args.get('username', fake.username())

    token = AccessToken(TWILIO_ACCOUNT_SID, TWILIO_API_KEY, TWILIO_API_SECRET, identify = username)

    sync_grant_access = SyncGrant(TWILIO_SYNC_SERVICE_SID)
    token.add_grant(sync_grant_access)
    return jsonify(identity = username, token = token.to_jwt().decode())

if __name__ == "__main__":
    app.run()