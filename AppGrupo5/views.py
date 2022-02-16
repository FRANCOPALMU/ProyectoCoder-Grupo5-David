from django.shortcuts import render
from django.http import HttpResponse
from django.template.context import Context
from django.template import loader
from AppGrupo5.forms import AvatarFormulario, CargaInstrumento, UserEditForm, UserRegisterForm
from AppGrupo5.models import Discos, Instrumento, Avatar,User 
import datetime
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout, authenticate  
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import user_passes_test

# Create your views here.
 

def instrumentos(request):
    return render(request, "AppGrupo5/instrumento.html")

def pedal(request):
    return render(request, "AppGrupo5/pedal.html")

def disco(request):
    return render(request, "AppGrupo5/disco.html")

def about(request):
    return render(request, "AppGrupo5/about.html")

def paginaenconstruccion(request):
    return render(request, "AppGrupo5/paginaenconstruccion.html")

def Carga_Instrumento(request):

    if request.method == 'POST':

        miformulario = CargaInstrumento(request.POST)

        print(miformulario)

        if miformulario.is_valid:
            
            informacion = miformulario.cleaned_data

            instrumento = Instrumento (marca = informacion ['marca'], modelo =informacion ['modelo'], tipoinstrumento=informacion['tipoinstrumento'],color=informacion['color'])

            instrumento.save()

            return render (request,"AppGrupo5/inicio.html")
    else:

        miformulario = CargaInstrumento()

    return render (request,"AppGrupo5/cargainstrumento.html", {"miformulario":miformulario})


def buscarinstrumento(request):

    if  request.GET["tipoinstrumento"]:

	      
        tipoinstrumento = request.GET['tipoinstrumento'] 
        Instrumentos = Instrumento.objects.filter(tipoinstrumento__icontains=tipoinstrumento)

        return render(request, "AppGrupo5/instrumento.html", {"Instrumentos":Instrumentos,"Tipo de Instrumento":tipoinstrumento})
    else: 

	    respuesta = "No se han cargado ningún dato"
    return HttpResponse(respuesta)

def buscardisco(request):

    if  request.GET["artista"]:

	      
        artista = request.GET['artista'] 
        Disco = Discos.objects.filter(artista__icontains=artista)

        return render(request, "AppGrupo5/disco.html", {"Disco":Disco,"Artista":artista})
    else: 

	    respuesta = "No se han cargado ningún dato"
    return HttpResponse(respuesta)

# CRUD Avatares --Franco DN. -- #

  


##  Registro --- Franco P --- ##

def register(request):
        
        if request.method == 'POST':
            form = UserRegisterForm(request.POST)

            if form.is_valid():

                username=form.cleaned_data['username']
                form.save()
                return render (request,"AppGrupo5/registro_exitoso.html",{"mensaje":"Usuario Creado Exitosamente:)"})
        else:
            form=UserRegisterForm()
        
        return render(request,"AppGrupo5/registro.html",{"form":form})


# def inicio (request):
    
#      return render(request, "AppGrupo5/inicio.html")




##  Vistas Basadas en Clases ##

# Instrumentos #

class ListaInstrumentos (ListView):
    model = Instrumento
    template_name = 'AppGrupo5/instrumentoLista.html'
    
class DetalleInstrumento (DetailView):
    model = Instrumento
    template_name = 'AppGrupo5/instrumentoDetalle.html'
 
class CrearInstrumento (CreateView):
    model = Instrumento
    success_url = '/AppGrupo5/listaInstrumentos/'
    fields = ['tipoinstrumento', 'marca', 'modelo', 'color']
    template_name = 'AppGrupo5/instrumentoCrear.html'
   
class ActualizarInstrumento (UpdateView):
    model = Instrumento
    success_url = '/AppGrupo5/listaInstrumentos/'
    fields = ['tipoinstrumento', 'marca', 'modelo', 'color']
    template_name = 'AppGrupo5/instrumentoActualizar.html'

class BorrarInstrumento (DeleteView):
    model = Instrumento
    success_url = '/AppGrupo5/listaInstrumentos/'
    template_name = 'AppGrupo5/InstrumentoBorrar_confirm.html'


# Discos #

class ListaDiscos (ListView):
    model = Discos
    template_name = 'AppGrupo5/discosLista.html'
    
    
