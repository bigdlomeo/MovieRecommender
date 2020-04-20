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
    i = 0
    alldata = []
    while i <5:
        data = []
        print(i)
        if "id" in movies_return["results"][i]:
            data.append("https://www.imdb.com"+movies_return["results"][i]["id"])
        else:
            data.append("")
        if "image" in movies_return["results"][i]:
            data.append(movies_return["results"][i]["image"]["url"])
        else:
            data.append("")
        if "title" in movies_return["results"][i]:
            data.append( movies_return["results"][i]["title"])
        else:
            data.append("")
        data.append( "")
        if "year" in movies_return["results"][i]:
            data.append(movies_return["results"][i]["year"])
        else:
            data.append("")
        if "runningTimeInMinutes" in movies_return["results"][i]:
            data.append(movies_return["results"][i]["runningTimeInMinutes"])
        else:
            data.append("")
        if "titleType" in movies_return["results"][i]:
            data.append(movies_return["results"][i]["titleType"])
        else:
            data.append("")
        data.append( "")
        data.append("")
        data.append("")
        data.append("")
        alldata.append(data)
        i=i+1
    return alldata
