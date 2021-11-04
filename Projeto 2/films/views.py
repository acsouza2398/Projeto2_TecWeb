from django.shortcuts import render, redirect
from .models import Film
import requests
import json


def index(request):
    if request.method == 'POST':

        url = "https://imdb-internet-movie-database-unofficial.p.rapidapi.com/film/{title}".format(title = request.POST.get('titulo'))

        headers = {
            'x-rapidapi-host': "imdb-internet-movie-database-unofficial.p.rapidapi.com",
            'x-rapidapi-key': "890d8b80cbmsh3b3238894fe0e6bp1069f8jsndeb50fd98ced"
        }

        response = requests.request("GET", url, headers=headers)

        dictio = json.loads(response.text)

        title = dictio['title']
        content = dictio['plot']
        rating = float(dictio['rating'])
        # TAREFA: Utilize o title e content para criar um novo Note no banco de dados
        film = Film(title = title, content = content, rating = rating)
        film.save()
        return redirect('index')
    else:
        all_films = Film.objects.all()
        return render(request, 'films/index.html', {'films': all_films})

def delete(request):
    id = request.POST.get('id')
    film = Film.objects.get(id=id)
    film.delete()

    return redirect('index')