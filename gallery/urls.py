from django.urls import path
from . import views

urlpatterns = [
    path('', views.index_gallery, name='index_gallery'),
    path('categoria/<slug:slug>/', views.categoria_detail, name='categoria_detail'),
    path('album/<slug:slug>/', views.album_detail, name='album_detail'),
]
