from flask import Flask, render_template, request, redirect, url_for
from find_min_std import get_recommend
from movie_detail import Movie
from html import unescape
import json
from ibm_watson import AssistantV2
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator, BasicAuthenticator
from search_movie_by_title import requestIBMD

app = Flask(__name__)

authenticator = IAMAuthenticator('k3AEmH-u5f0HYHSySDDGbWzMvtaA0IqLkanMUVouDmUa')

assistant = AssistantV2(
    version='2020-02-05',
    authenticator=authenticator
)


# replace url

assistant.set_service_url('https://api.us-south.assistant.watson.cloud.ibm.com')

assistant_idd = 'bf5d1798-657f-47be-925f-0d26863c731b'

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

@app.route('/howto')
def howTo():
    return render_template('howto.html')


@app.route('/movie')
def movie():
    return render_template('page.html')

@app.route('/pred', methods=['GET', 'POST'])
def predict():
    data = request.args.get('data')
    if request.method == 'POST' and 'movie_search' in request.form:
        keyword = request.form.get("movie_search")
        movies= requestIBMD(keyword)
        print("from prediction page: ")
        print(movies)
        j = 0
        imdbs = []
        images = []
        titles = []
        synopsises = []
        releasedes = []
        runtimes = []
        genres= []
        languages = []
        actors = []
        creators = []
        directors = []
        while j < 5:
            if sig==1:
                imdbs.append(movies[j][0])
                images.append(movies[j][1])
                titles.append(movies[j][2])
                synopsises.append(movies[j][3])
                releasedes.append(movies[j][4])
                runtimes.append(movies[j][5])
                genres.append(movies[j][6])
                languages.append(movies[j][7])
                actors.append(movies[j][8])
                creators.append(movies[j][9])
                directors.append(movies[j][10])
            j = j+1
        print(titles)
        data = [imdbs, images,titles, synopsises,releasedes, runtimes, genres, languages, actors, creators, directors]
        return render_template('prediction.html', data=data)
    return render_template('prediction.html', data= data)


@app.route('/test')
def test():
    return render_template('test.html')








@app.route('/send_message/<message>')
def send_message(message):
    response = assistant.message(
        assistant_idd,
        session_idd,
        input={
            'message_type': 'text',
            'text': str(message)
        }
    ).get_result()['output']['generic'][0]['text']

    # print(response)
    # return "reponse str,false" if assistant are going to recommend 
    # return "reponse str,true" if assistant just talk e.g : reply to 'how are you? ' ;
    if response[0] == '{':
        return get_movies(response)
    else:
        return response

def get_movies(movies):
    response = "I recommend"
    movies = json.loads(movies)
    for x in movies["courses"]:
        response = response + ", " + x["title"] + " (" + x["released"] + ")"
    return response






@app.route('/p', methods=['GET', 'POST'])
def presonality():
    if request.method == 'POST':
        sig = 0
        #get the data from personality questionaire
        movies = []
        if 'movie_search' in request.form:
            sig = 1
            print("Yes get movie_search")
            keyword = request.form.get("movie_search")
            movies= requestIBMD(keyword)
            print(movies)
        else:
            i = 1
            personality_detail = []
            while i <=50:
                q_result = request.form.get('q'+str(i))
                if q_result == "a":
                    personality_detail.append(1)
                elif q_result == "b":
                    personality_detail.append(2)
                elif q_result == "c":
                    personality_detail.append(3)
                elif q_result == "d":
                    personality_detail.append(4)
                elif q_result == "e":
                    personality_detail.append(5)
                else:
                    personality_detail.append(0)
                i= i+1
            #calculate the big fivepersonality
            j = 0
            pe = 20
            pa = 14
            pc = 14
            pn = 38
            po = 8
            while j < 10:
                pe = pe + ((-1)**(j))* personality_detail[5*j]
                pa = pa + ((-1)**(j+1))*personality_detail[1+5*j]
                pc = pc + ((-1)**(j))* personality_detail[2+5*j]
                pn = pn + ((-1)**(j+1))* personality_detail[3+5*j]
                po = po + ((-1)**(j))* personality_detail[4+5*j]
                j = j +1
            big_five = [po/40, pc/40, pe/40, pa/40, pn/40]
            print("big five are: ", str(big_five))
            movie_detail = get_recommend(big_five, 20)
            #handle movies data and store them into differrent categories
            i = 0
            while i < 20:
                movies.append(Movie(movie_detail[i][1]))
                i = i +1
        j = 0
        imdbs = []
        images = []
        titles = []
        synopsises = []
        releasedes = []
        runtimes = []
        genres= []
        languages = []
        actors = []
        creators = []
        directors = []
        while j < 6:
            if sig==1:
                imdbs.append(movies[j][0])
                images.append(movies[j][1])
                titles.append(movies[j][2])
                synopsises.append(movies[j][3])
                releasedes.append(movies[j][4])
                runtimes.append(movies[j][5])
                genres.append(movies[j][6])
                languages.append(movies[j][7])
                actors.append(movies[j][8])
                creators.append(movies[j][9])
                directors.append(movies[j][10])
            else:
                imdbs.append( "https://usa.newonnetflix.info/info/"+str(movie_detail[j][0]))
                images.append(movies[j].image())
                titles.append(unescape(movies[j].title()))
                synopsises.append(unescape(movies[j].synopsis()))
                releasedes.append(movies[j].released())
                runtimes.append(movies[j].runtime())
                genres.append(unescape(movies[j].genre()))
                languages.append(movies[j].language())
                actors.append(', '.join(map(str, unescape(movies[j].actor()))))
                creators.append(', '.join(map(str, unescape(movies[j].creator()))))
                directors.append(', '.join(map(str, unescape(movies[j].director()))))
            j = j+1
        print(titles)
        data = [imdbs, images,titles, synopsises,releasedes, runtimes, genres, languages, actors, creators, directors ]
        return render_template('prediction.html', data=data)
    return render_template('personality.html')


#def questionnaire():
#    if request.method == 'POST':
#        data = request.form.get('data')
#        return redirect(url_for('pred', data = data))
#    return render_template('temp_questionaire.html')

# def begin():
#     global session_idd
#     session_idd = assistant.create_session(
#         assistant_id=assistant_idd
#     ).get_result()['session_id']



#@app.route('//<message>')
#def send_message(message):
#    response = assistant.message(
#        assistant_idd,
#        session_idd,
#        input={
#            'message_type': 'text',
###    ).get_result()
#    return json.dumps(response)


'''
#methods to send message and get the response
@app.route('/send_message/<message>')
def send_message(message):

'''

if __name__ == '__main__':
    app.run(debug=True)
