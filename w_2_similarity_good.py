import spacy
import requests

nlp = spacy.load("en_core_web_md")

api_key = "7f344331d0b2323597bb5c0818ed1cce"

def get_weather(city_name):
    api_url = "http://api.openweathermap.org/data/2.5/weather?q={}&appid={}".format(city_name, api_key)

    response = requests.get(api_url)
    response_dict = response.json()
    
    weather = response_dict["weather"][0]["description"]

    if response.status_code == 200:
        return weather
    else:
        print('[!] HTTP {0} calling [{1}]'.format(response.status_code, api_url))
        return None

#test_1
#Add those two lines and run just to test the code (output was "mist")		
weather1 = get_weather("Tokio")
print(weather1)		

def chatbot(statement):
    weather = nlp("Current weather in a city")
    statement = nlp(statement)
    min_similarity = 0.70
    
    if weather.similarity(statement) >= min_similarity:
        #pass
        similarity = weather.similarity(statement)
        return similarity

#test_2
#Add those two lines and run just to test the "similarity"code 
#(output was "mist")	
	
similarity1 = chatbot("What is the weather in Kiev?")
print(similarity1)



