from django.db import models
from django.utils.text import slugify


# Create your models here.
class Categoria(models.Model):
    titulo = models.CharField(max_length=100)
    descripcion = models.TextField()
    imagen = models.ImageField(upload_to='categorias/')
    slug = models.SlugField(max_length=100, unique=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.titulo)
        super(Categoria, self).save(*args, **kwargs)

    def __str__(self):
        return self.titulo


class Album(models.Model):
    titulo = models.CharField(max_length=100)
    categoria = models.ForeignKey(
        Categoria, related_name='albumes', on_delete=models.CASCADE)
    imagen_destacada = models.ImageField(upload_to='albumes/')
    slug = models.SlugField(max_length=100, unique=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.titulo)
        super(Album, self).save(*args, **kwargs)

    def __str__(self):
        return self.titulo


class Foto(models.Model):
    album = models.ForeignKey(
        Album, related_name='fotos', on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to='fotos/')
    pie_de_foto = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return f"{self.album.titulo} - {self.id}"
