import requests
import json

url = "https://imdb-internet-movie-database-unofficial.p.rapidapi.com/film/avengers"

headers = {
    'x-rapidapi-host': "imdb-internet-movie-database-unofficial.p.rapidapi.com",
    'x-rapidapi-key': "890d8b80cbmsh3b3238894fe0e6bp1069f8jsndeb50fd98ced"
    }

response = requests.request("GET", url, headers=headers)

print(response.text)
dictio = json.loads(response.text)

print(dictio["Title"])


#resposta esperada
'''
{11 items
"id":"tt0848228"
"title":"The Avengers "
"year":"2012"
"length":"2h 23min"
"rating":"8.0"
"rating_votes":"1213478"
"poster":"https://m.media-amazon.com/images/M/MV5BNDYxNjQyMjAtNTdiOS00NGYwLWFmNTAtNThmYjU5ZGI2YTI1XkEyXkFqcGdeQXVyMTMxODk2OTU@.jpg"
"plot":"Earth's mightiest heroes must come together and learn to fight as a team if they are going to stop the mischievous Loki and his alien army from enslaving humanity."
"trailer":{2 items
"id":"vi1891149081"
"link":"https://www.imdb.com/videoplayer/vi1891149081"
}
"cast":[15 items
0:{...}3 items
1:{...}3 items
2:{...}3 items
3:{...}3 items
4:{...}3 items
5:{...}3 items
6:{...}3 items
7:{...}3 items
8:{...}3 items
9:{...}3 items
10:{...}3 items
11:{...}3 items
12:{...}3 items
13:{...}3 items
14:{...}3 items
]
"technical_specs":[10 items
0:[...]2 items
1:[...]2 items
2:[...]2 items
3:[...]2 items
4:[...]2 items
5:[...]2 items
6:[...]2 items
7:[...]2 items
8:[...]2 items
9:[...]2 items
]
}
'''