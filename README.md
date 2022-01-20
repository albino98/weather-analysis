# weather-analysis

## Description

The purpose of the project is to historicize and analyze the meteorological data of a certain area, to understand how the weather will change.

The project consists of a python script (to be scheduled at 00:00 every day) and a python application with flask. 

**The script** (telegramForecast.py):

**1)**  retrieves the weather forecast of the day with three-hour intervals through the free api provided by OpenWeatherMap;

**2)**  sends these weather forecasts to a telegram bot;

**3)**  saves the data to a MySQL database;

**The flask application** displays the graphs of the various weather parameters through the [Frappe Charts](https://github.com/frappe/charts) library.

