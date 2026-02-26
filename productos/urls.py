
from django.urls import path
from .views import listar_productos, otra_vista

urlpatterns = [
    path('', listar_productos, name='lista_productos'),
    path('otra/', otra_vista, name='otra_vista')
]