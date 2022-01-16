import requests as rq
import json
from datetime import datetime as dt
import mysql.connector
from secrets import secrets

def connectToMySql():
    mydb = mysql.connector.connect(
        host=secrets.get('DB_LOCALHOST'),
        user=secrets.get('DB_LOCALHOST_USR'),
        # password="yourpassword",
        database=secrets.get('DB_LOCALHOST_NAME')
    )
    return mydb

def saveForecastOnDb(weather):
    temp = weather['main']['temp']
    feels_like = weather['main']['feels_like']
    temp_min = weather['main']['temp_min']
    temp_max = weather['main']['temp_max']
    pressure = weather['main']['pressure']
    sea_level = weather['main']['sea_level']
    grnd_level = weather['main']['grnd_level']
    humidity = weather['main']['humidity']
    weather_id = weather['weather'][0]['id']
    weather_main = weather['weather'][0]['main']
    weather_desc = weather['weather'][0]['description']
    clouds_all = weather['clouds']['all']
    wind_speed = weather['wind']['speed']
    wind_deg = weather['wind']['deg']
    wind_gust = weather['wind']['gust']
    visibility = weather['visibility']
    pop = weather['pop']
    pod = weather['sys']['pod']
    dateTime = dt.strptime(weather["dt_txt"], "%Y-%m-%d %H:%M:%S")

    #print(str(temp)+str(feels_like)+str(temp_min)+str(temp_max)+str(pressure)+str(sea_level)+str(grnd_level)+str(humidity)+str(weather_id)+str(weather_main)+str(weather_desc)+str(clouds_all+wind_speed)+str(wind_deg)+str(wind_gust)+str(visibility)+str(pop)+str(pod)+str(dateTime))
    result = False
    mydb = connectToMySql()
    try:
        mycursor = mydb.cursor()
        sql = "INSERT INTO `forecastdata`(`temp`, `feels_like`, `temp_min`, `temp_max`, `pressure`, `sea_level`, `grnd_level`, `humidity`, `weather_id`, `weather_main`, `weather_desc`, `clouds_all`, `wind_speed`, `wind_deg`, `wind_gust`, `visibility`, `pop`, `pod`, `dt`) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        val = (temp,feels_like,temp_min,temp_max,pressure,sea_level,grnd_level,humidity,weather_id,weather_main,weather_desc,clouds_all,wind_speed,wind_deg,wind_gust,visibility,pop,pod,dateTime)
        mycursor.execute(sql, val)
        mydb.commit()
        print(mycursor.rowcount, "record inserted.")
        if mycursor.rowcount > 0:
            result = True
        mydb.close()
    except Exception as e:
        mydb.close()
        print(str(e))
    return result

# format forecast data for insert on db
def formatForecastData(forecastData):
    for row in forecastData:
        insert_result = saveForecastOnDb(row)
        print(str(insert_result))

# Return response from OpenWeather for your city
def get_response():
    api_key = secrets.get('OWM_API_KEY')
    base_url = "http://api.openweathermap.org/data/2.5/forecast"  # 5 day weather forecast
    city = secrets.get('OWM_CITY')
    payload = {"q": city, "appid": api_key, "units": "metric", "lang": "it"}

    return rq.get(base_url, params=payload)


# Function to send custom message to Weather Channel
def send_message(message):
    bot_key = secrets.get('TELEGRAM_BOT_KEY')
    url = "https://api.telegram.org/bot" + bot_key
    chat_id = secrets.get('TELEGRAM_CHAT_ID')
    rq.get(url + "/sendMessage", params={"chat_id": chat_id, "text": message})


# Main function
def main():
    forecast = get_response().json()["list"][0:8]
    message = f"Buongiorno,\n\nle previsioni di oggi sono:\n"
    for weather in forecast:
        time_dt = dt.strptime(weather["dt_txt"], "%Y-%m-%d %H:%M:%S")
        message += (f"\n"+u"\U0001F550"+f"Ore: {time_dt.strftime('%H:%M')}\n" \
                    f"Tempo: {weather['weather'][0]['description']}\n" \
                    f"Temperatura: {int(round(weather['main']['temp'], 0))}°C\n"
                    f"Temperatura percepita: {int(round(weather['main']['feels_like'], 0))}°C\n"
                    f"Vento: {int(round(weather['wind']['speed'], 0)) * 3.6} Km/h\n")  # Convert from m/sec to km/h
    send_message(message)

    # If today's rain/drizzle/thunderstorm bring your umbrella
    if any(x in w["weather"][0]["description"] for w in forecast for x in ["pioggia", "temporale", "pioggerella"]):
        message += "\nNON DIMENTICARE DI PRENDERE L'OMBRELLO" + u"\U00002614"
        send_message(message)
    formatForecastData(forecast)

if __name__ == "__main__":
    main()