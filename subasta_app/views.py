from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from .models import Categoria,Articulo
# Create your views here.
'''Funcion que muestra el index'''
def index(request):
    '''Pagina Index'''
    return render(request, "./subastas_app/index.html")


def registro(request):
   if request.method == "POST":
      first_name = request.POST['first_name']
      last_name = request.POST['last_name']
      username = request.POST['username']
      password = request.POST['password']
      email = request.POST['email']


      user = User.objects.create_user(
         username =  username,
         email = email,
         first_name = first_name,
         last_name = last_name,
         is_staff=False,
         is_active = True,
      )
      user.set_password(password)
      user.save()
      next = request.GET.get("next", "/login/")

      return redirect(next)

   return render(request, "./subastas_app/registro.html")



'''Funcion que muestra la pagina con las categorias'''
def categorias_subastas(request):
    categorias_all = Categoria.objects.all()                                    #Consulta y selecciona todas las categorias registras
    return render(request, "./subastas_app/categorias.html",
    {
        "categorias": categorias_all
    })


    '''Funcion que muestra la pagina de articulos de una categoria'''
def articulos_categoria(request, categoria_nombre):
    categoria = Categoria.objects.filter(nombre=categoria_nombre)
    articulos = Articulo.objects.all()
    #categorias = Categoria.objects.all()    
    print(articulos)
    return render(request, "./subastas_app/articulos.html",
    {
        'articulos': articulos,
        'categoria': categoria
    })