from .models import Categoria, Articulo, Subasta, Profile, Publicacion, Puja
from django.contrib import admin

# Register your models here.
class ProfileAdmin(admin.ModelAdmin):
    list_display = ("id","user")


class CategoriaAdmin(admin.ModelAdmin):
    list_display = ("nombre", "descripcion")


class ArticuloAdmin(admin.ModelAdmin):
    list_display = ("nombre", "categoria", "user")
    search_fields = ("id", "user", "nombre")


class PublicacionAdmin(admin.ModelAdmin):
    list_display = ("articulo", "is_active")

class SubastaAdmin(admin.ModelAdmin):
    list_display = ("articulo", "user_ganador")

class PujaAdmin(admin.ModelAdmin):
    list_display = ("user", "precio")

admin.site.register(Profile, ProfileAdmin)
admin.site.register(Categoria, CategoriaAdmin)
admin.site.register(Articulo, ArticuloAdmin)
admin.site.register(Publicacion, PublicacionAdmin)
admin.site.register(Subasta,SubastaAdmin)
admin.site.register(Puja, PujaAdmin)
