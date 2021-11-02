from django.shortcuts import render, redirect
from .models import Note


def index(request):
    if request.method == 'POST':
        import requests
        import json

        url = "https://movie-database-imdb-alternative.p.rapidapi.com/"

        querystring = {"s":"{title}".format(title = request.POST.get('titulo')),"r":"json","page":"1"}

        headers = {
            'x-rapidapi-host': "movie-database-imdb-alternative.p.rapidapi.com",
            #'x-rapidapi-key': "890d8b80cbmsh3b3238894fe0e6bp1069f8jsndeb50fd98ced" #chave Ana
            #'x-rapidapi-key': '7c06e8aa11msh18a56dfb6b8a592p18b9e7jsn1c16abd3528f' #chave Tiago
            }

        response = requests.request("GET", url, headers=headers, params=querystring)

        dictio = json.loads(response.text)

        id_filme = dictio['Search'][0]['imdbID']

        querystring2 = {"r":"json","i":"{id}".format(id = id_filme)}

        response = requests.request("GET", url, headers=headers, params=querystring2)
        dictio2 = json.loads(response.text)

        valor1 = dictio2['Ratings'][0]['Value']
        valor2 = dictio2['Ratings'][1]['Value']
        valor3 = dictio2['Ratings'][2]['Value']

        valor1_nota = float(valor1[0:3])*10
        valor2_nota = float(valor2[0:2])
        valor3_nota = float(valor3[0:2])

        valor_nota_média = int((valor1_nota + valor2_nota + valor3_nota)/3)
        nota = "{0}/100".format(valor_nota_média)


        title = dictio['Search'][0]['Title']
        content = dictio2['Plot']
        # TAREFA: Utilize o title e content para criar um novo Note no banco de dados
        note = Note(title = title, content = content)
        note.save()
        return redirect('index')
    else:
        all_notes = Note.objects.all()
        return render(request, 'notes/index.html', {'notes': all_notes})