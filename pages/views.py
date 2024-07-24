from django.shortcuts import render
from gallery.models import Categoria
# Create your views here.


def index(request):
    categorias = Categoria.objects.all()
    return render(request, 'pages/index.html', {'categorias': categorias})


def about(request):
    return render(request, 'pages/about.html')


def faq(request):
    return render(request, 'pages/faq.html')


def contact(request):
    return render(request, 'pages/contact.html')
