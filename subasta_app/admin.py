from .models import Categoria, Articulo, Subasta, Profile
from django.contrib import admin

# Register your models here.
class ProfileAdmin(admin.ModelAdmin):
    lista = ('user')


class CategoriaAdmin(admin.ModelAdmin):
    list_categorias = ("nombre", "descripcion")


class ArticuloAdmin(admin.ModelAdmin):
    lista = ("nombre", "categoria", )


class SubastaAdmin(admin.ModelAdmin):
    lista = ("articulo", "user_ganador")

admin.site.register(Profile, ProfileAdmin)
admin.site.register(Categoria, CategoriaAdmin)
admin.site.register(Articulo, ArticuloAdmin)
admin.site.register(Subasta,SubastaAdmin)

