
import json

#movie_detail = '{"RESULT":{"nfinfo":{"image1":"https://art-s.nflximg.net/118f9/84edf0b82c04ebccc781c0f06123bb318ee118f9.jpg","title":"Pok&eacute;mon the Movie: Diancie and the Cocoon of Destruction","synopsis":"A princess calls upon Ash and his friends to help her find the energy-giving Heart Diamond, save her domain from its enemies and restore her kingdom.","matlevel":"","matlabel":"Suitable for general audiences.","avgrating":"2.969697","type":"movie","updated":"","unogsdate":"2016-02-01 05:04:01","released":"2014","netflixid":"80091264","runtime":"1h16m","image2":"https://art-s.nflximg.net/118f9/84edf0b82c04ebccc781c0f06123bb318ee118f9.jpg","download":"1"},"imdbinfo":{"rating":"5.6","votes":"1031","metascore":"N/A","genre":"Animation, Action, Adventure, Comedy, Family, Fantasy","awards":"1 nomination.","runtime":"76 min","plot":"When Diancie a Pok&eacute;mon said to create diamond travels to find Xerneas to help her make a heart diamond to save her home, Ash, Serena, Clemont and Bonnie help her to be safe on the way from thieves.","country":"Japan","language":"Japanese, English","imdbid":"tt3918368"},"mgname":["Children & Family Movies","Anime","Family Sci-Fi & Fantasy","Family Adventures"],"Genreid":["783","7424","52849","52855"],"people":[{"actor":["Rica Matsumoto","Ikue Ohtani","Haven Paschall","Mayuki Makiguchi","Alyson Leigh Rosenfeld","Mariya Ise","Yuki Kaji","Mike Liscio","Sarah Natochenny","Yuji Ueda","Shinichiro Miki","Ikue Otani","Inuko Inuyama","Megumi Hayashibara"]},{"creator":["Hideki Sonoda","Satoshi Tajiri","Junichi Masuda","Ken Sugimori"]},{"director":["Kunihiko Yuyama"]}],"country":[]}}'




class Movie:
    def __init__(self, data):
        self.all_data = json.loads(data)

    def image(self):
        return self.all_data["RESULT"]["nfinfo"]["image1"]

    def title(self):
        return self.all_data["RESULT"]["nfinfo"]["title"]

    def synopsis(self):
        return self.all_data["RESULT"]["nfinfo"]["synopsis"]

    def released(self):
        return self.all_data["RESULT"]["nfinfo"]["released"]

    def runtime(self):
        return self.all_data["RESULT"]["nfinfo"]["runtime"]

    def genre(self):
        return self.all_data["RESULT"]["imdbinfo"]["genre"]

    def language(self):
        return self.all_data["RESULT"]["imdbinfo"]["language"]

    def actor(self):
        return self.all_data["RESULT"]["people"][0]["actor"]

    def creator(self):
        return self.all_data["RESULT"]["people"][1]["creator"]

    def director(self):
        return self.all_data["RESULT"]["people"][2]["director"]


#y = Node(movie_detail)
#print(y.image())
#print(y.title())
#print(y.synopsis())
#print(y.released())
#print(y.runtime())
#print(y.genre())
#print(y.language())
#print(y.actor())
#print(y.creator())
#print(y.director())
