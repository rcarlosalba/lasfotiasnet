from django.contrib import admin
from .models import CustomURL
from django.utils.html import format_html
# Register your models here.


class CustomURLAdmin(admin.ModelAdmin):
    list_display = ('album_name', 'masked_url')  # Mostrar la URL enmascarada
    fields = ('url_original', 'album_name')
    # Hacer la URL enmascarada de solo lectura
    readonly_fields = ('masked_url',)

    def masked_url(self, obj):
        if obj.album_name:
            return format_html('<a href="{}" target="_blank">{}</a>', obj.generate_masked_url(), obj.generate_masked_url())
        return "Album name not set"

    masked_url.short_description = 'Masked URL'
    masked_url.allow_tags = True


admin.site.register(CustomURL, CustomURLAdmin)
