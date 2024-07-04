import requests
import datetime


api_key = "baa7b30be7211c6435a66ffcd73a6aa9"



city = 'Paris'


url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric'


response = requests.get(url)


if response.status_code == 200:
    
    data = response.json()

    
    temperature_actuelle = data['main']['temp']
    temperature_min = data['main']['temp_min']
    temperature_max = data['main']['temp_max']
    humidite = data['main']['humidity']
    vitesse_vent = data['wind']['speed']
    direction_vent = data['wind']['deg']
    pression_atmospherique = data['main']['pressure']
    description_temps = data['weather'][0]['description']
    heure_lever_soleil = datetime.datetime.fromtimestamp(data['sys']['sunrise']).strftime('%H:%M:%S')
    heure_coucher_soleil = datetime.datetime.fromtimestamp(data['sys']['sunset']).strftime('%H:%M:%S')

    
    print(f"Météo à {city}:")
    print(f"Température actuelle: {temperature_actuelle}°C")
    print(f"Température minimale: {temperature_min}°C")
    print(f"Température maximale: {temperature_max}°C")
    print(f"Humidité: {humidite}%")
    print(f"Vitesse du vent: {vitesse_vent} m/s")
    print(f"Direction du vent: {direction_vent}°")
    print(f"Pression atmosphérique: {pression_atmospherique} hPa")
    print(f"Description du temps: {description_temps}")
    print(f"Heure du lever du soleil: {heure_lever_soleil}")
    print(f"Heure du coucher du soleil: {heure_coucher_soleil}")
else:
    print(f"Erreur lors de la requête: {response.status_code}")

