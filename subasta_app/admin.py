from .models import Categoria, Articulo
from django.contrib import admin

# Register your models here.

class CategoriaAdmin(admin.ModelAdmin):
    list_categorias = ("nombre", "descripcion")


class ArticuloAdmin(admin.ModelAdmin):
    lista = ("nombre", "categoria", )

admin.site.register(Categoria, CategoriaAdmin)
admin.site.register(Articulo, ArticuloAdmin)

