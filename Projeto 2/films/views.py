from django.shortcuts import render, redirect
from .models import Film
import requests
import json
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http import Http404
from .serializers import FilmSerializer

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
        img = dictio['poster']
        # TAREFA: Utilize o title e content para criar um novo Note no banco de dados
        film = Film(title = title, content = content, rating = rating, img = img)
        film.save()
        return redirect('index')
    #versao final, por as prox 3 linhas dentro do if e deletar o render
    all_films = Film.objects.all()
    serialized_film = FilmSerializer(all_films, many=True)
    #return Response(serialized_film.data)
    return render(request, 'films/index.html', {'films': all_films})


@api_view(['GET', 'POST', 'DELETE'])
def api_film(request):
    try:
        film_id = request.query_params.get('film_id')
        print(film_id)
        film = Film.objects.get(id=film_id)
    except Film.DoesNotExist:
        raise Http404()

    if request.method == 'POST':
        new_film_data = request.data
        url = "https://imdb-internet-movie-database-unofficial.p.rapidapi.com/film/{title}".format(title = new_film_data['titulo'])

        headers = {
            'x-rapidapi-host': "imdb-internet-movie-database-unofficial.p.rapidapi.com",
            'x-rapidapi-key': "890d8b80cbmsh3b3238894fe0e6bp1069f8jsndeb50fd98ced"
        }

        response = requests.request("GET", url, headers=headers)

        dictio = json.loads(response.text)

        film.title = dictio['title']
        film.content = dictio['plot']
        film.rating = float(dictio['rating'])
        film.img = dictio['poster']
        film.save()
    elif request.method == "DELETE":
        id = request.POST.get('id')
        film = Film.objects.get(id=id)
        film.delete()
    serialized_film = FilmSerializer(film)
    return Response(serialized_film.data)

@api_view(['GET', 'POST'])
def api_film_list(request):
    if request.method == 'POST':
        new_film_data = request.data
        film = Film()
        url = "https://imdb-internet-movie-database-unofficial.p.rapidapi.com/film/{title}".format(title = new_film_data['titulo'])

        headers = {
            'x-rapidapi-host': "imdb-internet-movie-database-unofficial.p.rapidapi.com",
            'x-rapidapi-key': "890d8b80cbmsh3b3238894fe0e6bp1069f8jsndeb50fd98ced"
        }

        response = requests.request("GET", url, headers=headers)

        dictio = json.loads(response.text)

        film.title = dictio['title']
        film.content = dictio['plot']
        film.rating = float(dictio['rating'])
        film.img = dictio['poster']
        film.save()

    all_films = Film.objects.all()
    serialized_film = FilmSerializer(all_films, many=True)
    return Response(serialized_film.data)