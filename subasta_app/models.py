from django.db import models
from django.contrib.auth.models import User

# Create your models here.

#Modelo de Perfil de usuario
class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='user_images', null=True, blank=True, default='./user_images/anonimo.svg')






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


class Subasta(models.Model):
    articulo = models.OneToOneField(Articulo, on_delete=models.CASCADE)
    user_ganador = models.ForeignKey(User, on_delete=models.CASCADE)
    precio_ganador = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return f'Usuario ganador: {self.user_ganador}, Precio ganador: {self.precio_ganador}'