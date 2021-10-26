# https://rapidapi.com/rapidapi/api/movie-database-imdb-alternative/
import requests
import json

url = "https://movie-database-imdb-alternative.p.rapidapi.com/"

querystring = {"r":"json","i":"tt4154796"}

headers = {
    'x-rapidapi-host': "movie-database-imdb-alternative.p.rapidapi.com",
    'x-rapidapi-key': "890d8b80cbmsh3b3238894fe0e6bp1069f8jsndeb50fd98ced"
    }

response = requests.request("GET", url, headers=headers, params=querystring)
dictio = json.loads(response.text)

print(dictio["Title"])