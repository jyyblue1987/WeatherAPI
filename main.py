import requests

print("Start Program")

API_KEY = 'eb8ba848f5d59614a31f13987ddf8e37'
BASE_URL = 'http://api.openweathermap.org/data/2.5/weather?appid='+API_KEY
while(True):
    print('0: Exit')
    print('1. Get Weather Based on City')

    choice = int(input('Choice: '))
    if choice == 1 :
        city = input('City Name: ')
        url = BASE_URL + '&q=' + city
        res = requests.get(url)
        if res.status_code != 200:
            print('Invalid City Name')
        else:
            data = res.json()
            print(data)


