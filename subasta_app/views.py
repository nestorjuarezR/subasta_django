from django.contrib.auth.models import User
from django.shortcuts import render, redirect

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