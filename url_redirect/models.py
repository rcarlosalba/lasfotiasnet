from django.db import models
from django.conf import settings

# Create your models here.


class CustomURL(models.Model):
    url_original = models.URLField()
    album_name = models.CharField(unique=True, blank=True, max_length=350)

    def generate_masked_url(self):
        return f"{settings.SITE_URL}/redirect/{self.album_name}"

    def save(self, *args, **kwargs):
        if not self.album_name:
            import uuid
            self.album_name = str(uuid.uuid4())
        super().save(*args, **kwargs)

    def __str__(self):
        return self.generate_masked_url()  # Mostrar la URL enmascarada por defecto

    class Meta:
        verbose_name = "Generar URL personalizada"  # Cambiar el nombre en el admin
        verbose_name_plural = "Generar URLs personalizadas"
