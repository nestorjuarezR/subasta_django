from .models import Categoria, Articulo, Subasta, Profile, Publicacion, Puja
from django.contrib import admin

# Register your models here.
class ProfileAdmin(admin.ModelAdmin):
    lista = ("user")


class CategoriaAdmin(admin.ModelAdmin):
    list_categorias = ("nombre", "descripcion")


class ArticuloAdmin(admin.ModelAdmin):
    lista = ("nombre", "categoria", )


class PublicacionAdmin(admin.ModelAdmin):
    lista = ("articulo", "is_active")

class SubastaAdmin(admin.ModelAdmin):
    lista = ("articulo", "user_ganador")

class PujaAdmin(admin.ModelAdmin):
    lista = ("user", "precio")

admin.site.register(Profile, ProfileAdmin)
admin.site.register(Categoria, CategoriaAdmin)
admin.site.register(Articulo, ArticuloAdmin)
admin.site.register(Publicacion, PublicacionAdmin)
admin.site.register(Subasta,SubastaAdmin)
admin.site.register(Puja, PujaAdmin)
