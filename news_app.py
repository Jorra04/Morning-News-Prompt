from bs4 import BeautifulSoup
import pyttsx3
import requests
from twilio.rest import Client
import speech_recognition as sr
from creds import account_sid, auth_token, cell, twillio_num
class news_app:
    def __init__(self):
        self.__message = ""
    def get_weather(self):
        r = requests.get('http://api.openweathermap.org/data/2.5/weather?id=6173577&appid=fa711ce878bc951520b7a3e55fee096a')
        json_obj = r.json()
        temp = float(json_obj['main']['temp']) - 273.15
        desc = json_obj["weather"][0]["description"]
        return str(int(temp)) + " °C" + " - " + str(desc)
    
    def next_leafs_game(self): ##written weird but it works
        URL = 'https://www.thescore.com/nhl/teams/5' #scrape from this site
        page = requests.get(URL)
        team = ""
        time = ""
        date = ""
        soup = BeautifulSoup(page.content, 'html.parser')
        results = soup.find_all("div", class_="EventCard__teamName--JweK5") #The score uses this classname for all their upcoming games... so you will have 
        if(results[2].get_text().strip().find("TOR") == -1):
            team = results[2].get_text().strip()
        else:
            team = results[3].get_text().strip()
        date = soup.find("div", class_="TeamMiniSchedule__nextGameHeader--ogTJZ").get_text().strip()
        
        time = soup.find_all("div", class_="EventCard__clockColumn--3lEPz")[1].get_text().strip()

        return date[13:len(date)] + " @ " + time + " VS " + team

    def next_jays_game(self): ##written weird but it works
        URL = 'https://www.thescore.com/mlb/teams/4' #scrape from this site
        page = requests.get(URL)
        team = ""
        time = ""
        date = ""
        soup = BeautifulSoup(page.content, 'html.parser')
        results = soup.find_all("div", class_="EventCard__teamName--JweK5") #The score uses this classname for all their upcoming games... so you will have 
        if(results[2].get_text().strip().find("TOR") == -1):
            team = results[2].get_text().strip()
        else:
            team = results[3].get_text().strip()
        date = soup.find("div", class_="TeamMiniSchedule__nextGameHeader--ogTJZ").get_text().strip()
        
        time = soup.find_all("div", class_="EventCard__clockColumn--3lEPz")[1].get_text().strip()

        return date[13:len(date)] + " @ " + time + " VS " + team

    def get_relevant_news(self):
        pass
    def baseball_team_decoder(self, message):
        if(message.find("LAA") != -1):
            message = message.replace("ANA", "Los Angeles")
            return message

        elif(message.find("ARI") != -1):
            message = message.replace("ARI", "Arizona")
            return message

        elif(message.find("ATL") != -1):
            message = message.replace("ATL", "Atlanta")
            return message

        elif(message.find("BAL") != -1):
            message = message.replace("BAL", "Baltimore")
            return message

        elif(message.find("BOS") != -1):
            message = message.replace("BOS", "Boston")
            return message

        elif(message.find("CWS") != -1):
            message = message.replace("CWS", "Chicago")
            return message
        
        elif(message.find("CHC") != -1):
            message = message.replace("CHC", "Chicago")
            return message

        elif(message.find("CLE") != -1):
            message = message.replace("CLE", "Cleveland")
            return message

        elif(message.find("CIN") != -1):
            message = message.replace("CIN", "Cincinnati")
            return message

        elif(message.find("COL") != -1):
            message = message.replace("COL", "Colorado")
            return message

        elif(message.find("DET") != -1):
            message = message.replace("DET", "Detroit")
            return message

        elif(message.find("FLA") != -1):
            message = message.replace("FLA", "Florida")
            return message

        elif(message.find("HOU") != -1):
            message = message.replace("HOU", "Houston")
            return message

        elif(message.find("KC") != -1):
            message = message.replace("KC", "Kansas City")
            return message

        elif(message.find("LAD") != -1):
            message = message.replace("LAD", "Los Angeles")
            return message

        elif(message.find("MIA") != -1):
            message = message.replace("MIA", "Miami")
            return message

        elif(message.find("MIN") != -1):
            message = message.replace("MIN", "Minnesota")
            return message

        elif(message.find("MIL") != -1):
            message = message.replace("MIL", "Milwuakee")
            return message

        elif(message.find("NYM") != -1):
            message = message.replace("NYM", "New York")
            return message

        elif(message.find("NYY") != -1):
            message = message.replace("NYY", "New York")
            return message

        elif(message.find("OAK") != -1):
            message = message.replace("OAK", "Oakland")
            return message

        elif(message.find("PHI") != -1):
            message = message.replace("PHI", "Philidelphia")
            return message

        elif(message.find("PIT") != -1):
            message = message.replace("PIT", "Pittsburgh")
            return message

        elif(message.find("SD") != -1):
            message = message.replace("SD", "San Diego")
            return message

        elif(message.find("SEA") != -1):
            message = message.replace("SEA", "Seattle")
            return message

        elif(message.find("SF") != -1):
            message = message.replace("SF", "San Francisco")
            return message

        elif(message.find("STL") != -1):
            message = message.replace("STL", "St. Louis")
            return message

        elif(message.find("TB") != -1):
            message = message.replace("TB", "Tampa Bay")
            return message

        elif(message.find("TEX") != -1):
            message = message.replace("TEX", "Texas")
            return message

        elif(message.find("WSH") != -1):
            message = message.replace("WSH", "Washington")
            return message

    def hockey_team_decoder(self, message):
        if(message.find("CBJ") != -1):
            message = message.replace("CBJ", "Columbus")
            return message

        elif(message.find("BOS") != -1):
            message = message.replace("BOS", "Boston")
            return message

        elif(message.find("ANA") != -1):
            message = message.replace("ANA", "Anaheim")
            return message

        elif(message.find("ARI") != -1):
            message = message.replace("ARI", "Arizona")
            return message

        elif(message.find("BUF") != -1):
            message = message.replace("BUF", "Buffalo")
            return message

        elif(message.find("CAR") != -1):
            message = message.replace("CAR", "Carolina")
            return message

        elif(message.find("CGY") != -1):
            message = message.replace("CGY", "Calgary")
            return message

        elif(message.find("CHI") != -1):
            message = message.replace("CHI", "Chicago")
            return message

        elif(message.find("COL") != -1):
            message = message.replace("COL", "Colorado")
            return message

        elif(message.find("DAL") != -1):
            message = message.replace("DAL", "Dallas")
            return message

        elif(message.find("DET") != -1):
            message = message.replace("DET", "Detroit")
            return message

        elif(message.find("EDM") != -1):
            message = message.replace("EDM", "Edmonton")
            return message

        elif(message.find("FLA") != -1):
            message = message.replace("FLA", "Florida")
            return message

        elif(message.find("LAK") != -1):
            message = message.replace("LAK", "Los Angeles")
            return message

        elif(message.find("MIN") != -1):
            message = message.replace("MIN", "Minnesota")
            return message

        elif(message.find("MTL") != -1):
            message = message.replace("MTL", "Montreal")
            return message

        elif(message.find("NSH") != -1):
            message = message.replace("NSH", "Nashville")
            return message

        elif(message.find("NJD") != -1):
            message = message.replace("NJD", "New Jersey")
            return message

        elif(message.find("NYI") != -1):
            message = message.replace("NYI", "New York")
            return message

        elif(message.find("NYR") != -1):
            message = message.replace("NYR", "New York")
            return message

        elif(message.find("OTT") != -1):
            message = message.replace("OTT", "Ottawa")
            return message

        elif(message.find("PHI") != -1):
            message = message.replace("PHI", "Philidelphia")
            return message

        elif(message.find("PIT") != -1):
            message = message.replace("PIT", "Pittsburgh")
            return message

        elif(message.find("SJS") != -1):
            message = message.replace("SJS", "San Jose")
            return message

        elif(message.find("STL") != -1):
            message = message.replace("STL", "St. Louis")
            return message

        elif(message.find("TBL") != -1):
            message = message.replace("TBL", "Tampa Bay")
            return message

        elif(message.find("VAN") != -1):
            message = message.replace("VAN", "Vancouver")
            return message

        elif(message.find("VGK") != -1):
            message = message.replace("VGK", "Las Vegas")
            return message

        elif(message.find("WPG") != -1):
            message = message.replace("WPG", "Winnipeg")
            return message
            
        elif(message.find("WSH") != -1):
            message = message.replace("WSH", "Washington")
            return message
          
assistant = news_app()

final_string = "Good morning, the current temperature is: " + str(assistant.get_weather() + "\n" + "The next Toronto Maple Leafs game will be: " +
     str(assistant.hockey_team_decoder(assistant.next_leafs_game()))) + "\nThe next Toronto Blue Jays game will be: " + str(assistant.baseball_team_decoder(assistant.next_jays_game()))

# assistant.hockey_team_decoder(assistant.next_leafs_game())
# print(final_string)
engine = pyttsx3.init()
engine.setProperty('rate', 170)
voices = engine.getProperty('voices')
try:
    engine.setProperty('voice', voices[1].id)
except:
    engine.setProperty('voice', voices[0].id)

engine.say(final_string)
engine.runAndWait()

engine.say("May I start the wakeup protocol? ")
engine.runAndWait()
r = sr.Recognizer()
with sr.Microphone() as source:
    audio_data = r.record(source, duration=5)
    engine.say("Hang on while I process that")
    engine.runAndWait()
    text = r.recognize_google(audio_data)

if(text == 'yes' or text == 'Yes'):
    print("Lights on")

# client = Client(account_sid, auth_token)

# message = client.messages.create(body=final_string,from_=twillio_num,to=cell)