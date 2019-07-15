from django.urls import path
from .views import procesarFoto, home

app_name = 'recognition'

urlpatterns = [
    path(r'', home, name='enviar-foto'),
    path(r'procesar-foto', procesarFoto, name='procesar-foto')
]
