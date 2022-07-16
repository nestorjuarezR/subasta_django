from django.db import models

# Create your models here.

#Modelo de categorias
class Categoria(models.Model):
    id = models.BigAutoField(primary_key=True)
    nombre = models.CharField(max_length=30, null=False, blank=False)
    descripcion = models.CharField(max_length=250, null=False, blank=False)
    category_image = models.ImageField(upload_to='categorias' , null=True)
    url_name = models.CharField(max_length=30, null=False, blank=False)

    def __str__(self):
        return f'{self.nombre}'