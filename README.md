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
