from django.db.models.fields.related import create_many_to_many_intermediary_model
from django.shortcuts import render, redirect
from .models import Note, Tag


def index(request):
    if request.method == 'POST':
        title = request.POST.get('titulo')
        content = request.POST.get('detalhes')
        tag_info = request.POST.get('tag')
        # TAREFA: Utilize o title e content para criar um novo Note no banco de dados
        tag, new = Tag.objects.get_or_create(tag = tag_info)
        if new:
            tag.save()

        note = Note(title = title, content = content, tag = tag)
        note.save()
        return redirect('index')
    else:
        all_notes = Note.objects.all()
        return render(request, 'notes/note.html', {'notes': all_notes})

def delete(request):
    id = request.POST.get('id')
    note = Note.objects.get(id=id)
    note.delete()

    return redirect('index')

def edit(request, id):
    title = request.POST.get('titulo')
    content = request.POST.get('detalhes')
    tag_info = request.POST.get('tag')
    tag, new = Tag.objects.get_or_create(tag = tag_info)
    print(new)
    if new:
        tag.save()
        
    note = Note.objects.filter(id=id)
    
    note.update(title=title, content=content, tag = tag)
    
    return redirect('index')

def list_tags(request):
    tags = Tag.objects.all()
    return render(request, 'notes/all_tags.html', {'tags': tags})

def tag_info(request, tag_id):
    tag_select = Tag.objects.filter(id = tag_id)
    note_select = Note.objects.filter(tag = tag_id)
    return render(request, 'notes/tag_info.html', {'notes': note_select})