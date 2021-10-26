from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('delete', views.delete, name='note_delete'),
    path('edit/<int:id>', views.edit, name='note_edit'),
    path('tags', views.list_tags, name='tag_list'),
    path('tag/<int:tag_id>', views.tag_info, name='tag_info')
]