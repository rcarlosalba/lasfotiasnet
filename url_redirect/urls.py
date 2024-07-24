from django.urls import path
from . import views

urlpatterns = [
    path('<str:album_name>/', views.redirect_to_original,
         name='redirect_to_original'),
]
