from django.shortcuts import redirect, get_object_or_404
from django.http import HttpResponse
from django.core.exceptions import ObjectDoesNotExist
from .models import CustomURL

# Create your views here.


def redirect_to_original(request, album_name):
    try:
        custom_url = get_object_or_404(CustomURL, album_name=album_name)
        return redirect(custom_url.url_original)
    except ObjectDoesNotExist as e:
        print(f"Error: {e}")  # Debug
        return HttpResponse("Not Found", status=404)
