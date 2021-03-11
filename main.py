import requests
import mysql.connector
import json

print("Start Program")

# Connect database
mydb = mysql.connector.connect(
      host="localhost",
      user="root",
      password=""
)
mycursor = mydb.cursor()

# create database
mycursor.execute("CREATE DATABASE IF NOT EXISTS weather")
mycursor.execute("USE weather")

# create table
mycursor.execute("CREATE TABLE IF NOT EXISTS `weather` ( `id` INT(11) UNSIGNED NOT NULL, `name` VARCHAR(50), `content` TEXT, PRIMARY KEY (`id`) )")

API_KEY = 'eb8ba848f5d59614a31f13987ddf8e37'
BASE_URL = 'http://api.openweathermap.org/data/2.5/weather?appid='+API_KEY
current_data = {}

while(True):
    print('0: Exit')
    print('1. Find Weather Based on City')
    print('2. Find Weather Based on Zip Code')
    print('3. Find Weather Based on Geographic')
    print('4. Save current weather')
    print('5. Display weather from database')
    print('6. Display weather from database alphabetically')

    choice = int(input('Choice: '))
    if choice == 1:
        city = input('City Name: ')
        url = BASE_URL + '&q=' + city

    if choice == 2: # 94040,us
        zip_code = input('Zip Code: ')
        url = BASE_URL + '&zip=' + zip_code

    if choice == 3: # 35,129
        lat_lon = input('Lat, Lon: ')
        lat_lon_array = lat_lon.split(',')
        if len(lat_lon_array) < 2:
            print("Invalid Geographic")
            continue

        url = BASE_URL + '&lat=' + lat_lon_array[0] + '&lon=' + lat_lon_array[1]

    if choice == 1 or choice == 2 or choice == 3:
        res = requests.get(url)
        if res.status_code != 200:
            print('Invalid Input')
        else:
            current_data = res.json()
            print(current_data)


    if choice == 4:
        if current_data:
            try:
                result = json.dumps(current_data)
                sql = "INSERT INTO weather (id, name, content) VALUES (" + str(current_data['id']) + ", '" + current_data['name'] + "', '" + result + "')"
                mycursor.execute(sql)
                mydb.commit()

                print("Weather Data is saved successfully")
            except Exception as e:
                print(e)
        else:
            print("There is no data for saving")


    if choice == 5 or choice == 6:
        try:
            sql = "Select * From weather"
            if choice == 6:
                sql = sql + " order by name"

            mycursor.execute(sql)

            myresult = mycursor.fetchall()

            for x in myresult:
                print(x)

        except Exception as e:
            print(e)
