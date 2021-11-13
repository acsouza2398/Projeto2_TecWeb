from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('api/films/<int:film_id>/', views.api_film),
    path('api/films/', views.api_film_list),
]