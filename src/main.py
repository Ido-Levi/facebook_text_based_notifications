import os
import json

from flask import Flask, request, Response

app = Flask(__name__)

# token to verify that this bot is legit
verify_token = os.getenv('VERIFY_TOKEN', None)
# token to send messages through facebook messenger
access_token = os.getenv('ACCESS_TOKEN', None)


@app.route('/webhook', methods=['GET'])
def webhook_verify():
    if request.args.get('hub.verify_token') == verify_token:
        return request.args.get('hub.challenge')
    return "Wrong verify token, try another mate"


@app.route('/webhook', methods=['POST'])
def webhook_action():
    data = json.loads(request.data.decode('utf-8'))
    print('heyo fellas, we got a message from da facebook')
    print(data)
    for entry in data['entry']:
        user_message = entry['messaging'][0]['message']['text']
        user_id = entry['messaging'][0]['sender']['id']
        print(f'user_id: {user_id}')
        print(f'user_message: {user_message}')
    return Response(response="EVENT RECEIVED",
                    status=200)


@app.route('/', methods=['GET'])
def index():
    return "Hello there, this is a telegram bot to get notifications " \
           "when shit comes up in FB groups, read da docs pho more, esse."


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
