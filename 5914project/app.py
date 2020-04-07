from flask import Flask, render_template
import json
from ibm_watson import AssistantV2
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator, BasicAuthenticator

app = Flask(__name__)

authenticator = IAMAuthenticator('JE-aM2ut2o22Ky_2WdQmEgAnMwEgIqBgmh1Eipjw2pm4')

assistant = AssistantV2(
    version='2020-02-05',
    authenticator=authenticator
)


# replace url

assistant.set_service_url('https://api.us-south.assistant.watson.cloud.ibm.com')

assistant_idd = 'ebaf838c-1efe-4137-8f08-470f2526aa44'

# create session.
session_idd  = assistant.create_session(
        assistant_id=assistant_idd
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

<<<<<<< HEAD
@app.route('/p')
def presonality():
    return render_template('personality.html')
=======
@app.route('/test')
def test():
    return render_template('test.html')
>>>>>>> 2bf872495553ad498e71895d005d0797c247ebef

# def begin():
#     global session_idd
#     session_idd = assistant.create_session(
#         assistant_id=assistant_idd
#     ).get_result()['session_id']
    


@app.route('/send_message/<message>')
def send_message(message):
    response = assistant.message(
        assistant_idd,
        session_idd,
        input={
            'message_type': 'text',
            'text': str(message)
        }
    ).get_result()
    return json.dumps(response)

@app.route('/submit/<answer>')
def submit(answer):
    extroversion = 20 + int(answer[0]) - int(answer[5]) + int(answer[10]) - int(answer[15]) + int(answer[20]) - int(answer[25]) + int(answer[30]) - int(answer[35]) + int(answer[40]) - int(answer[45])
    agreeableness = 14 - int(answer[1]) + int(answer[6]) - int(answer[11]) + int(answer[16]) - int(answer[21]) + int(answer[26]) - int(answer[31]) + int(answer[36]) + int(answer[41]) + int(answer[46])
    conscientiousness = 14 + int(answer[2]) - int(answer[7]) + int(answer[12]) - int(answer[17]) + int(answer[22]) - int(answer[27]) + int(answer[32]) - int(answer[37]) + int(answer[42]) + int(answer[47])
    neuroticism = 38 - int(answer[3]) + int(answer[8]) - int(answer[13]) + int(answer[18]) - int(answer[23]) - int(answer[28]) - int(answer[33]) - int(answer[38]) - int(answer[43]) - int(answer[48])
    openness = 8 + int(answer[4]) - int(answer[9]) + int(answer[14]) - int(answer[19]) + int(answer[24]) - int(answer[29]) + int(answer[34]) + int(answer[39]) + int(answer[44]) + int(answer[49])
    scores = [float(extroversion)/40.0, float(agreeableness)/40.0, float(extroversion)/40.0, float(conscientiousness)/40.0, float(neuroticism)/40.0,float(openness)/40.0]
    return "calulation complete"

'''
#methods to send message and get the response
@app.route('/send_message/<message>')
def send_message(message):

'''

if __name__ == '__main__':
    app.run(debug=True)
