from bs4 import BeautifulSoup
import requests
from twilio.rest import Client
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

assistant = news_app()

final_string = "Good morning, the current temperature is: " + str(assistant.get_weather() + "\n" + "The next Toronto Maple Leafs game will be: " +
     str(assistant.next_leafs_game())) + "\nThe next Toronto Blue Jays game will be: " + str(assistant.next_jays_game())

print(final_string)