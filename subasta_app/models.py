from django.db import models
from django.contrib.auth.models import User

# Create your models here.

#Modelo de Perfil de usuario
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    date_birth = models.DateField(null=True, blank=True)
    GENERO = [
    ("H", "Hombre"),
    ("M", "Mujer"),
    ("O", "Otro"),
    ]
    genere = models.CharField(max_length=1, choices=GENERO)
    image = models.ImageField(upload_to='user_images', null=True, blank=True, default='./user_images/anonimo.svg')

    def __str__(self):
        return f'{self.user}'


#Modelo de categorias
class Categoria(models.Model):
    id = models.BigAutoField(primary_key=True)
    nombre = models.CharField(max_length=30, null=False, blank=False)
    descripcion = models.CharField(max_length=250, null=False, blank=False)
    category_image = models.ImageField(upload_to='categorias' , null=True)
    url_name = models.CharField(max_length=30, null=False, blank=False)

    def __str__(self):
        return f'{self.nombre}'




#Modelo de Articulo
class Articulo(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    nombre =models.CharField( max_length=80, null=False, blank=False)
    descripcion = models.CharField(max_length=240, null=False, blank=False)
    precio_minimo = models.IntegerField(null=True, blank=True)
    imagen =  models.ImageField(upload_to='articulos_images', null=True)

    def __str__(self):
        return f'{self.nombre}, {self.descripcion}'


class Publicacion(models.Model):
    is_active = models.BooleanField(default=True, null=False, blank=False)
    articulo = models.OneToOneField(Articulo, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.articulo}, {self.is_active}'


class Subasta(models.Model):
    articulo = models.OneToOneField(Articulo, on_delete=models.CASCADE)
    user_ganador = models.ForeignKey(User, on_delete=models.CASCADE)
    precio_ganador = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return f'Usuario ganador: {self.user_ganador}, Precio ganador: {self.precio_ganador}'