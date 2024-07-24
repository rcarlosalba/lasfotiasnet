from django.shortcuts import render, get_object_or_404
from .models import Categoria, Album

# Create your views here.


def index_gallery(request):
    categorias = Categoria.objects.all()
    return render(request, 'index.html', {'categorias': categorias})


def categoria_detail(request, slug):
    categoria = get_object_or_404(Categoria, slug=slug)
    albumes = categoria.albumes.all()
    return render(request, 'gallery/categoria_detail.html', {'categoria': categoria, 'albumes': albumes})


def album_detail(request, slug):
    album = get_object_or_404(Album, slug=slug)
    fotos = album.fotos.all()
    return render(request, 'gallery/album_detail.html', {'album': album, 'fotos': fotos})
