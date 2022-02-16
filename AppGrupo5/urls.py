from unicodedata import name
from xml.dom.minidom import Document
from django.urls import path
from AppGrupo5 import views
from django.contrib.auth.views import LogoutView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    
    path('instrumentos/',views.instrumentos, name="instrumentos"),
    #path('pedal/', views.pedal, name= "pedal"),
    path('disco/',views.disco, name= "disco"),
    path('', views.inicio, name="inicio"),
    path('about/', views.about, name="about"),
    path('paginaenconstruccion/',views.paginaenconstruccion,name="paginaenconstruccion"),
    #path('cargainstrumento/',views.Carga_Instrumento,name="cargainstrumento"),
    path('buscarinstrumento/',views.buscarinstrumento),
    path('buscardisco/',views.buscardisco),
    
#MENU USUARIO#
    path('login/', views.login_request, name='Login'),
    path('registro/', views.register, name='Register'),
    path ('logout/', LogoutView.as_view(template_name='AppGrupo5/logout.html'), name='Logout'),
    path ('editarPerfil/', views.editarPerfil, name='EditarPerfil'),

#CRUD VISTA BASADA EN CLASE#

#Instrumentos#
    
    path('listaInstrumentos/',views.ListaInstrumentos.as_view(), name='Lista'),
    path('detalleInstrumentos/<pk>',views.DetalleInstrumento.as_view(), name='Detalle'),
    path('crearInstrumentos/',views.CrearInstrumento.as_view(), name='CrearInstrumento'),
    path('actualizarInstrumentos/<pk>',views.ActualizarInstrumento.as_view(), name='Actualizar'),
    path('borrarInstrumentos/<pk>',views.BorrarInstrumento.as_view(), name='Borrar'),
    path('single/', views.single, name ='Single'),
    
    
#Discos#
    
    path('listaDiscos/',views.ListaDiscos.as_view(), name='ListaDiscos'),
    path('detalleDiscos/<pk>',views.DetalleDiscos.as_view(), name='DetalleDiscos'),
    path('crearDiscos/',views.CrearDiscos.as_view(), name='CrearDiscos'),
    path('actualizarDiscos/<pk>',views.ActualizarDiscos.as_view(), name='ActualizarDiscos'),
    path('borrarDiscos/<pk>',views.BorrarDiscos.as_view(), name='BorrarDiscos'),



#AVATAR
    path('agregarAvatar', views.agregarAvatar , name="agregarAvatar"),



]

