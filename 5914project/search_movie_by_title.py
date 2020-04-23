import http.client
import json
def requestIBMD(word):
    url = "/title/find?q="+word
    conn = http.client.HTTPSConnection("imdb8.p.rapidapi.com")

    headers = {
    'x-rapidapi-host': "imdb8.p.rapidapi.com",
    'x-rapidapi-key': "ecfcd67f29msh1ad906a110869b4p1edd2djsne99126bc2a3b"
    }
    conn.request("GET", "/title/find?q="+word, headers=headers)

    res = conn.getresponse()

    data = res.read()
    #print(data.decode("utf-8"))
    movies_return = json.loads(data.decode("utf-8"))
    print(json.dumps(movies_return, indent=4, sort_keys=True))
    alldata = []
    for movie in movies_return["results"]:
        data = []
        if "id" in movie:
            data.append("https://www.imdb.com"+movie["id"])
        else:
            data.append("")
        if "image" in movie:
            data.append(movie["image"]["url"])
        else:
            data.append("")
        if "title" in movie:
            data.append(movie["title"])
        else:
            data.pop() # rermove image
            data.pop() #remove id
            continue
        if "year" in movie:
            data.append(movie["year"])
        else:
            data.append("")
        if "runningTimeInMinutes" in movie:
            data.append(movie["runningTimeInMinutes"])
        else:
            data.append("")
        if "titleType" in movie:
            data.append(movie["titleType"])
        else:
            data.append("")
        data.append( "")
        data.append("")
        data.append("")
        data.append("")
        data.append("")
        alldata.append(data)
    return alldata
