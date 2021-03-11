import requests

print("Start Program")

API_KEY = 'eb8ba848f5d59614a31f13987ddf8e37'
BASE_URL = 'http://api.openweathermap.org/data/2.5/weather?appid='+API_KEY
while(True):
    print('0: Exit')
    print('1. Find Weather Based on City')
    print('2. Find Weather Based on Zip Code')
    print('3. Find Weather Based on Geographic')

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
            data = res.json()
            print(data)