class DetalleDiscos (DetailView):
    model = Discos
    template_name = 'AppGrupo5/discosDetalle.html'


class CrearDiscos (CreateView):
    model = Discos
    success_url = '/AppGrupo5/listaDiscos/'
    fields = ['album', 'artista', 'fechaLanzamiento']
    template_name = 'AppGrupo5/discoCrear.html'
   
class ActualizarDiscos (UpdateView):
    model = Discos
    success_url = '/AppGrupo5/listaDiscos/'
    fields = ['album', 'artista', 'fechaLanzamiento']
    template_name = 'AppGrupo5/discosActualizar.html'
  
class BorrarDiscos (DeleteView):
    model = Discos
    success_url = '/AppGrupo5/listaDiscos/'
    template_name = 'AppGrupo5/discosBorrar_confirm.html'



# Pedales #







def inicio(request):

     if request.user.is_authenticated:

        avatares = Avatar.objects.filter(user=request.user.id)
      
        return render(request, "AppGrupo5/inicio.html", {"url":avatares[0].imagen.url})
     else:
         
         return render(request, "AppGrupo5/inicio.html")



def about(request):

     if request.user.is_authenticated:

        avatares = Avatar.objects.filter(user=request.user.id)
      
        return render(request, "AppGrupo5/about.html", {"url":avatares[0].imagen.url})
     else:
         
         return render(request, "AppGrupo5/about.html")


def instrumentos(request):

     if request.user.is_authenticated:

        avatares = Avatar.objects.filter(user=request.user.id)
      
        return render(request, "AppGrupo5/instrumento.html", {"url":avatares[0].imagen.url})
     else:
         
         return render(request, "AppGrupo5/instrumento.html")         


def disco(request):

     if request.user.is_authenticated:

        avatares = Avatar.objects.filter(user=request.user.id)
      
        return render(request, "AppGrupo5/disco.html", {"url":avatares[0].imagen.url})
     else:
         
         return render(request, "AppGrupo5/disco.html")  





def agregarAvatar (request):
    if request.method == 'POST':

        miFormulario = AvatarFormulario (request.POST, request.FILES)

        if miFormulario.is_valid():
            u = User.objects.get (username = request.user)
            avatar = Avatar (user=u, imagen = miFormulario.cleaned_data['imagen'])
            avatar.save()
            return render(request, "AppGrupo5/inicio.html")

    else:
        miFormulario = AvatarFormulario() 

        return render(request,"AppGrupo5/agregarAvatar.html", {"miFormulario":miFormulario})   


#Editar Perfil # 


def editarPerfil (request):
    
    usuario = request.user
    
    if (request.method == 'POST'):
        
        form = UserEditForm (request.POST)
        
        if form.is_valid():
            
            data = form.cleaned_data
            
            usuario.email = data ['email']
            usuario.password1 = data ['password1']
            usuario.password2 = data ['password2']
            usuario.first_name = data ['first_name']
            usuario.last_name = data ['last_name']
            
            usuario.save()
            
            return render (request, 'AppGrupo5/inicio.html')
            #return HttpResponse('Se ha modificado con exito')
        
    else:
        
        form = UserEditForm (initial = {'email' : usuario.email, "first_name" : usuario.first_name, "last_name" : usuario.last_name})  
        
        return render (request, "AppGrupo5/editarPerfil.html", {"form" : form, 'usuario': usuario})
  



##  Login --- Franco DN. --- ##
def login_request (request):

    if request.method == "POST":
        form = AuthenticationForm (request,data = request.POST)

        if form.is_valid():
            usuario = form.cleaned_data.get ('username')
            contra = form.cleaned_data.get('password')

            user = authenticate (username = usuario, password = contra)

            if user is not None:
                login (request, user)
                
                avatares=Avatar.objects.filter(user=request.user.id)

                return render (request, "AppGrupo5/inicio.html", {"mensaje": f"Bienvenido {user.get_username}", 'url':avatares[0].imagen.url })
            else:
                return render (request, "AppGrupo5/inicio.html", {"mensaje":"Datos incorrectos"})

        else:
            return render(request,"AppGrupo5/inicio.html", {"mensaje": "Formulario erroneo"})

    form = AuthenticationForm()

    return render ( request, 'AppGrupo5/login.html', {'form':form})


def single (request):
    return render (request,"AppGrupo5/single.html")