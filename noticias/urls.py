

from django.urls import path
from .views import listas_noticias


urlpatterns = [
    path('', listas_noticias, name="lista_noticias")
]