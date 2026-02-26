from django.shortcuts import render
from .models import Noticia
# Create your views here.

def listas_noticias(request):
    noticias = Noticia.objects.all().order_by("-fecha_publicacion")
    return render(request, 'noticias/lista.html', {'noticias': noticias})