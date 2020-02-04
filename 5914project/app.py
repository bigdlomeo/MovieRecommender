from flask import Flask, render_template
import json
from ibm_watson import AssistantV2
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator, BasicAuthenticator

app = Flask(__name__)

authenticator = BasicAuthenticator('clockworkdelphine@hotmail.com', 'Kurogane970426')

assistant = AssistantV2(
    version='2019-02-28',
    authenticator=authenticator
)

# replace url

assistant.set_service_url('https://gateway.watsonplatform.net/assistant/api')

assistant_id = 'ad14b037-49bc-4fdb-9025-3a40584574b7'

# create session.
session_id = assistant.create_session(
    assistant_id=assistant_id
).get_result()['session_id']

'''
# Set up Assistant service.
authenticator = IAMAuthenticator('{apikey}') # replace with API key
service = AssistantV2(
    version = '2019-02-28',
    authenticator = authenticator
)
assistant_id = '{assistant_id}' # replace with assistant ID

# Create session.
session_id = service.create_session(
    assistant_id = assistant_id
).get_result()['session_id']

'''


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/movie')
def movie():
    return render_template('page.html')


@app.route('/pred')
def predict():
    return render_template('prediction.html')


@app.route('/send_message/<message>')
def send_message(message):
    response = assistant.message(
        assistant_id,
        session_id,
        input={
            'message_type': 'text',
            'text': str(message)
        }
    ).get_result()


assistant.delete_session(
    assistant_id=assistant_id,
    session_id=session_id

)
'''
#methods to send message and get the response
@app.route('/send_message/<message>')
def send_message(message):

'''

if __name__ == '__main__':
    app.run(debug=True)
