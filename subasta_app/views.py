from datetime import  datetime
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from .models import Categoria,Articulo, Subasta, Profile, Publicacion, Puja
import datetime



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
      genere = request.POST['genere']
      date_birth = request.POST['date_birth']

    #Creo el usuario con los datos obtenidos del formulario
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

      #Creacion del perfil  del usuario
      perfil = Profile.objects.create(
        user=user,
        genere = genere,
        date_birth = date_birth
        )
      perfil.save()
      
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
    publicaciones = Publicacion.objects.all()

    return render(request, "./subastas_app/articulos.html",
    {
        'articulos': articulos,
        'categoria': categoria,
        'publicaciones': publicaciones
    })

'''Funcion para mostrar la pagina de la subasta del articulo'''
def subasta_articulo(request,articulo_id):
    #Obtengo los objetos para el listado de informacion
    articulo_subasta = Subasta.objects.filter(articulo_id = articulo_id)
    articulo = Articulo.objects.filter(id=articulo_id)
    puja = Puja.objects.filter(articulo_id= articulo_id).order_by('-fecha','-hora').values()
    usuario = User.objects.all()

    #Actualizacion del valor de ultima puja en html
    if request.method == "POST":
        valor_puja = request.POST['valor_puja']
        nueva_puja = Puja.objects.create(
            user = request.user,
            articulo_id = articulo_id,
            precio = valor_puja,
            fecha = datetime.datetime.now()
            )
        nueva_puja.save()           
        return redirect(request.META['HTTP_REFERER'])


    return render(request,"./subastas_app/subasta_articulo.html",
    {
        'articulo_subasta' : articulo_subasta,
        'articulo' : articulo,
        'puja': puja,
        'usuarios': usuario,
    })


'''Funcion para que el usuario agrege articulos de una categoria'''
def agregar_articulo(request):
    #obtengo el nombre de las categorias
    categorias_all = Categoria.objects.all()     

    if request.method == "POST":
        nuevo_articulo = Articulo()
        user = request.user.id
        nombre = request.POST['nombre']
        categoria_id = request.POST['categoria_id']
        descripcion = request.POST['descripcion']
        precio_minimo = request.POST['precio_minimo']
        #fecha_limite = request.PSOT['fecha_limite']
        imagen = request.FILES['imagen']

        nuevo_articulo = Articulo(
            user_id = user,
            nombre = nombre,
            descripcion = descripcion,
            precio_minimo = precio_minimo,
            categoria_id = categoria_id,
            imagen = imagen
        )
        nuevo_articulo.save()

        #Crear publicacion
        publicacion = Publicacion.objects.create(
            articulo = nuevo_articulo
        )
        publicacion.save()

        subasta = Subasta.objects.create(
            user_ganador = request.user,
            articulo = nuevo_articulo,
            fecha_limite = datetime.datetime.now() + datetime.timedelta(30)
        )
        subasta.save()


        return redirect("/categorias/")

    return render(request, "./subastas_app/agregar_articulo.html",{
        'categorias': categorias_all
    })