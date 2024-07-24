from django.contrib import admin
from .models import Categoria, Album, Foto
from django.forms.models import BaseInlineFormSet
from django.core.exceptions import ValidationError
# Register your models here.


class MinMaxInlineFormSet(BaseInlineFormSet):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.extra = max(0, 10 - len(self.initial_forms))

    def clean(self):
        super().clean()
        if any(self.errors):
            return
        total_forms = len(self.initial_forms) + len(self.extra_forms)
        if total_forms < 10:
            raise ValidationError('Debes subir al menos 10 fotos.')
        if total_forms > 20:
            raise ValidationError('No puedes subir más de 20 fotos.')


class FotoInline(admin.TabularInline):
    model = Foto
    formset = MinMaxInlineFormSet
    extra = 10
    max_num = 20


class AlbumAdmin(admin.ModelAdmin):
    inlines = [FotoInline]


admin.site.register(Categoria)
admin.site.register(Album, AlbumAdmin)
