from django.shortcuts import render,redirect

from django.urls import reverse
from Control.forms import Formulario
# Create your views here
from Control.models import Basquet,Tenis,Rugby,Futbol

from django.template import Template,Context

def Inicio(request):
    return render (request,'control/inicio.html')



  
def InscribirseTenis(request):
   if request.method == "POST":
       formulario = Formulario(request.POST)

       if formulario.is_valid():
           data=formulario.cleaned_data
           nombre= data ["nombre"]
           apellido= data ["apellido"]
           dni= data ["dni"]
           email= data ["email"]
           telefono = data["telefono"]
           tenis = Tenis(nombre=nombre,apellido=apellido,dni=dni,email=email,telefono=telefono)
           tenis.save()  # Lo guardan en la Base de datos

           # Redirecciono al usuario a la lista de cursos
           url_exitosa = reverse('Inicio')  # estudios/cursos/
           return redirect(url_exitosa)
   else:  # GET
       formulario = Formulario()
   http_response = render(
       request=request,
       template_name='control/formulario_tenis.html',
       context={'formulario': formulario}
   )
   return http_response
  

def InscribirseRugby(request):
   if request.method == "POST":
       formulario = Formulario(request.POST)

       if formulario.is_valid():
           data=formulario.cleaned_data
           nombre= data ["nombre"]
           apellido= data ["apellido"]
           dni= data ["dni"]
           email= data ["email"]
           rugby = Rugby(nombre=nombre,apellido=apellido,dni=dni,email=email)
           rugby.save()  # Lo guardan en la Base de datos

           # Redirecciono al usuario a la lista de cursos
           url_exitosa = reverse('Inicio')  # estudios/cursos/
           return redirect(url_exitosa)
   else:  # GET
       formulario = Formulario()
   http_response = render(
       request=request,
       template_name='control/formulario_rugby.html',
       context={'formulario': formulario}
   )
   return http_response
  
def InscribirseFutbol(request):
    if request.method == "POST":
       formulario = Formulario(request.POST)

       if formulario.is_valid():
           data=formulario.cleaned_data
           nombre= data ["nombre"]
           apellido= data ["apellido"]
           dni= data ["dni"]
           email= data ["email"]
           telefono = data["telefono"]
           futbol = Futbol(nombre=nombre,apellido=apellido,dni=dni,email=email,telefono=telefono)
           futbol.save()  # Lo guardan en la Base de datos

           # Redirecciono al usuario a la lista de cursos
           url_exitosa = reverse('Inicio')  # estudios/cursos/
           return redirect(url_exitosa)
    else:  # GET
       formulario = Formulario()
    http_response = render(
       request=request,
       template_name='control/formulario_futbol.html',
       context={'formulario': formulario}
   )
    return http_response
  

def InscribirseBasquet(request):
   if request.method == "POST":
       formulario = Formulario(request.POST)

       if formulario.is_valid():
           data=formulario.cleaned_data
           nombre= data ["nombre"]
           apellido= data ["apellido"]
           dni= data ["dni"]
           email= data ["email"]
           telefono = data["telefono"]
           basquet = Basquet(nombre=nombre,apellido=apellido,dni=dni,email=email,telefono=telefono)
           basquet.save()  # Lo guardan en la Base de datos

           # Redirecciono al usuario a la lista de cursos
           url_exitosa = reverse('Inicio')  # estudios/cursos/
           return redirect(url_exitosa)
   else:  # GET
       formulario = Formulario()
   http_response = render(
       request=request,
       template_name='control/formulario_basquet.html',
       context={'formulario': formulario}
   )
   return http_response
  
def buscar_jugadores(request):
   if request.method == "POST":
        data = request.POST
        busqueda = data["busqueda"]
        # Filtro simple
        nombre = Basquet.objects.filter(nombre__contains=busqueda)
   
   
        # Ejemplo filtro avanzado
        # basquet = Curso.objects.filter(
        #     Q(nombre=busqueda) | Q(comision__contains=busqueda)
        # )
   
   http_response = render(
            request=request,
            template_name='control/lista_basquet.html',
        )
   return http_response
   

   
def listar_jugadores(request):
    # Data de pruebas, más adelante la llenaremos con nuestros cursos de verdad
    contexto = {
        "jugadores": Basquet.objects.all(),
    }
    http_response = render(
        request=request,
        template_name='control/lista_basquet.html',
        context=contexto,
    )
    return http_response



