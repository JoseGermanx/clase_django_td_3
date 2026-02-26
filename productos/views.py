from django.shortcuts import render
from .models import Producto

# Create your views here.

def listar_productos(request):
    productos = Producto.objects.all()
    return render(request, 'productos/lista.html', {'productos': productos})

def otra_vista(request):
    return render(request, 'productos/otra_pagina.html')
