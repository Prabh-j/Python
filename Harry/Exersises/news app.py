#use newsapi using request module to fetch news on two diffrenet topic
import requests
import json

def news(a):
    data = { 'q':a,'from': '2023-10-26', 'sortBy':'popularity','apiKey': '93e25304a544431ba79473776f5947ca'}

    news = requests.get('https://newsapi.org/v2/top-headlines', params=data)

    x = news.json()
    print('\n')
    for i in x['articles']:
        print(i['title'])
        print(i['description'])
        print("------------------------------------------------------------------------------------------------------------------------------------------")

s = input('selet the topic: ')
j = input('selet the second topic: ')
news(s)
news(j)