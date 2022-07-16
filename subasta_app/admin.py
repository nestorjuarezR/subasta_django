from .models import Categoria
from django.contrib import admin

# Register your models here.

class CategoriaAdmin(admin.ModelAdmin):
    list_categorias = ("nombre", "descripcion")

admin.site.register(Categoria, CategoriaAdmin)
