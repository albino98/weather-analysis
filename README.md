<p align="center">
<a href="https://www.flaticon.com/free-icons/graph" target="_blank" >
<img src="https://user-images.githubusercontent.com/63566699/151661097-ce9b885f-ca37-4c38-a435-dc8033e624b6.png" alt="weather-analysis" />
</a>
</p>

# Weather-Analysis

## Description

The purpose of the project is to historicize and analyze the meteorological data of a certain area, to understand how the weather will change.

The project consists of a python script (to be scheduled at 00:00 every day) and a python application with flask. 

**The script** (telegramForecast.py):

**1)**  retrieves the weather forecast of the day with three-hour intervals through the free api provided by [OpenWeatherMap](https://openweathermap.org/);

**2)**  sends these weather forecasts to a telegram bot;

**3)**  saves the data to a MySQL database;

**The flask application** displays the graphs of the various weather parameters through the [Frappe Charts](https://github.com/frappe/charts) library.

![screen1](https://user-images.githubusercontent.com/63566699/151639990-978bc146-a3b0-4635-a29f-c4f5809293ac.png)

## Web Application Code

### secrets.py

The script.py script is a simple python file that contains a dictionary with the db credentials and other information that you don't want shown on the repository. In fact, it is enough not to commit the file by inserting it in the .gitignore.

```{python}
secrets = {
    'DB_HOST': "host_name",
    'DB_USR': "db user",
    'DB_NAME': 'db_name',
    'DB_PORT': 'db_port',
    'DB_PWD': 'db_pwd',
    #OPENWEATHERMAP CONF
    'OWM_API_KEY': 'omw_key',
    'OWM_CITY': 'name_of_city',
    #TELEGRAM CONF
    'TELEGRAM_BOT_KEY': 'telegram_key',
    'TELEGRAM_CHAT_ID': 'chat_id'
}
```
## Telegram Script

### Forecast Configuration

<img style="width:30%; height:20%;" src="https://user-images.githubusercontent.com/63566699/151667607-5f80e18b-edbc-4544-8fa0-af3a410f8b28.jpg">
<img style="width:30%; height:20%;" src="https://user-images.githubusercontent.com/63566699/151667541-aab00f9b-2b03-41d6-a6de-2bf91430006c.jpg">

The API used provides the weather forecast every three hours, scheduling the script at 00:00 will send 8 forecasts as shown above. If you want to send fewer forecasts, just change the number at the following line of the script:

```{python}
forecast = get_response().json()["list"][0:8]
```
## Deployment

I have deployed the whole application on PythonAnywhere, the script that sends the weather forecast, the web application and the MySql database.

### Database Dump

The following is a very useful command which allows you to export the database from PythonAnywhere. **The command must be run via a bash console and not a db console. Replace USER and HOSTNAME in three occurrences:**

```{bash}
mysqldump -u USER -h HOSTNAME --databases    'USER$default' --single-transaction --no-tablespaces > backup.sql;
```
The command will generate the .sql script at /home/user on PythonAnywhere:

![image](https://user-images.githubusercontent.com/63566699/151668840-244b22db-dc86-412e-a88d-140bf449e64b.png)


